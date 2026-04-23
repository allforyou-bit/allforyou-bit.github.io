"""Find odd backtick in 447a and 313a — read-only diagnosis."""
import re, sys
from pathlib import Path

def safe_print(text):
    sys.stdout.buffer.write((str(text) + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()

for code in ['447a', '313a']:
    safe_print(f'\n{"="*60}')
    safe_print(f'FILE: {code}.html')
    safe_print('='*60)

    txt = Path(f'{code}.html').read_text(encoding='utf-8')
    lines = txt.split('\n')
    total_bt = txt.count('`')
    safe_print(f'Total backticks: {total_bt} ({"ODD" if total_bt%2==1 else "EVEN"})')

    # List ALL lines containing backtick
    bt_lines = [(i+1, line) for i, line in enumerate(lines) if '`' in line]
    safe_print(f'Lines with backtick: {len(bt_lines)}')
    for lnum, line in bt_lines:
        safe_print(f'  L{lnum}: {line.strip()[:140]}')

    # Check </script> occurrences
    safe_print(f'\n</script> occurrences:')
    for i, line in enumerate(lines, 1):
        if '</script>' in line.lower():
            safe_print(f'  L{i}: {line.strip()[:120]}')

    # Check for backtick inside questions array (explanation/keyConcept/text)
    safe_print(f'\nBackticks inside questions data:')
    arr_start = re.search(r'const questions\s*=\s*\[', txt)
    if arr_start:
        arr_section = txt[arr_start.start():]
        arr_lines = arr_section.split('\n')
        for i, line in enumerate(arr_lines, 1):
            if '`' in line:
                abs_line = txt[:arr_start.start()].count('\n') + i
                safe_print(f'  L~{abs_line}: {line.strip()[:140]}')

    # Look for downloadStudySheet or window.open
    has_wo = 'const w = window.open' in txt
    safe_print(f'\nHas downloadStudySheet/window.open: {has_wo}')

    # Count backticks in first half vs second half to find imbalance
    half = len(txt) // 2
    first_half_bt = txt[:half].count('`')
    second_half_bt = txt[half:].count('`')
    safe_print(f'Backticks first half: {first_half_bt}, second half: {second_half_bt}')

    # Find the single unmatched backtick by scanning pairs
    # Simulate a simple state machine (not JS-parser-accurate but helps locate)
    in_string = False
    in_single = False
    in_double = False
    depth = 0
    last_backtick_line = None
    for i, line in enumerate(lines, 1):
        for ch in line:
            if ch == '`' and not in_single and not in_double:
                in_string = not in_string
                last_backtick_line = i
            elif ch == "'" and not in_string and not in_double:
                in_single = not in_single
            elif ch == '"' and not in_string and not in_single:
                in_double = not in_double
        # Newline resets single/double quote state (simplified)
        in_single = False
        in_double = False

    safe_print(f'State-machine result: in_template_literal at EOF = {in_string}')
    safe_print(f'Last backtick seen at line: {last_backtick_line}')
