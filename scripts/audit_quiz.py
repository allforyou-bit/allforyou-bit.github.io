"""
Quiz Quality Audit Script — parses questions[] array from HTML files.
Usage: python scripts/audit_quiz.py 421a 310t 309a
"""
import re, sys, json
from pathlib import Path
from collections import Counter

def safe_print(text):
    sys.stdout.buffer.write((str(text) + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()

def extract_all_question_blocks(html_text):
    """
    Extract each question object by finding {id:N,...} blocks.
    Handles JS single-line comments (// ...) between objects.
    """
    # Find start of questions array
    start_m = re.search(r'const questions\s*=\s*\[', html_text)
    if not start_m:
        return None, "Cannot find 'const questions = ['"

    array_text = html_text[start_m.end():]

    # Remove single-line JS comments (// ...) to handle section headers
    array_text = re.sub(r'//[^\n]*\n', '\n', array_text)

    # Split on ,{ where { is followed (possibly with whitespace) by id:
    parts = re.split(r',\s*\{(?=[\s\S]{0,30}?id\s*:)', array_text)

    blocks = []
    for i, part in enumerate(parts):
        if i == 0:
            block = part.lstrip()
            if block.startswith('{'):
                blocks.append(block)
        else:
            blocks.append('{' + part)

    return blocks, None

def parse_block(block):
    """Parse a single question block into a dict of fields."""
    q = {}

    # id
    id_m = re.search(r'\bid\s*:\s*(\d+)', block)
    q['id'] = int(id_m.group(1)) if id_m else -1

    # topic
    topic_m = re.search(r"(?:^|,|\{)\s*topic\s*:\s*['\"]([^'\"]+)['\"]", block)
    q['topic'] = topic_m.group(1) if topic_m else ''

    # diff
    diff_m = re.search(r"(?:^|,|\{)\s*diff\s*:\s*['\"]([^'\"]+)['\"]", block)
    q['diff'] = diff_m.group(1) if diff_m else ''

    # answer
    ans_m = re.search(r'\banswer\s*:\s*(\d+)', block)
    q['answer'] = int(ans_m.group(1)) if ans_m else -1

    # options count (count items in options:[...] array)
    options_block = re.search(r'options\s*:\s*\[([^\]]+)\]', block, re.DOTALL)
    if options_block:
        opts_text = options_block.group(1)
        # Count string literals (single or double quoted)
        opt_items = re.findall(r"(?:^|,)\s*['\"]", opts_text)
        q['options_count'] = len(opt_items) if len(opt_items) > 0 else 4
    else:
        q['options_count'] = 4  # assume 4

    # text field
    text_m = re.search(r"\btext\s*:\s*'((?:[^'\\]|\\.)*)'", block, re.DOTALL)
    if not text_m:
        text_m = re.search(r'\btext\s*:\s*"((?:[^"\\]|\\.)*)"', block, re.DOTALL)
    q['text'] = text_m.group(1)[:120].strip() if text_m else ''

    # explanation
    exp_m = re.search(r"\bexplanation\s*:\s*'((?:[^'\\]|\\.)*)'", block, re.DOTALL)
    if not exp_m:
        exp_m = re.search(r'\bexplanation\s*:\s*"((?:[^"\\]|\\.)*)"', block, re.DOTALL)
    q['explanation'] = exp_m.group(1).strip() if exp_m else ''

    return q

def classify_question_type(text):
    """Heuristic: applied/scenario vs recall/memorization."""
    scenario_keywords = [
        'technician', 'worker', 'mechanic', 'you are', 'a customer', 'a vehicle',
        'discovers', 'finds', 'notices', 'complains', 'during', 'while', 'after',
        'what should', 'next step', 'first step', 'correct action', 'which action',
        'most likely', 'probable cause', 'diagnose', 'troubleshoot', 'inspect',
        'measured', 'reading', 'test result', 'indicates', 'excessive', 'abnormal',
        'shop', 'job site', 'contractor', 'apprentice', 'journeyman', 'foreman',
        'is found', 'is observed', 'has been', 'should be done', 'must be done',
        'what is the correct', 'what is the first', 'what is the most',
        'a sheet metal', 'a welder', 'a plumber', 'an electrician', 'a gas fitter',
        'a truck', 'an engine', 'a circuit', 'a system', 'a duct', 'a fitting',
        'when installing', 'when welding', 'when cutting', 'when testing',
        'before', 'immediately', 'if a', 'if the', 'when a', 'when the',
        'is being', 'are being', 'has failed', 'is leaking', 'is overheating',
    ]
    text_lower = (text or '').lower()
    count = sum(1 for kw in scenario_keywords if kw in text_lower)
    return 'applied' if count >= 1 else 'recall'

def count_explanation_sentences(expl):
    if not expl:
        return 0
    sentences = re.split(r'(?<=[.!?])\s+', expl.strip())
    return len([s for s in sentences if len(s.strip()) > 5])

def audit_quiz(code):
    filepath = Path(f'{code}.html')
    if not filepath.exists():
        return {'code': code, 'error': f'File not found: {code}.html'}

    html_text = filepath.read_text(encoding='utf-8')

    blocks, err = extract_all_question_blocks(html_text)
    if err:
        return {'code': code, 'error': err}

    questions = []
    for block in blocks:
        if re.search(r'\bid\s*:\s*\d+', block):
            q = parse_block(block)
            if q['id'] > 0:
                questions.append(q)

    if not questions:
        return {'code': code, 'error': 'No questions parsed from blocks'}

    total = len(questions)
    ids = [q['id'] for q in questions]

    # --- Analysis ---

    # Duplicate IDs
    id_counts = Counter(ids)
    dup_ids = [(id_, cnt) for id_, cnt in id_counts.items() if cnt > 1]

    # Answer out of range
    answer_errors = [q['id'] for q in questions if q['answer'] < 0 or q['answer'] > 3]
    answer_suspect = [q['id'] for q in questions
                      if q['options_count'] > 1 and q['answer'] >= q['options_count']]

    # Explanation missing
    no_explanation = [q['id'] for q in questions if not q['explanation']]

    # Explanation short (< 2 sentences)
    short_explanation = [q['id'] for q in questions
                         if q['explanation'] and count_explanation_sentences(q['explanation']) < 2]

    # Applied vs recall
    applied_count = sum(1 for q in questions if classify_question_type(q['text']) == 'applied')
    applied_pct = round(applied_count / total * 100) if total else 0

    # Topic distribution
    topic_counts = Counter(q['topic'] for q in questions)

    # Difficulty distribution
    diff_counts = Counter(q['diff'] for q in questions)

    # Duplicate texts (use 60 chars, skip empty)
    text_map = {}
    for q in questions:
        snippet = q['text'][:60].lower().strip()
        if len(snippet) > 10:  # skip very short / empty
            if snippet not in text_map:
                text_map[snippet] = []
            text_map[snippet].append(q['id'])
    dup_text_ids = [ids_list for ids_list in text_map.values() if len(ids_list) > 1]

    # UX features
    ux_difficulty = bool(re.search(r'diffTag|data-diff|difficulty', html_text, re.I))
    ux_wrongbank = bool(re.search(r'wrongBank', html_text))
    ux_progress = bool(re.search(r'saveProgress|progress_[a-z0-9]', html_text))

    return {
        'code': code,
        'total': total,
        'applied_pct': applied_pct,
        'recall_pct': 100 - applied_pct,
        'no_explanation': no_explanation,
        'short_explanation': short_explanation,
        'answer_errors': answer_errors,
        'answer_suspect': answer_suspect,
        'dup_ids': dup_ids,
        'dup_text_ids': dup_text_ids,
        'topic_counts': dict(topic_counts),
        'diff_counts': dict(diff_counts),
        'ux_difficulty': ux_difficulty,
        'ux_wrongbank': ux_wrongbank,
        'ux_progress': ux_progress,
        'ids_range': f'{min(ids)}-{max(ids)}' if ids else 'N/A',
        'error': None
    }

def format_report(r):
    if r.get('error'):
        return f"퀴즈: {r['code']}\n  ERROR: {r['error']}"

    lines = [f"퀴즈: {r['code'].upper()}"]
    lines.append(f"  총 문제: {r['total']} (ID: {r['ids_range']})")
    lines.append(f"  적용형/암기 비율: {r['applied_pct']}% / {r['recall_pct']}%")

    no_exp = r['no_explanation']
    lines.append(f"  explanation 누락: {len(no_exp)}개{(' (ID: ' + str(no_exp[:8]) + ')') if no_exp else ''}")

    short_exp = r['short_explanation']
    lines.append(f"  explanation 2문장 미만: {len(short_exp)}개{(' (ID: ' + str(short_exp[:8]) + ')') if short_exp else ''}")

    ans_err = r['answer_errors']
    lines.append(f"  정답 인덱스 범위 외(0~3): {len(ans_err)}개{(' (ID: ' + str(ans_err[:5]) + ')') if ans_err else ''}")

    ans_sus = r['answer_suspect']
    lines.append(f"  정답 인덱스 의심: {len(ans_sus)}개{(' (ID: ' + str(ans_sus[:5]) + ')') if ans_sus else ''}")

    dup_ids = r['dup_ids']
    lines.append(f"  ID 중복: {len(dup_ids)}개{(' ' + str(dup_ids[:3])) if dup_ids else ''}")

    dup_txt = r['dup_text_ids']
    lines.append(f"  텍스트 중복 의심: {len(dup_txt)}쌍{(' ' + str(dup_txt[:3])) if dup_txt else ''}")

    tc = r['topic_counts']
    total = r['total']
    topic_str = ', '.join(f"{k}:{v}({round(v/total*100)}%)" for k, v in sorted(tc.items(), key=lambda x: -x[1]))
    lines.append(f"  토픽 분포: {topic_str}")

    dc = r['diff_counts']
    diff_str = ', '.join(f"{k}:{v}" for k, v in sorted(dc.items()))
    lines.append(f"  난이도 분포: {diff_str}")

    lines.append(f"  UX: 난이도표시[{'O' if r['ux_difficulty'] else 'X'}] 오답노트[{'O' if r['ux_wrongbank'] else 'X'}] 진행저장[{'O' if r['ux_progress'] else 'X'}]")

    priority = []
    if r['answer_errors']: priority.append(f"정답 인덱스 오류 즉시 수정 (ID: {r['answer_errors'][:10]})")
    if r['no_explanation']: priority.append(f"explanation 누락 (ID: {r['no_explanation'][:10]})")
    if r['dup_ids']: priority.append(f"ID 중복 제거 {r['dup_ids'][:3]}")
    if dup_txt: priority.append(f"중복 텍스트 확인 필요 ({len(dup_txt)}쌍)")
    if r['applied_pct'] < 40: priority.append(f"적용형 비중 부족 ({r['applied_pct']}%)")
    if not priority: priority.append("없음")
    lines.append(f"  우선 수정: " + " / ".join(priority))

    return '\n'.join(lines)

if __name__ == '__main__':
    codes = sys.argv[1:] if len(sys.argv) > 1 else []
    results = []
    for code in codes:
        safe_print(f"Auditing {code}...")
        r = audit_quiz(code)
        results.append(r)
        safe_print(format_report(r))
        safe_print('')

    # Save JSON
    json_path = Path('scripts/audit_results.json')
    existing = json.loads(json_path.read_text(encoding='utf-8')) if json_path.exists() else []
    existing = [e for e in existing if e.get('code') not in codes]
    existing.extend(results)
    json_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding='utf-8')
    safe_print(f"Results saved to {json_path}")
