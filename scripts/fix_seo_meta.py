#!/usr/bin/env python3
"""
작업 4: og:image + twitter:card 최적화
- og:image 전 페이지 추가
- twitter:card summary → summary_large_image
- twitter:image 추가
- 누락된 twitter block 추가
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OG_IMAGE = "https://allforyou-bit.github.io/favicon.svg"

changed = []

for f in sorted(ROOT.glob("*.html")):
    if f.name == "404.html":
        continue
    text = f.read_text(encoding="utf-8")
    original = text

    # 1. og:image 추가 (없을 경우 og:type 뒤에 삽입)
    if 'property="og:image"' not in text and 'property="og:type"' in text:
        text = re.sub(
            r'(<meta property="og:type" content="[^"]*">)',
            r'\1\n<meta property="og:image" content="' + OG_IMAGE + r'">',
            text
        )

    # 2. twitter:card summary → summary_large_image
    text = text.replace(
        'content="summary">',
        'content="summary_large_image">'
    )

    # 3. twitter:image 추가 (없을 경우 twitter:description 뒤에 삽입)
    if 'name="twitter:image"' not in text and 'name="twitter:description"' in text:
        text = re.sub(
            r'(<meta name="twitter:description" content="[^"]*">)',
            r'\1\n<meta name="twitter:image" content="' + OG_IMAGE + r'">',
            text
        )

    # 4. twitter block 완전 누락 시 og:image 뒤에 추가
    if 'name="twitter:card"' not in text and 'property="og:title"' in text:
        og_title_m = re.search(r'property="og:title" content="([^"]*)"', text)
        og_desc_m  = re.search(r'property="og:description" content="([^"]*)"', text)
        og_title = og_title_m.group(1) if og_title_m else ""
        og_desc  = og_desc_m.group(1)[:200] if og_desc_m else ""
        twitter_block = (
            f'\n<meta name="twitter:card" content="summary_large_image">'
            f'\n<meta name="twitter:title" content="{og_title}">'
            f'\n<meta name="twitter:description" content="{og_desc}">'
            f'\n<meta name="twitter:image" content="{OG_IMAGE}">'
        )
        # Insert after og:image line if exists, else after og:type
        if 'property="og:image"' in text:
            text = re.sub(
                r'(<meta property="og:image" content="[^"]*">)',
                r'\1' + twitter_block,
                text
            )
        elif 'property="og:type"' in text:
            text = re.sub(
                r'(<meta property="og:type" content="[^"]*">)',
                r'\1' + twitter_block,
                text
            )

    if text != original:
        f.write_text(text, encoding="utf-8")
        changed.append(f.name)

out = sys.stdout.buffer
out.write(f"SEO meta fixed: {len(changed)} files\n".encode())
for fn in changed:
    out.write(f"  - {fn}\n".encode())
