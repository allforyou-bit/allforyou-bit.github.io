#!/usr/bin/env python3
"""
작업 1: AdSense placeholder 텍스트 제거 → <!-- AdSense placeholder -->
작업 2: 뉴스레터 허위 숫자 수정
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
html_files = list(ROOT.glob("*.html"))

changed_ads = []
changed_news = []

for f in html_files:
    text = f.read_text(encoding="utf-8")
    original = text

    # --- 작업 1: AdSense placeholder 제거 ---
    # Pattern A: single-line article variant (— or &mdash;)
    text = re.sub(
        r'\s*<div class="ad-banner">Advertisement\s*(?:—|&mdash;)\s*Google AdSense</div>',
        '\n  <!-- AdSense placeholder -->',
        text
    )
    # Pattern B: multi-line quiz variant (📢 ...)
    text = re.sub(
        r'<div class="ad-banner">\s*📢 Advertisement[^<]*<br>\s*<small>[^<]*</small>\s*</div>',
        '<!-- AdSense placeholder -->',
        text
    )

    # --- 작업 2: 뉴스레터 허위 숫자 수정 ---
    text = text.replace(
        "Join 1,000+ Red Seal candidates. Get 10 new practice questions + exam strategies weekly — free.",
        "Join fellow Red Seal candidates. Get exam tips and new questions — free."
    )
    text = text.replace(
        "Join 1,000+ Red Seal candidates",
        "Join fellow Red Seal candidates"
    )
    text = text.replace(
        "Get 10 new practice questions",
        "Get exam tips and new questions — free."
    )

    if text != original:
        f.write_text(text, encoding="utf-8")
        name = f.name
        ads_changed = "Advertisement" in original and "Advertisement" not in text.replace("<!-- AdSense placeholder -->", "")
        news_changed = "1,000+" in original or "10 new practice" in original
        if ads_changed:
            changed_ads.append(name)
        if news_changed:
            changed_news.append(name)

import sys
out = sys.stdout.buffer
out.write(f"AdSense removed: {len(changed_ads)} files\n".encode())
for f in sorted(changed_ads):
    out.write(f"  - {f}\n".encode())
out.write(f"\nNewsletter fixed: {len(changed_news)} files\n".encode())
for f in sorted(changed_news):
    out.write(f"  - {f}\n".encode())
