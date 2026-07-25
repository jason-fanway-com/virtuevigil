#!/usr/bin/env python3
"""Extract top 15 most-woke action films from reviews.json"""
import json, sys

with open(sys.argv[1]) as f:
    reviews = json.load(f)

films = [r for r in reviews if r.get('type') == 'film' and 'wokeScore' in r and 'tradScore' in r]
action = [r for r in films if 'Action' in r.get('genre', '')]
action.sort(key=lambda r: r['tradScore'] - r['wokeScore'])

for i, r in enumerate(action[:15]):
    m = r['tradScore'] - r['wokeScore']
    print(f"{i+1}|{r['title']}|{r.get('year','?')}|{r['wokeScore']:.1f}|{r['tradScore']:.1f}|{m:.1f}|{r.get('verdict','?')}|{r.get('slug','?')}")