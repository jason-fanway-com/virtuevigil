#!/usr/bin/env python3
"""Add 3 MCU reviews to reviews.json"""
import json, sys

with open('src/data/reviews.json') as f:
    reviews = json.load(f)

# Just print current count, the actual data will come from stdin
print(f"Current reviews: {len(reviews)}")
