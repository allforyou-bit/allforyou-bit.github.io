"""Work A-Hero Phase 3: standardize <header> → <section class="page-hero"> in 11 trade pages."""
import re, sys, datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

def sp(t):
    sys.stdout.buffer.write((str(t) + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()

TRADE_CODES = {
    '421a': '421A', '310t': '310T', '309a': '309A', '310s': '310S',
    '308a': '308A', '276a': '276A', '447a': '447A', '313a': '313A',
    '442a': '442A', '403a': '403A', '306a': '306A',
}

# Matches the full <header>...</header> block (single occurrence expected)
HEADER_PAT = re.compile(r'<header>(.*?)</header>', re.DOTALL)

passed = []
failed = []
rollbacks = []

for code, trade_code in TRADE_CODES.items():
    fname = f'{code}.html'
    path = BASE / fname
    src = path.read_text(encoding='utf-8')
    orig = src

    # ── find header block ──────────────────────────────────────────
    m = HEADER_PAT.search(src)
    if not m:
        sp(f'  FAIL [{fname}]: <header> not found')
        failed.append(fname + ' (no header)')
        continue

    inner = m.group(1)  # content between <header> and </header>

    # ── extract h1 text (preserve exactly as-is) ──────────────────
    h1_m = re.search(r'<h1>(.*?)</h1>', inner, re.DOTALL)
    if not h1_m:
        sp(f'  FAIL [{fname}]: <h1> not found inside header')
        failed.append(fname + ' (no h1)')
        continue
    h1_text = h1_m.group(1).strip()

    # ── extract subtitle <p> (preserve text as-is) ────────────────
    p_m = re.search(r'<p>(.*?)</p>', inner, re.DOTALL)
    subtitle_text = p_m.group(1).strip() if p_m else 'Canada Certification Exam Practice Questions | 2026'

    # ── extract existing pill spans (preserve exactly) ─────────────
    pills = re.findall(r'<span class="(?:badge|update-pill|rsos-pill)">[^<]*</span>', inner)

    # ── check if trade-badge already present ──────────────────────
    has_badge = 'class="trade-badge"' in inner

    # ── build pill-badges block ────────────────────────────────────
    if pills:
        pill_lines = '\n'.join(f'    {p}' for p in pills)
        pill_block = f'  <div class="pill-badges">\n{pill_lines}\n  </div>'
    else:
        pill_block = '  <div class="pill-badges"></div>'

    # ── build new hero section ─────────────────────────────────────
    if has_badge:
        # 421a already has trade-badge span — keep existing structure in new wrapper
        new_hero = (
            f'<section class="page-hero">\n'
            f'  <span class="trade-badge">{trade_code}</span>\n'
            f'  <h1>{h1_text}</h1>\n'
            f'  <p class="subtitle">{subtitle_text}</p>\n'
            f'{pill_block}\n'
            f'</section>'
        )
    else:
        new_hero = (
            f'<section class="page-hero">\n'
            f'  <span class="trade-badge">{trade_code}</span>\n'
            f'  <h1>{h1_text}</h1>\n'
            f'  <p class="subtitle">{subtitle_text}</p>\n'
            f'{pill_block}\n'
            f'</section>'
        )

    # ── replace full header block ──────────────────────────────────
    new_src = HEADER_PAT.sub(new_hero, src, count=1)

    if new_src == src:
        sp(f'  UNCHANGED [{fname}]: replacement produced no change')
        failed.append(fname + ' (unchanged)')
        continue

    # ── write file ────────────────────────────────────────────────
    path.write_text(new_src, encoding='utf-8')

    # ── immediate grep verification ────────────────────────────────
    txt = path.read_text(encoding='utf-8')
    v_page_hero = txt.count('class="page-hero"')
    v_trade_badge = txt.count('class="trade-badge"')
    v_h1 = txt.count('<h1>')
    v_placeholder_code = txt.count('[TRADE_CODE]')
    v_placeholder_name = txt.count('[TRADE_NAME]')

    ok = (v_page_hero == 1 and v_trade_badge >= 1 and v_h1 >= 1
          and v_placeholder_code == 0 and v_placeholder_name == 0)

    if ok:
        sp(f'  OK [{fname}]: page-hero={v_page_hero} trade-badge={v_trade_badge} h1={v_h1} placeholders=0')
        passed.append(fname)
    else:
        sp(f'  FAIL [{fname}]: page-hero={v_page_hero} trade-badge={v_trade_badge} h1={v_h1} '
           f'placeholder-code={v_placeholder_code} placeholder-name={v_placeholder_name}')
        # rollback
        path.write_text(orig, encoding='utf-8')
        failed.append(fname + f' (grep fail)')
        rollbacks.append(fname)
        sp(f'  ROLLBACK [{fname}]: restored from memory')

sp(f'\n=== SUMMARY ===')
sp(f'Passed: {len(passed)}/{len(TRADE_CODES)} — {passed}')
sp(f'Failed: {len(failed)} — {failed}')
sp(f'Rollbacks: {rollbacks}')
