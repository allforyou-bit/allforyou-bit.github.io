#!/usr/bin/env python3
"""
Red Seal Project — Telegram 알림 스크립트
사용법 (CLI):
  python scripts/notify_telegram.py "작업명" "file1.html,file2.html" "커밋해시" "다음할일"

모듈로 임포트:
  from scripts.notify_telegram import notify
  notify("작업명", files=["a.html","b.html"], commit="abc123", next_steps="...")
"""

import sys, os, urllib.request, urllib.parse, json
from pathlib import Path

BASE_DIR  = Path(__file__).resolve().parent.parent
SECRETS   = BASE_DIR / "secrets.txt"
CHAT_ID   = "7836949810"
MAX_CHARS = 4096


# ─── 토큰 로드 ────────────────────────────────────────────────────────────────

def _load_token() -> str:
    # 1순위: 환경 변수
    token = os.environ.get("REDSEAL_BOT_TOKEN", "")
    if token:
        return token

    # 2순위: secrets.txt
    if SECRETS.exists():
        for line in SECRETS.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("REDSEAL_BOT_TOKEN="):
                token = line.split("=", 1)[1].strip()
                if token:
                    return token

    sys.stdout.buffer.write(b"[ERROR] REDSEAL_BOT_TOKEN not found. Add to secrets.txt\n")
    sys.exit(1)


# ─── 전송 ─────────────────────────────────────────────────────────────────────

def _send(token: str, text: str) -> None:
    """4096자 초과 시 자동 분할 전송 (HTML parse_mode)"""
    chunks = [text[i:i + MAX_CHARS] for i in range(0, len(text), MAX_CHARS)]
    for chunk in chunks:
        payload = urllib.parse.urlencode({
            "chat_id":    CHAT_ID,
            "text":       chunk,
            "parse_mode": "HTML",
        }).encode()
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=payload,
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                result = json.load(resp)
                if not result.get("ok"):
                    msg = f"[Telegram ERROR] {result.get('description', result)}\n"
                    sys.stdout.buffer.write(msg.encode("utf-8"))
                    sys.exit(1)
        except urllib.error.URLError as e:
            sys.stdout.buffer.write(f"[Telegram FAIL] network error: {e}\n".encode("utf-8"))
            sys.exit(1)


# ─── 메시지 조합 ──────────────────────────────────────────────────────────────

def notify(
    task_name:  str,
    files:      list | str | None = None,
    commit:     str | None = None,
    next_steps: str | None = None,
    extra:      str | None = None,
) -> None:
    """
    Telegram으로 작업 완료 알림 전송.

    Parameters
    ----------
    task_name  : 작업 이름 (예: "Organization Schema 추가")
    files      : 수정 파일 목록 (리스트 또는 쉼표 구분 문자열)
    commit     : 커밋 해시 (짧은 형식 권장)
    next_steps : Kay가 해야 할 다음 작업
    extra      : 추가 메모 (선택)
    """
    token = _load_token()
    lines = [f"✅ {task_name}", ""]

    # 수정 파일
    if files:
        file_list = files if isinstance(files, list) else [f.strip() for f in files.split(",")]
        lines.append("수정 파일:")
        for f in file_list:
            lines.append(f"  · {f}")
        lines.append("")

    # 커밋
    if commit:
        lines.append(f"커밋: <code>{commit}</code>")

    # 다음 단계
    if next_steps:
        lines.append(f"다음 단계: {next_steps}")

    # 추가 메모
    if extra:
        lines.append(f"\n{extra}")

    message = "\n".join(lines)
    _send(token, message)
    sys.stdout.buffer.write(f"[Telegram] OK — {task_name}\n".encode("utf-8"))


# ─── CLI ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.stdout.buffer.write(b"Usage: python scripts/notify_telegram.py <task> [files] [commit] [next_steps]\n")
        sys.exit(1)

    notify(
        task_name  = args[0],
        files      = args[1] if len(args) > 1 else None,
        commit     = args[2] if len(args) > 2 else None,
        next_steps = args[3] if len(args) > 3 else None,
    )
