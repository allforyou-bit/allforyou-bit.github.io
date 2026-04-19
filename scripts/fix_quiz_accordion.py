#!/usr/bin/env python3
"""
작업 3: Exam Structure 표를 accordion(<details>)으로 변환
대상: 421a, 276a, 313a, 442a, 447a (Exam Structure가 있는 퀴즈 페이지)
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ACCORDION_CSS = """
  /* ── EXAM STRUCTURE ACCORDION ── */
  .exam-accordion{margin-bottom:20px}
  .exam-accordion summary{cursor:pointer;color:var(--primary);font-weight:700;font-size:.95rem;padding:12px 16px;background:var(--card);border-radius:8px;border-left:4px solid var(--accent);box-shadow:0 1px 5px rgba(0,0,0,.07);list-style:none;display:flex;justify-content:space-between;align-items:center}
  .exam-accordion summary::-webkit-details-marker{display:none}
  .exam-accordion summary::after{content:\"▼\";font-size:.75rem;opacity:.6;transition:transform .2s}
  .exam-accordion[open] summary::after{transform:rotate(180deg)}
  .exam-accordion .concept-section{border-radius:0 0 8px 8px;margin-top:0;box-shadow:0 2px 6px rgba(0,0,0,.06)}"""

TARGETS = ['421a.html','276a.html','313a.html','442a.html','447a.html']

changed = []
out = sys.stdout.buffer

for fname in TARGETS:
    f = ROOT / fname
    if not f.exists():
        out.write(f"SKIP (not found): {fname}\n".encode())
        continue
    text = f.read_text(encoding='utf-8')
    original = text

    # Skip if already converted
    if 'exam-accordion' in text:
        out.write(f"SKIP (already done): {fname}\n".encode())
        continue

    # Find concept-section containing "Exam Structure" header
    # Try with comment prefix first (421a style), then without (276a style)
    pattern_with_comment = re.compile(
        r'(  <!-- EXAM STRUCTURE -->\s*\n)'
        r'(  <div class="concept-section">.*?</div>\n)',
        re.DOTALL
    )
    pattern_no_comment = re.compile(
        r'(\n  <div class="concept-section">\s*\n\s*<h3>Exam Structure[^<]*</h3>.*?</div>\n)',
        re.DOTALL
    )

    m = pattern_with_comment.search(text)
    has_comment = bool(m)
    if not m:
        m = pattern_no_comment.search(text)

    if not m:
        out.write(f"PATTERN NOT FOUND: {fname}\n".encode())
        continue

    old_block = m.group(0)
    inner_div = m.group(2) if has_comment else m.group(1)

    # Normalize indent
    inner_div_clean = inner_div.strip('\n')

    # Extract h3 title for summary
    h3_m = re.search(r'<h3>(.*?)</h3>', inner_div_clean)
    title = h3_m.group(1) if h3_m else 'Exam Structure — Topic Breakdown'

    if has_comment:
        new_block = (
            f'  <!-- EXAM STRUCTURE -->\n'
            f'  <details class="exam-accordion">\n'
            f'    <summary>{title}</summary>\n'
            f'{inner_div}'
            f'  </details>\n'
        )
    else:
        new_block = (
            f'\n  <details class="exam-accordion">\n'
            f'    <summary>{title}</summary>\n'
            f'  {inner_div_clean}\n'
            f'  </details>\n'
        )

    text = text.replace(old_block, new_block, 1)

    # Add CSS before closing </style>
    if ACCORDION_CSS.strip() not in text:
        text = text.replace('</style>', ACCORDION_CSS + '\n</style>', 1)

    if text != original:
        f.write_text(text, encoding='utf-8')
        changed.append(fname)
        out.write(f"OK: {fname}\n".encode())

out.write(f"\nTotal changed: {len(changed)}\n".encode())
