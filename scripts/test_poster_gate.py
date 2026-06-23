#!/usr/bin/env python3
"""
Unit tests for the VirtueVigil poster-pipeline vision safety gate.

These tests MOCK the vision model + network entirely. No real OpenAI/Brave/OMDb
calls are made and NO real explicit content is ever used. The "explicit" case
is simulated purely by mocking the vision verdict.

Covered cases:
  1. explicit            -> REJECT, queued, placeholder used (no raw image saved)
  2. non-poster          -> REJECT, queued, placeholder used
  3. title mismatch      -> REJECT, queued, placeholder used
  4. valid poster        -> ACCEPT, image promoted (no placeholder)
  5. vision error/timeout-> placeholder + queue (fail safe)
  6. vision_safety_check accept logic (truth table)
  7. download_image_to_temp never writes to the poster dir

Run: python3 test_poster_gate.py
"""

import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT_DIR = Path(__file__).parent

# Load the pipeline module by file path (hyphenated filename).
_spec = importlib.util.spec_from_file_location("poster_pipeline", SCRIPT_DIR / "poster-pipeline.py")
pp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pp)


def _make_fake_jpeg(path):
    """Write minimal bytes that pass the JPEG magic-byte + size check (>1KB)."""
    with open(path, "wb") as f:
        f.write(b"\xff\xd8" + b"\x00" * 2000)


class GateTestBase(unittest.TestCase):
    def setUp(self):
        # Redirect POSTER_DIR and the review queue into a temp sandbox so we
        # never touch the live repo.
        self.tmpdir = tempfile.mkdtemp(prefix="vv_gate_test_")
        self.poster_dir = Path(self.tmpdir) / "posters"
        self.poster_dir.mkdir(parents=True, exist_ok=True)
        self.queue_path = Path(self.tmpdir) / "poster-review-queue.json"

        self._orig_poster_dir = pp.POSTER_DIR
        self._orig_queue_path = pp.REVIEW_QUEUE_PATH
        pp.POSTER_DIR = self.poster_dir
        pp.REVIEW_QUEUE_PATH = self.queue_path

        # Reset stats between tests.
        for k in ("omdb", "brave", "placeholder", "failed", "skipped", "rejected", "queued"):
            pp.stats[k] = 0
        pp.stats["failed_slugs"] = []

    def tearDown(self):
        pp.POSTER_DIR = self._orig_poster_dir
        pp.REVIEW_QUEUE_PATH = self._orig_queue_path

    def _read_queue(self):
        if not self.queue_path.exists():
            return []
        with open(self.queue_path) as f:
            return json.load(f)


class TestProcessPosterGate(GateTestBase):
    """End-to-end process_poster behavior with OMDb forced to fail."""

    def _run_with_vision(self, vision_verdict, slug="test-movie-2026", title="Test Movie", year=2026):
        """
        Force: OMDb returns nothing, Brave returns a URL, the candidate
        downloads to a temp JPEG, and the vision check returns vision_verdict.
        """
        fake_temp = os.path.join(self.tmpdir, "candidate.jpg")
        _make_fake_jpeg(fake_temp)

        with mock.patch.object(pp, "query_omdb", return_value=None), \
             mock.patch.object(pp, "search_brave_images", return_value="https://example.com/img.jpg"), \
             mock.patch.object(pp, "download_image_to_temp", return_value=fake_temp), \
             mock.patch.object(pp, "vision_safety_check", return_value=vision_verdict), \
             mock.patch.object(pp, "time") as _t:  # neutralize sleeps
            _t.sleep = lambda *_a, **_k: None
            result = pp.process_poster(slug, title, year, existing={}, brave_key="bk", openai_key="ok")
        return result

    def test_explicit_rejected(self):
        verdict = {"accept": False, "is_explicit": True, "is_movie_poster": True,
                   "matches_title": True, "reason": "nudity detected", "error": None}
        result = self._run_with_vision(verdict, slug="explicit-2026")
        self.assertEqual(result, "placeholder")
        # No Brave image promoted; the saved file must be the generated placeholder.
        self.assertTrue((self.poster_dir / "explicit-2026.jpg").exists())
        self.assertEqual(pp.stats["rejected"], 1)
        q = self._read_queue()
        self.assertEqual(len(q), 1)
        self.assertIn("explicit", q[0]["reason"])

    def test_non_poster_rejected(self):
        verdict = {"accept": False, "is_explicit": False, "is_movie_poster": False,
                   "matches_title": False, "reason": "random photo", "error": None}
        result = self._run_with_vision(verdict, slug="nonposter-2026")
        self.assertEqual(result, "placeholder")
        self.assertEqual(pp.stats["rejected"], 1)
        q = self._read_queue()
        self.assertIn("not_poster", q[0]["reason"])

    def test_title_mismatch_rejected(self):
        verdict = {"accept": False, "is_explicit": False, "is_movie_poster": True,
                   "matches_title": False, "reason": "different movie", "error": None}
        result = self._run_with_vision(verdict, slug="mismatch-2026")
        self.assertEqual(result, "placeholder")
        self.assertEqual(pp.stats["rejected"], 1)
        q = self._read_queue()
        self.assertIn("title_mismatch", q[0]["reason"])

    def test_valid_poster_accepted(self):
        verdict = {"accept": True, "is_explicit": False, "is_movie_poster": True,
                   "matches_title": True, "reason": "legit poster", "error": None}
        result = self._run_with_vision(verdict, slug="valid-2026")
        self.assertEqual(result, "brave")
        # The promoted file should be our fake candidate bytes, not a placeholder.
        saved = (self.poster_dir / "valid-2026.jpg").read_bytes()
        self.assertEqual(saved[:2], b"\xff\xd8")
        self.assertEqual(len(saved), 2002)  # exact size of fake candidate
        self.assertEqual(pp.stats["rejected"], 0)
        self.assertEqual(len(self._read_queue()), 0)

    def test_vision_error_falls_back_and_queues(self):
        verdict = {"accept": False, "is_explicit": True, "is_movie_poster": False,
                   "matches_title": False, "reason": "Vision check failed: timeout",
                   "error": "vision_error"}
        result = self._run_with_vision(verdict, slug="visionerr-2026")
        self.assertEqual(result, "placeholder")
        q = self._read_queue()
        self.assertEqual(len(q), 1)
        self.assertIn("vision_error", q[0]["reason"])
        # File on disk must be the safe placeholder, never a raw web image.
        self.assertTrue((self.poster_dir / "visionerr-2026.jpg").exists())


