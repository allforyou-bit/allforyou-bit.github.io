"""
fix_quiz_layout.py
For all 9 quiz pages:
1. Fix remaining 'Advertisement — Google AdSense' ad-banners → comment
2. Move score-box, topic-progress-panel, mock-launch-bar to BELOW question-card
3. Change Download Study Sheet button → Coming Soon (disabled)
"""
import os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

QUIZ_FILES = [
    '308a.html', '309a.html', '310s.html', '310t.html',
    '276a.html', '447a.html', '313a.html', '442a.html', '421a.html'
]


def find_div_end(html, div_start):
    """Given position of '<div', return position right after matching '</div>'."""
    depth = 0
    i = div_start
    while i < len(html):
        next_open = html.find('<div', i)
        next_close = html.find('</div>', i)
        if next_close == -1:
            return len(html)
        if next_open != -1 and next_open < next_close:
            depth += 1
            i = next_open + 4
        else:
            depth -= 1
            i = next_close + 6
            if depth == 0:
                return i
    return len(html)


def locate_div(html, search_str):
    """Find search_str, return (div_pos, div_end) for the <div> at/after that position."""
    pos = html.find(search_str)
    if pos == -1:
        return -1, -1
    div_pos = html.find('<div', pos)
    if div_pos == -1:
        return -1, -1
    return div_pos, find_div_end(html, div_pos)


changed = 0

for fname in QUIZ_FILES:
    fpath = os.path.join(BASE, fname)
    content = open(fpath, encoding='utf-8').read()
    original = content

    # ── 1. Fix remaining ad-banners ────────────────────────────────────
    content = content.replace(
        '<div class="ad-banner">Advertisement — Google AdSense</div>',
        '<!-- AdSense banner placeholder -->'
    )

    # ── 2. Locate the blocks to move (using div class, works for all templates) ─
    # score-box
    sb_pos, sb_end = locate_div(content, '<div class="score-box">')
    # topic-progress-panel
    tpp_pos, tpp_end = locate_div(content, '<div class="topic-progress-panel"')
    # mock-launch-bar
    mlb_pos, mlb_end = locate_div(content, '<div class="mock-launch-bar"')

    # Determine which blocks we have and their combined region
    if tpp_pos == -1 or mlb_end == -1:
        print(f'  SKIP {fname}: tpp/mlb not found')
        content = original
        continue

    # region_start: start of first block in the group (could be score-box or tpp)
    if sb_pos != -1 and sb_pos < tpp_pos:
        region_start = sb_pos
    else:
        region_start = tpp_pos  # 442a: no score-box

    region_end = mlb_end

    # Verify region is sensible (all blocks within first ~500 chars of each other)
    if tpp_pos > region_start + 2000:
        print(f'  SKIP {fname}: blocks too far apart (unexpected structure)')
        content = original
        continue

    # Extract the combined region text (will be reinserted after question-card)
    combined = content[region_start:region_end]

    # Remove the region (also strip any leading whitespace on the same line)
    remove_start = region_start
    while remove_start > 0 and content[remove_start - 1] in ' \t':
        remove_start -= 1
    if remove_start > 0 and content[remove_start - 1] == '\n':
        remove_start -= 1  # include the preceding newline in removal

    remove_end = region_end
    if remove_end < len(content) and content[remove_end] == '\n':
        remove_end += 1  # consume trailing newline

    content = content[:remove_start] + '\n' + content[remove_end:]

    # ── 3. Change Download Study Sheet → Coming Soon ───────────────────
    content = re.sub(
        r'<button[^>]*onclick="downloadStudySheet\(\)"[^>]*>[^<]*Download Study Sheet \(PDF\)</button>',
        '<button disabled style="background:#95a5a6;color:#fff;border:none;border-radius:8px;'
        'padding:9px 18px;font-size:.82rem;font-weight:700;cursor:not-allowed;'
        'display:inline-flex;align-items:center;gap:6px">📄 Study Sheet — Coming Soon</button>',
        content
    )

    # ── 4. Insert blocks after question-card ───────────────────────────
    qcard_m = re.search(r'<div class="question-card"', content)
    if not qcard_m:
        print(f'  SKIP {fname}: question-card not found')
        content = original
        continue

    qcard_end = find_div_end(content, qcard_m.start())

    # Normalize indentation: strip leading/trailing blank lines from combined
    insertion = '\n' + combined.strip('\n') + '\n'
    content = content[:qcard_end] + insertion + content[qcard_end:]

    # ── 5. Write if changed ─────────────────────────────────────────────
    if content != original:
        open(fpath, 'w', encoding='utf-8').write(content)
        changed += 1
        print(f'  Updated: {fname}')
    else:
        print(f'  No change: {fname}')

print(f'\nDone. {changed}/{len(QUIZ_FILES)} files updated.')
