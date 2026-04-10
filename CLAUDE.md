# 프로젝트 컨텍스트 — Canada Red Seal Exam Prep

이 파일은 새 Claude Code 세션에서 자동으로 읽힌다. 현재까지의 작업 전체 상태가 담겨있다.

---

## 사이트 기본 정보

- **URL:** https://allforyou-bit.github.io
- **GitHub 저장소:** https://github.com/allforyou-bit/allforyou-bit.github.io
- **GitHub 계정:** allforyou-bit
- **GitHub CLI 경로:** `C:\Program Files\GitHub CLI\gh.exe`
- **플랫폼:** GitHub Pages (무료 호스팅)
- **AdSense ID:** `ca-pub-6709396576574623`
- **Google Search Console 인증코드:** `AySEYGsNWhilNyl3EpVTQu6a3p0l6E1ZCe7P0EUN8O8`
- **IndexNow 키:** `c81bf78677cc427dbdd74c107c12d22b` (파일: c81bf78677cc427dbdd74c107c12d22b.txt)

## 사용자 정보

- 421A 중급 수준 Heavy Equipment Technician 어프렌티스
- 한국어 사용자, 비개발자
- Claude가 자율적으로 판단해서 바로 실행하는 걸 선호 (매번 허락 요청 불필요)
- 주 목표: AdSense 수익 창출 + 421A 시험 준비

---

## 현재 파일 구조 (총 34개 HTML)

```
allforyou-bit.github.io/
├── index.html               ← 메인 홈페이지 (5개 trade 카드 + 20개 article 카드, 770+ 표기)
├── 421a.html                ← 421A 퀴즈 (220문제) ✅ FAQ Schema ✅
├── 310t.html                ← 310T 퀴즈 (165문제) ✅ FAQ Schema ✅
├── 309a.html                ← 309A 퀴즈 (135문제) ✅ FAQ Schema ✅
├── 310s.html                ← 310S 퀴즈 (135문제) ✅ FAQ Schema ✅
├── 308a.html                ← 308A 퀴즈 (115문제) ✅ FAQ Schema ✅
├── exam-guide.html          ← 시험 등록 가이드 (1,500단어+, FAQ Schema) ✅
├── study-guide.html         ← 학습 가이드 (5개 trade 탭 포함) ✅
├── about.html               ← 소개 페이지 (저자 바이오, E-E-A-T) ✅
├── contact.html             ← 연락처 (lidbil515@gmail.com) ✅
├── privacy.html             ← 개인정보처리방침 ✅
├── terms.html               ← 이용약관 ✅
├── disclaimer.html          ← 면책조항 ✅
├── 404.html                 ← 커스텀 404 페이지 ✅
├── ads.txt                  ← AdSense 소유권 인증
├── sitemap.xml              ← 34개 URL
├── robots.txt               ← 검색엔진 설정
├── favicon.svg              ← RS 로고
├── .gitignore               ← .claude/settings.local.json 제외
│
├── [커리어 가이드 기사 - 8개] ✅
│   ├── how-to-become-heavy-equipment-technician-canada.html
│   ├── how-to-become-truck-transport-mechanic-canada.html
│   ├── construction-electrician-309a-career-canada.html
│   ├── automotive-service-technician-310s-career-canada.html
│   ├── hvac-refrigeration-mechanic-308a-career-canada.html
│   ├── what-is-red-seal-certification-canada.html
│   ├── red-seal-421a-exam-tips.html
│   └── which-red-seal-trade-should-i-choose.html  ← 비교 가이드 (FAQ Schema)
│
├── [시험 전략 기사 - 4개] ✅ (모두 FAQ Schema)
│   ├── how-to-pass-red-seal-310t-exam.html
│   ├── how-to-pass-red-seal-309a-exam.html
│   ├── how-to-pass-red-seal-310s-exam.html
│   └── how-to-pass-red-seal-308a-exam.html
│
├── [급여 가이드 기사 - 5개] ✅ (모두 FAQ Schema)
│   ├── heavy-equipment-technician-salary-canada.html
│   ├── truck-transport-mechanic-310t-salary-canada.html
│   ├── construction-electrician-309a-salary-canada.html
│   ├── automotive-service-technician-310s-salary-canada.html
│   └── hvac-refrigeration-mechanic-308a-salary-canada.html
│
└── [트래픽 기사 - 3개] ✅ (모두 FAQ Schema + BreadcrumbList + HowTo Schema)
    ├── red-seal-exam-format-guide.html       ← 시험 형식 완전 가이드 (120~135문제, 시간, CBT)
    ├── trades-in-demand-canada-2026.html     ← 캐나다 수요 직종 10개 + 급여 데이터
    └── how-long-red-seal-apprenticeship-canada.html  ← 어프렌티스십 기간 (5개 trade 상세)
```

---

## 퀴즈 문제 수 현황 (최신)