class TestVisionSafetyCheckLogic(GateTestBase):
    """Unit-test vision_safety_check accept logic with mocked HTTP."""

    def _fake_openai_response(self, verdict_dict):
        body = json.dumps({
            "choices": [{"message": {"content": json.dumps(verdict_dict)}}]
        }).encode("utf-8")

        class FakeResp:
            def __enter__(self_inner):
                return self_inner
            def __exit__(self_inner, *a):
                return False
            def read(self_inner):
                return body
        return FakeResp()

    def _check(self, verdict_dict):
        tmp = os.path.join(self.tmpdir, "vc.jpg")
        _make_fake_jpeg(tmp)
        with mock.patch.object(pp.urllib.request, "urlopen",
                               return_value=self._fake_openai_response(verdict_dict)):
            return pp.vision_safety_check(tmp, "Test Movie", 2026, "fake-key")

    def test_all_positive_accepts(self):
        r = self._check({"is_explicit": False, "is_movie_poster": True,
                         "matches_title": True, "reason": "ok"})
        self.assertTrue(r["accept"])

    def test_explicit_blocks_accept(self):
        r = self._check({"is_explicit": True, "is_movie_poster": True,
                         "matches_title": True, "reason": "nsfw"})
        self.assertFalse(r["accept"])

    def test_missing_key_fails_safe(self):
        tmp = os.path.join(self.tmpdir, "vc2.jpg")
        _make_fake_jpeg(tmp)
        r = pp.vision_safety_check(tmp, "Test Movie", 2026, openai_key=None)
        self.assertFalse(r["accept"])
        self.assertEqual(r["error"], "missing_key")

    def test_http_error_fails_safe(self):
        tmp = os.path.join(self.tmpdir, "vc3.jpg")
        _make_fake_jpeg(tmp)
        with mock.patch.object(pp.urllib.request, "urlopen", side_effect=Exception("timeout")):
            r = pp.vision_safety_check(tmp, "Test Movie", 2026, "fake-key")
        self.assertFalse(r["accept"])
        self.assertEqual(r["error"], "vision_error")


class TestTempIsolation(GateTestBase):
    """download_image_to_temp must never write into the poster directory."""

    def test_temp_not_in_poster_dir(self):
        fake_bytes = b"\xff\xd8" + b"\x00" * 3000

        class FakeResp:
            def __enter__(self_inner): return self_inner
            def __exit__(self_inner, *a): return False
            def read(self_inner): return fake_bytes

        with mock.patch.object(pp.urllib.request, "urlopen", return_value=FakeResp()):
            tmp_path = pp.download_image_to_temp("https://example.com/x.jpg")
        self.assertIsNotNone(tmp_path)
        self.assertFalse(str(self.poster_dir) in str(tmp_path))
        # Poster dir stays empty until something is explicitly promoted.
        self.assertEqual(list(self.poster_dir.glob("*.jpg")), [])
        os.unlink(tmp_path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
