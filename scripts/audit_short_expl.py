"""Print 1-sentence explanations for a quiz, with question text, for manual review."""
import re, sys
from pathlib import Path

def safe_print(text):
    sys.stdout.buffer.write((str(text) + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()

def count_sentences(text):
    if not text: return 0
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return len([p for p in parts if len(p.strip()) > 5])

def get_short_expl_questions(code):
    txt = Path(f'{code}.html').read_text(encoding='utf-8')
    arr_start = re.search(r'const questions\s*=\s*\[', txt).end()
    arr_text = txt[arr_start:]
    arr_clean = re.sub(r'//[^\n]*\n', '\n', arr_text)
    parts = re.split(r',\s*\{(?=[\s\S]{0,30}?id\s*:)', arr_clean)

    results = []
    for p in parts:
        m = re.search(r'\bid\s*:\s*(\d+)', p)
        if not m: continue
        qid = int(m.group(1))

        exp_m = re.search(r"explanation\s*:\s*'([^']+)'", p, re.DOTALL)
        expl = exp_m.group(1) if exp_m else ''
        # Strip HTML tags for sentence counting
        expl_plain = re.sub(r'<[^>]+>', ' ', expl).strip()

        if count_sentences(expl_plain) < 2:
            text_m = re.search(r"text\s*:\s*'([^']+)'", p, re.DOTALL)
            qtext = text_m.group(1)[:100] if text_m else ''
            topic_m = re.search(r"topic\s*:\s*'([^']+)'", p)
            topic = topic_m.group(1) if topic_m else ''
            results.append({'id': qid, 'topic': topic, 'text': qtext, 'expl': expl_plain[:200]})
    return results

code = sys.argv[1] if len(sys.argv) > 1 else '442a'
items = get_short_expl_questions(code)
safe_print(f'{code.upper()}: {len(items)} short-explanation questions')
safe_print('=' * 60)
for q in items:
    safe_print(f"Q{q['id']} [{q['topic']}]")
    safe_print(f"  Q: {q['text'][:90]}")
    safe_print(f"  E: {q['expl'][:180]}")
    safe_print('')
