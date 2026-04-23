import re, sys

def safe_print(b):
    sys.stdout.buffer.write(b if isinstance(b, bytes) else b.encode('utf-8', 'replace'))
    sys.stdout.buffer.write(b'\n')
    sys.stdout.buffer.flush()

txt = open('308a.html', encoding='utf-8').read()
arr_start = re.search(r'const questions\s*=\s*\[', txt).end()
arr_text = txt[arr_start:]
arr_clean = re.sub(r'//[^\n]*\n', '\n', arr_text)
parts = re.split(r',\s*\{(?=[\s\S]{0,30}?id\s*:)', arr_clean)

q_map = {}
for p in parts:
    m = re.search(r'\bid\s*:\s*(\d+)', p)
    if m:
        qid = int(m.group(1))
        if qid in (78, 103):
            text_m = re.search(r"text\s*:\s*'([^']+)'", p, re.DOTALL)
            opts_m = re.search(r'options\s*:\s*\[([^\]]+)\]', p, re.DOTALL)
            ans_m = re.search(r'\banswer\s*:\s*(\d+)', p)
            exp_m = re.search(r"explanation\s*:\s*'([^']+)'", p, re.DOTALL)
            q_map[qid] = {
                'text': text_m.group(1) if text_m else 'FAIL',
                'options': opts_m.group(1) if opts_m else 'FAIL',
                'answer': ans_m.group(1) if ans_m else '?',
                'explanation': exp_m.group(1) if exp_m else 'FAIL'
            }

for qid in [78, 103]:
    q = q_map.get(qid, {})
    safe_print(f'=== Q{qid} ===')
    safe_print(f"text: {q.get('text','?')[:150]}")
    safe_print(f"answer: {q.get('answer','?')}")
    safe_print(f"explanation: {q.get('explanation','?')[:250]}")
    safe_print('')

# Check if identical
if 78 in q_map and 103 in q_map:
    same_text = q_map[78]['text'] == q_map[103]['text']
    same_ans  = q_map[78]['answer'] == q_map[103]['answer']
    same_opts = q_map[78]['options'].strip() == q_map[103]['options'].strip()
    safe_print(f'text identical: {same_text}')
    safe_print(f'answer identical: {same_ans}')
    safe_print(f'options identical: {same_opts}')
