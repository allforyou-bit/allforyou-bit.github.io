"""Diagnostic: find backtick and </script> issues in quiz HTML files. READ ONLY."""
import re, sys
from pathlib import Path

def safe_print(text):
    sys.stdout.buffer.write((str(text) + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()

QUIZ_FILES = ['421a','310t','309a','310s','308a','276a','447a','313a','442a','403a','306a']

# ── STEP 1: 421a.html backtick + window.open location ──
safe_print('=== STEP 1: 421a.html key locations ===')
txt421 = Path('421a.html').read_text(encoding='utf-8')
lines421 = txt421.split('\n')
for i, line in enumerate(lines421, 1):
    if 'const w = window.open' in line:
        safe_print(f'  window.open line: {i}')

# ── STEP 2: backtick count (all quizzes) ──
safe_print('\n=== STEP 2: backtick count per file ===')
odd_files = []
for code in QUIZ_FILES:
    path = Path(f'{code}.html')
    if not path.exists():
        safe_print(f'  {code}.html: NOT FOUND')
        continue
    content = path.read_text(encoding='utf-8')
    cnt = content.count('`')
    status = 'ODD=BROKEN?' if cnt % 2 == 1 else 'even'
    safe_print(f'  {code}.html: backticks={cnt} ({status})')
    if cnt % 2 == 1:
        odd_files.append(code)

safe_print(f'\n  Files with ODD backtick count: {odd_files if odd_files else "none"}')

# ── STEP 3: backtick line locations in 421a ──
safe_print('\n=== STEP 3: backtick lines in 421a.html (first 40) ===')
backtick_lines = [(i+1, line.strip()[:120]) for i, line in enumerate(lines421) if '`' in line]
for lnum, content in backtick_lines[:40]:
    safe_print(f'  L{lnum}: {content}')
safe_print(f'  Total backtick lines: {len(backtick_lines)}')

# ── STEP 4: backticks inside explanation/text fields ──
safe_print('\n=== STEP 4: backticks inside question data fields in 421a ===')
# Find explanation fields containing backtick
arr_start = re.search(r'const questions\s*=\s*\[', txt421)
if arr_start:
    arr_section = txt421[arr_start.start():]
    # Find lines with backtick inside explanation or text value
    for i, line in enumerate(arr_section.split('\n'), 1):
        if '`' in line and ('explanation' in line or 'text:' in line or 'keyConcept' in line or 'options' in line):
            # Approximate absolute line number
            abs_line = txt421[:arr_start.start()].count('\n') + i
            safe_print(f'  L~{abs_line}: {line.strip()[:150]}')

# ── STEP 5: </script> tag occurrences ──
safe_print('\n=== STEP 5: </script> occurrences in 421a.html ===')
for i, line in enumerate(lines421, 1):
    if '</script>' in line.lower():
        safe_print(f'  L{i}: {line.strip()[:120]}')

# Check for escaped version
esc_count = txt421.count('<\\/script>')
safe_print(f'\n  Escaped <\\/script> occurrences: {esc_count}')

# ── STEP 6: window.open in all HTML files ──
safe_print('\n=== STEP 6: files containing "const w = window.open" ===')
all_html = list(Path('.').glob('*.html'))
wo_files = []
for p in sorted(all_html):
    try:
        c = p.read_text(encoding='utf-8')
        if 'const w = window.open' in c:
            wo_files.append(p.name)
    except:
        pass
for f in wo_files:
    safe_print(f'  {f}')
safe_print(f'  Total: {len(wo_files)} files')

# ── STEP 7: Context around the break point in 421a ──
safe_print('\n=== STEP 7: 421a.html context around L2840-2850 ===')
for i, line in enumerate(lines421[2835:2855], start=2836):
    safe_print(f'  L{i}: {line[:120]}')

# ── STEP 8: Find where questions array ends and JS engine begins ──
safe_print('\n=== STEP 8: transition from questions[] to JS engine in 421a ===')
# Look for ]; which closes the questions array
for i, line in enumerate(lines421, 1):
    stripped = line.strip()
    if stripped in ('];', '] ;') or stripped.startswith('];'):
        safe_print(f'  L{i} (potential array close): {line[:80]}')
    if 'const MOCK_PAGE_KEY' in line:
        safe_print(f'  L{i} MOCK_PAGE_KEY: {line[:80]}')