| 파일 | 문제 수 | 주제 |
|------|---------|------|
| 421a.html | **220문제** | Safety, Engine, Electrical, Hydraulics, Powertrain, Brakes |
| 310t.html | **165문제** | Air Brakes, Engine, Drivetrain, DOT Compliance, Electrical |
| 309a.html | **135문제** | Theory, CEC Code, Motors, Wiring Methods, Safety |
| 310s.html | **135문제** | Engine, Brakes, Electrical, Suspension, Transmission |
| 308a.html | **115문제** | Cycle, Refrigerants, Components, Controls, Troubleshooting |
| **합계** | **770문제** | |

---

## 퀴즈 페이지 기능 현황 (모든 5개 퀴즈 페이지 동일)

- [x] **Mock Exam 시스템** — 토픽/난이도 비례 출제, 결과 화면, URL 파라미터 자동 실행
- [x] **Mock Exam 타이머** — 1.5분/문제, 5분 이하 빨간색 경고
- [x] **Study Streak** — localStorage 기반 연속 학습일 + 오늘 맞힌 문제 수
- [x] **Share Score** — Web Share API + 클립보드 폴백
- [x] **Download Mock Results** — Mock Exam 결과 .txt 파일 다운로드 (오답 하이라이트)
- [x] **Download Study Sheet (PDF)** — 버튼 클릭 → 새 탭에 인쇄 최적화 HTML 오픈 → Ctrl+P로 PDF 저장. 토픽 필터 반영, 전문제+정답키+해설 포함
- [x] **Cookie Consent 배너** — GDPR 컴플라이언스
- [x] **Related Guides 섹션** — 각 퀴즈 페이지 하단 내부 링크 (4개: career/exam-tip/salary/what-is-red-seal)
- [x] **150단어+ 인트로 텍스트** — 콘텐츠 품질 (AdSense thin content 방지)
- [x] **Freshness Badge** — "Updated April 2026" 뱃지
- [x] **FAQ Schema** — 모든 5개 퀴즈 페이지 + 6개 exam-guide/salary 기사 포함

---

## 장문 기사 현황 (20개 완성)

### 커리어 가이드 (8개)
1. **How to Become a Heavy Equipment Technician** — 421A 커리어 가이드 (HowTo Schema ✅)
2. **7 Proven Tips to Pass the Red Seal 421A Exam** — 시험 전략
3. **Heavy Equipment Technician Salary Canada 2026** — 주별 임금 데이터 (FAQ Schema)
4. **What Is the Red Seal Certification?** — Red Seal 제도 전체 설명
5. **How to Become a Truck & Transport Mechanic** — 310T 커리어 가이드 (HowTo Schema ✅)
6. **Construction Electrician Career Guide** — 309A 커리어 가이드 (HowTo Schema ✅)
7. **Automotive Service Technician Career Guide** — 310S 커리어 가이드 (HowTo Schema ✅)
8. **Refrigeration & AC Mechanic Career Guide** — 308A 커리어 가이드 (HowTo Schema ✅)

### 시험 전략 기사 (4개, 모두 FAQ Schema)
9. **How to Pass the Red Seal 310T Exam** — 310T 시험 팁
10. **How to Pass the Red Seal 309A Exam** — 309A 시험 팁
11. **How to Pass the Red Seal 310S Exam** — 310S 시험 팁
12. **How to Pass the Red Seal 308A Exam** — 308A 시험 팁

### 급여 가이드 (5개, 모두 FAQ Schema)
13. **Truck & Transport Mechanic Salary Canada 2026** — 310T 급여
14. **Construction Electrician Salary Canada 2026** — 309A 급여
15. **Automotive Service Technician Salary Canada 2026** — 310S 급여
16. **HVAC Mechanic Salary Canada 2026** — 308A 급여

### 비교 가이드 (1개, FAQ Schema)
17. **Which Red Seal Trade Should I Choose?** — 5개 trade 비교표

### 트래픽 기사 (3개, 모두 Article + FAQ + BreadcrumbList Schema)
18. **Red Seal Exam Format 2026** — 시험 형식, 문제 수, 시간, CBT, 재시험 정책
19. **10 Skilled Trades in Demand in Canada 2026** — 수요 직종 + 급여 데이터
20. **How Long Does a Red Seal Apprenticeship Take?** — 5개 trade 기간 + 임금 진행표

---

## 내부 링크 네트워크 (완성)

각 퀴즈 페이지 Related Guides (4개 링크):
- Career Guide → Exam Tips Article → Salary Guide → What Is Red Seal

각 커리어 기사: salary + exam tips 양방향 연결
각 급여 기사: career guide + related salary guides 연결
비교 기사: what-is-red-seal, exam-guide, 421a.html에서 링크됨

---

## SEO / 인프라 완료 사항

