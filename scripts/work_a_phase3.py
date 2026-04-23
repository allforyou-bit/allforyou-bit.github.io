"""Work A Phase 3 — batch apply styles.css link + nav dropdown update to 70 HTML files."""
import re, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

def safe_print(t):
    sys.stdout.buffer.write((str(t) + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()

# Active trade link per file (quiz pages only)
QUIZ_ACTIVE = {
    '276a.html': '/276a.html',
    '306a.html': '/306a.html',
    '308a.html': '/308a.html',
    '309a.html': '/309a.html',
    '310s.html': '/310s.html',
    '310t.html': '/310t.html',
    '313a.html': '/313a.html',
    '403a.html': '/403a.html',
    '442a.html': '/442a.html',
    '447a.html': '/447a.html',
}

TRADES = [
    ('/276a.html', '276A Welder'),
    ('/306a.html', '306A Sheet Metal Worker'),
    ('/308a.html', '308A HVAC/Refrigeration'),
    ('/309a.html', '309A Construction Electrician'),
    ('/310s.html', '310S Automotive Service Tech'),
    ('/310t.html', '310T Truck &amp; Transport Mechanic'),
    ('/313a.html', '313A Industrial Electrician'),
    ('/403a.html', '403A Gas Fitter (Class A)'),
    ('/421a.html', '421A Heavy Equipment Tech'),
    ('/442a.html', '442A Ironworker'),
    ('/447a.html', '447A Plumber'),
]

SKIP = {'421a.html', '404.html'}

# Build new dropdown HTML for a given file
def build_dropdown(fname):
    active_href = QUIZ_ACTIVE.get(fname)
    links = []
    for href, label in TRADES:
        if active_href and href == active_href:
            links.append(f'        <a href="{href}" class="active">{label}</a>')
        else:
            links.append(f'        <a href="{href}">{label}</a>')
    menu = '\n'.join(links)
    return (
        '      <button class="nav-drop-btn" id="tradesBtn" aria-haspopup="true">Trades ▾</button>\n'
        '      <div class="nav-drop-menu">\n'
        f'{menu}\n'
        '      </div>'
    )

# Regex: matches the entire trades dropdown button + menu block
# Handles both literal ▾ and HTML entity &#x25BE;
DROP_PAT = re.compile(
    r'<button class="nav-drop-btn" id="tradesBtn"[^>]*>Trades (?:▾|&#x25BE;)</button>\s*'
    r'<div class="nav-drop-menu">.*?</div>',
    re.DOTALL
)

LINK_TAG = '<link rel="stylesheet" href="/styles.css">'

modified = []
skipped = []
errors = []

html_files = sorted(BASE.glob('*.html'))
for path in html_files:
    fname = path.name
    if fname in SKIP:
        continue

    src = path.read_text(encoding='utf-8')
    orig = src

    # 1. Add styles.css link if not present
    if LINK_TAG not in src:
        # Insert before </head>
        if '</head>' in src:
            src = src.replace('</head>', f'{LINK_TAG}\n</head>', 1)
        else:
            safe_print(f'  WARN: {fname} — no </head> found, skipping link insert')

    # 2. Replace dropdown block
    matches = DROP_PAT.findall(src)
    if not matches:
        safe_print(f'  WARN: {fname} — no dropdown pattern found')
        skipped.append(fname)
        continue

    replacement = build_dropdown(fname)
    src, count = DROP_PAT.subn(replacement, src, count=1)
    if count != 1:
        safe_print(f'  ERROR: {fname} — unexpected replacement count {count}')
        errors.append(fname)
        continue

    if src != orig:
        path.write_text(src, encoding='utf-8')
        modified.append(fname)
        safe_print(f'  OK: {fname}')
    else:
        safe_print(f'  UNCHANGED: {fname}')

safe_print(f'\n=== DONE ===')
safe_print(f'Modified: {len(modified)} files')
safe_print(f'Skipped (no dropdown): {skipped}')
safe_print(f'Errors: {errors}')
