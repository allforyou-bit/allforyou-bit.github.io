#!/usr/bin/env python3
"""
Red Seal Project — Telegram 알림 스크립트

신규 함수 (새 작업에서 사용):
  from scripts.notify_telegram import send_telegram
  send_telegram(
      title="✅ 작업명",
      scope="7/71 파일",
      changes=["변경 1", "변경 2"],
      validation="치환 18개 / 예상 18개 (일치)",
      warnings="없음",
      files=["421a.html", "308a.html"],
      commit="abc1234",
      push_status="완료",
      next_step="Kay 모바일 재확인",
      kay_check=["421a.html 스크롤 확인", "기사 페이지 정상 여부"],
  )

레거시 함수 (기존 호출 코드용, 새 작업 사용 금지):
  from scripts.notify_telegram import notify
  notify("작업명", files="a.html,b.html", commit="abc123", next_steps="...")

CLI (레거시):
  python scripts/notify_telegram.py "작업명" "file1.html,file2.html" "커밋해시" "다음할일"
"""

import sys, os, urllib.request, urllib.parse, json
from pathlib import Path

BASE_DIR  = Path(__file__).resolve().parent.parent
SECRETS   = BASE_DIR / "secrets.txt"
CHAT_ID   = "7836949810"
MAX_CHARS = 4096
DIVIDER   = "\u2501" * 18  # ━━━━━━━━━━━━━━━━━━


# ─── 토큰 로드 ────────────────────────────────────────────────────────────────

def _load_token() -> str:
    token = os.environ.get("REDSEAL_BOT_TOKEN", "")
    if token:
        return token
    if SECRETS.exists():
        for line in SECRETS.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("REDSEAL_BOT_TOKEN="):
                token = line.split("=", 1)[1].strip()
                if token:
                    return token
    sys.stdout.buffer.write(b"[ERROR] REDSEAL_BOT_TOKEN not found. Add to secrets.txt\n")
    sys.exit(1)


# ─── 전송 (분할 지원) ─────────────────────────────────────────────────────────

def _send(token: str, text: str) -> None:
    """4096자 초과 시 [1/N], [2/N] 표시 후 분할 전송."""
    if len(text) <= MAX_CHARS:
        chunks = [text]
    else:
        # 분할: 4000자씩 (헤더 공간 확보)
        size = 3900
        raw_chunks = [text[i:i + size] for i in range(0, len(text), size)]
        n = len(raw_chunks)
        chunks = [f"[{i+1}/{n}]\n{c}" for i, c in enumerate(raw_chunks)]

    for chunk in chunks:
        payload = json.dumps({
            "chat_id":    CHAT_ID,
            "text":       chunk,
            "parse_mode": "HTML",
        }).encode("utf-8")
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=payload,
            headers={"Content-Type": "application/json"},
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


# ─── 신규 구조화 함수 ─────────────────────────────────────────────────────────

def send_telegram(
    title:       str,
    scope:       str,
    changes:     list,
    validation:  str,
    warnings:    str,
    files:       list,
    commit:      str,
    push_status: str,
    next_step:   str,
    kay_check:   list = None,
) -> None:
    """
    구조화된 작업 완료 보고를 Telegram으로 전송.

    Parameters
    ----------
    title       : 제목 (이모지 허용, 예: "✅ </script> 이스케이프 전수 수정 완료")
    scope       : 작업 범위 (예: "7/71 파일")
    changes     : 변경 내용 bullet 리스트 (3~5개)
    validation  : 검증 결과 문자열 (예: "치환 18개 / 예상 18개 (일치)")
    warnings    : 경고/의심 사항 (없으면 "없음")
    files       : 수정 파일 목록 (리스트)
    commit      : 커밋 해시
    push_status : push 상태 (예: "완료" / "실패")
    next_step   : 다음 단계 자유 텍스트
    kay_check   : Kay 확인 요청 사항 리스트 (없으면 None 또는 빈 리스트)
    """
    token = _load_token()

    lines = [
        DIVIDER,
        title,
        DIVIDER,
        f"\U0001f4ca 작업 범위: {scope}",
        "\U0001f4dd 변경 내용:",
    ]
    for bullet in changes:
        lines.append(f"  \u00b7 {bullet}")

    lines.append(f"\U0001f50d 검증 결과: {validation}")
    lines.append(f"\u26a0\ufe0f 경고: {warnings}")
    lines.append("")

    file_count = len(files) if files else 0
    lines.append(f"\U0001f4c1 수정 파일 ({file_count}):")
    for f in (files or []):
        lines.append(f"  \u00b7 {f}")

    lines.append("")
    lines.append(f"\U0001f516 commit: <code>{commit}</code>")
    lines.append(f"\U0001f680 push: {push_status}")
    lines.append(f"\u27a1\ufe0f 다음 단계: {next_step}")

    if kay_check:
        lines.append(f"\U0001f464 Kay 확인 요청:")
        for item in kay_check:
            lines.append(f"  \u00b7 {item}")

    lines.append(DIVIDER)

    message = "\n".join(lines)
    _send(token, message)
    sys.stdout.buffer.write(f"[Telegram] OK — {title}\n".encode("utf-8"))


# ─── 레거시 함수 (기존 호출 코드용, 새 작업 사용 금지) ───────────────────────

def notify(
    task_name:  str,
    files:      "list | str | None" = None,
    commit:     str = None,
    next_steps: str = None,
    extra:      str = None,
) -> None:
    """레거시: 기존 3필드 포맷. 새 작업에서는 send_telegram() 사용."""
    token = _load_token()
    lines = [f"\u2705 {task_name}", ""]

    if files:
        file_list = files if isinstance(files, list) else [f.strip() for f in files.split(",")]
        lines.append("수정 파일:")
        for f in file_list:
            lines.append(f"  \u00b7 {f}")
        lines.append("")

    if commit:
        lines.append(f"커밋: <code>{commit}</code>")
    if next_steps:
        lines.append(f"다음 단계: {next_steps}")
    if extra:
        lines.append(f"\n{extra}")

    message = "\n".join(lines)
    _send(token, message)
    sys.stdout.buffer.write(f"[Telegram] OK — {task_name}\n".encode("utf-8"))


# ─── CLI (레거시 호환) ────────────────────────────────────────────────────────

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.stdout.buffer.write(
            b"Usage: python scripts/notify_telegram.py <task> [files] [commit] [next_steps]\n"
        )
        sys.exit(1)

    notify(
        task_name  = args[0],
        files      = args[1] if len(args) > 1 else None,
        commit     = args[2] if len(args) > 2 else None,
        next_steps = args[3] if len(args) > 3 else None,
    )