- [x] Google Search Console 등록 + HTML 태그 인증 완료
- [x] Google AdSense 신청 완료 (심사 대기 중)
- [x] ads.txt 설치 완료
- [x] sitemap.xml 제출 완료 (34개 URL)
- [x] IndexNow (Bing/Yandex) — 34개 URL 제출 완료
- [x] FAQ Schema (LD+JSON) — 전체 26개 페이지 (퀴즈 5 + 커리어 가이드 6 + 시험전략 5 + 급여 5 + 비교 1 + exam-guide 1 + 트래픽 기사 3)
- [x] BreadcrumbList Schema — 19개 기사/가이드 페이지 전체 (+ 트래픽 기사 3개 포함)
- [x] HowTo Schema — 5개 커리어 가이드 페이지 (421A, 310T, 309A, 310S, 308A)
- [x] Article Schema — 장문 기사 전체
- [x] terms.html + disclaimer.html (AdSense 정책 요구사항)
- [x] robots.txt
- [x] 쿠키 동의 배너 (GDPR)
- [x] 전체 페이지 nav/footer 통일 (sticky nav, min-height:52px)
- [x] 완전한 내부 링크 네트워크 — 퀴즈↔커리어↔급여↔시험전략↔비교 양방향
- [x] Open Graph (og:title/description/url/type) + Twitter Card 메타 태그 — 전체 페이지
- [x] canonical 태그 — 전체 article 페이지 + 퀴즈 페이지
- [x] nav 링크 순서 통일 — Home | 421A | 310T | 309A | 310S | 308A | Exam Guide | Study Guide | About
- [x] 전 도 apprenticeship 연락처 URL 수정 (12개 province/territory)
- [x] study-guide.html 전면 재작성 (5개 trade 탭 인터페이스)
- [x] .gitignore 생성 (.claude/settings.local.json 제외)
- [x] 팩트체크 완료 — 4개 오류 수정 (BC 기관명, Ontario College of Trades→STO, 310T 문제 수, Manitoba 중복)

---

## Search Console 수동 색인 요청 현황

**완료된 것 (사용자가 직접 수행):**
- URL 1~11: 완료 (2026-04-09)

**남은 것 (내일 또는 다음 세션에 수행):**
- URL 12: https://allforyou-bit.github.io/309a.html
- URL 13: https://allforyou-bit.github.io/310s.html
- URL 14: https://allforyou-bit.github.io/308a.html
- URL 15: https://allforyou-bit.github.io/421a.html
- 그 이후: 새로 추가된 17개 기사들도 요청

**방법:** search.google.com/search-console → URL 검사 → URL 붙여넣기 → "색인 생성 요청" 클릭

---

## AdSense 심사 상태

**제출 완료, 심사 대기 중.** 현재 승인 확률 추정: **75~80%**

승인되면:
- 각 페이지의 `<div class="ad-banner">Advertisement</div>` 플레이스홀더를
  실제 `<ins class="adsbygoogle">` 광고 코드로 교체
- AdSense 대시보드에서 광고 단위 생성 후 코드 받아서 삽입

---

## 앞으로 할 일 (우선순위 순)

### 1순위 — AdSense 승인 후 즉시
- [ ] 광고 단위 생성 및 플레이스홀더 교체 (각 페이지 ad-banner div 2~3개)
- [ ] 수익 모니터링 시작

### 2순위 — Search Console 수동 색인 요청 (남은 것)
- [ ] URL 12~15 색인 요청 (309a, 310s, 308a, 421a)
- [ ] 새로 추가된 17개 기사들 색인 요청
- [ ] sitemap.xml 재제출 확인

### 3순위 — 사용자 경험 개선
- [ ] 연속 정답 스트릭 카운터 ("🔥 3 in a row!") — 퀴즈 중 표시
- [ ] 오답 신고 버튼 (사용자가 문제 오류 제보 가능)
- [ ] 퀴즈 결과 이메일 전송 (EmailJS)

### 4순위 — 장기 확장
- [ ] 새 trade 추가: 442A Ironworker, 403A Gas Fitter, 306A Sheet Metal Worker
- [ ] 각 신규 trade에 퀴즈 + 커리어 기사 세트

---

## 기술 스택

- **순수 HTML/CSS/JS** — 프레임워크 없음
- **퀴즈 방식:** JavaScript 배열 + 필터 (topic/difficulty)
- **Mock Exam:** buildMockQs(n) — 토픽 비례 + 40/40/20 난이도 분배
- **Download Study Sheet:** window.open() + document.write() — 인쇄 최적화 HTML, Ctrl+P로 PDF
- **localStorage 키:** studyStreak, streakDate, todayCorrect_[trade], todayDate_[trade], mockBest_[trade], cookieOk
- **배포:** git push → GitHub Pages 자동 배포
- **Push 방법:** `cd "C:\Users\kayky\Desktop\RedSeal-Project\allforyou-bit.github.io" && git add -A && git commit -m "메시지" && git push origin master`

---

## 주의사항

- 이 프로젝트 폴더 위치: `C:\Users\kayky\Desktop\RedSeal-Project\allforyou-bit.github.io`
- git remote는 GitHub에 연결되어 있어 push하면 바로 사이트에 반영됨
- Edit 툴로 퀴즈 파일 수정 시 동일한 문자열이 여러 개 있으면 `replace_all: true` 또는 고유 컨텍스트 포함
- Download Study Sheet: currentTopic 변수 기준으로 필터링 → 토픽 탭 선택 상태 반영됨
- sitemap.xml: 새 페이지 추가 시 수동으로 업데이트 필요
