#!/usr/bin/env python3
"""작업 5: 누락된 내부 링크 추가 (salary 페이지 → common-mistakes/exam-tips)"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
out = sys.stdout.buffer

LINK_STYLE = 'style="background:#eaf0f9;border-radius:8px;padding:16px;text-decoration:none;color:#1a3a5c;font-size:.88rem;font-weight:600;border-left:4px solid #f0a500;display:block"'
SUB_STYLE = 'style="display:block;font-size:.8rem;color:#7f8c8d;font-weight:400;margin-top:4px"'

ADDITIONS = {
    'heavy-equipment-technician-salary-canada.html': [
        ('/common-mistakes-421a-exam.html', '421A Common Exam Mistakes', 'Avoid the most frequent errors on exam day'),
    ],
    'truck-transport-mechanic-310t-salary-canada.html': [
        ('/how-to-pass-red-seal-310t-exam.html', 'How to Pass the 310T Exam', 'Exam strategy, topics, and study tips'),
        ('/common-mistakes-310t-exam.html', '310T Common Exam Mistakes', 'Avoid the most frequent errors on exam day'),
    ],
    'construction-electrician-309a-salary-canada.html': [
        ('/how-to-pass-red-seal-309a-exam.html', 'How to Pass the 309A Exam', 'Exam strategy, topics, and study tips'),
        ('/common-mistakes-309a-exam.html', '309A Common Exam Mistakes', 'Avoid the most frequent errors on exam day'),
    ],
}

changed = []
for filename, links in ADDITIONS.items():
    f = ROOT / filename
    if not f.exists():
        out.write(f'MISSING: {filename}\n'.encode())
        continue
    text = f.read_text(encoding='utf-8')
    original = text

    for href, title, subtitle in links:
        if href.lstrip('/') in text:
            continue
        new_card = f'\n      <a href="{href}" {LINK_STYLE}>{title}<span {SUB_STYLE}>{subtitle}</span></a>'
        # Insert before closing </div> of the related guides grid
        # Find the last </a> in the related grid and insert after it
        text = text.replace(
            '</a>\n    </div>\n  </div>\n  <!-- AdSense',
            f'</a>{new_card}\n    </div>\n  </div>\n  <!-- AdSense',
            1
        )

    if text != original:
        f.write_text(text, encoding='utf-8')
        changed.append(filename)
        out.write(f'OK: {filename}\n'.encode())

out.write(f'\nTotal changed: {len(changed)}\n'.encode())
