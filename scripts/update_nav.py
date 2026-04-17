"""Replace nav on all HTML pages with new dropdown nav."""
import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"C:\Users\kayky\Desktop\RedSeal-Project\allforyou-bit.github.io"

# ── New dropdown CSS (added before </style>) ─────────────────────────────
DROP_CSS = """
/* ── NAV DROPDOWN (2026-04) ── */
.nav-dropdown{position:relative;display:inline-flex;align-items:center}
.nav-drop-btn{background:none;border:none;color:rgba(255,255,255,.85);font-weight:600;font-size:.88rem;cursor:pointer;font-family:inherit;padding:16px 0;display:inline-flex;align-items:center;gap:4px;transition:color .2s;white-space:nowrap}
.nav-drop-btn:hover,.nav-dropdown.open>.nav-drop-btn{color:#f0a500}
.nav-drop-menu{display:none;position:absolute;top:calc(100% + 2px);left:0;background:#1a3a5c;border-radius:8px;box-shadow:0 10px 28px rgba(0,0,0,.32);min-width:230px;z-index:300;border:1px solid rgba(255,255,255,.12);padding:6px 0}
.nav-dropdown.open>.nav-drop-menu{display:block}
.nav-drop-menu a{display:block!important;padding:9px 18px!important;color:rgba(255,255,255,.85)!important;text-decoration:none!important;font-size:.84rem!important;font-weight:600!important;transition:all .15s!important;border-bottom:1px solid rgba(255,255,255,.05)!important;width:100%!important}
.nav-drop-menu a:last-child{border-bottom:none!important}
.nav-drop-menu a:hover{background:rgba(255,255,255,.1)!important;color:#f0a500!important}
@media(max-width:860px){
  .nav-dropdown{width:100%}
  .nav-drop-btn{width:100%;padding:13px 20px!important;border-bottom:1px solid rgba(255,255,255,.07)!important;font-size:.9rem!important;justify-content:space-between!important}
  .nav-drop-menu{position:static!important;background:#0d2440!important;box-shadow:none!important;border-radius:0!important;border:none!important;padding:0!important;min-width:unset!important}
  .nav-drop-menu a{padding:10px 20px 10px 36px!important;border-bottom:1px solid rgba(255,255,255,.04)!important;font-size:.86rem!important}
}"""

# ── Nav JS (appended before </body>) ─────────────────────────────────────
NAV_JS = """<script>
(function(){
  var nt=document.getElementById('navToggle'),nl=document.getElementById('navLinks');
  var td=document.getElementById('tradesDrop'),tb=document.getElementById('tradesBtn');
  if(nt&&nl)nt.addEventListener('click',function(){var o=nl.classList.toggle('open');nt.textContent=o?'✕':'☰';});
  if(tb&&td){tb.addEventListener('click',function(e){e.stopPropagation();td.classList.toggle('open');});
  document.addEventListener('click',function(){if(td)td.classList.remove('open');});}
})();
</script>"""

# ── New nav HTML (quiz pages keep class="site-nav") ───────────────────────
def new_nav(is_quiz, active_href=None):
    tag = 'nav class="site-nav"' if is_quiz else 'nav'
    trades = [
        ('/421a.html',  '🚜 421A Heavy Equipment'),
        ('/310t.html',  '🚛 310T Truck &amp; Transport'),
        ('/309a.html',  '⚡ 309A Construction Electrician'),
        ('/310s.html',  '🔧 310S Automotive'),
        ('/308a.html',  '❄️ 308A HVAC/Refrigeration'),
        ('/276a.html',  '🔥 276A Welder'),
        ('/447a.html',  '🔩 447A Plumber'),
        ('/313a.html',  '⚡ 313A Industrial Electrician'),
        ('/442a.html',  '🏗️ 442A Ironworker'),
    ]
    drop_links = '\n'.join(f'        <a href="{href}">{name}</a>' for href, name in trades)
    home_active = ' class="active"' if (active_href == '/') else ''
    return f"""<{tag}>
  <a href="/" class="nav-brand">🔧 Red Seal Prep</a>
  <button class="nav-toggle" id="navToggle">☰</button>
  <div class="nav-links" id="navLinks">
    <a href="/"{{home_active}}>Home</a>
    <div class="nav-dropdown" id="tradesDrop">
      <button class="nav-drop-btn" id="tradesBtn">Trades ▾</button>
      <div class="nav-drop-menu">
{drop_links}
      </div>
    </div>
    <a href="/practice-quizzes.html">Quizzes</a>
    <a href="/red-seal-trades.html">Guides</a>
    <a href="/about.html">About</a>
  </div>
</{tag.split()[0]}>""".replace('{home_active}', home_active)

QUIZ_FILES = {'421a.html','310t.html','309a.html','310s.html','308a.html','276a.html','447a.html','313a.html','442a.html'}
SKIP_FILES = {'index.html', '404.html'}  # index.html already updated

ok = fail = skip_count = 0
html_files = [f for f in os.listdir(BASE) if f.endswith('.html')]

for fname in sorted(html_files):
    if fname in SKIP_FILES:
        print(f"SKIP: {fname}")
        skip_count += 1
        continue
    path = os.path.join(BASE, fname)
    with open(path, encoding='utf-8') as f:
        content = f.read()

    is_quiz = fname in QUIZ_FILES
    nav_close_tag = '</nav>' if not is_quiz else '</nav>'

    # Check if already has new nav (has nav-dropdown)
    if 'nav-dropdown' in content and 'navToggle' in content and 'tradesDrop' in content:
        print(f"SKIP (already updated): {fname}")
        skip_count += 1
        continue

    changed = False

    # 1. Find and replace nav HTML block
    # Matches <nav ...> ... </nav> (first occurrence)
    nav_pattern = re.compile(r'<nav[^>]*>.*?</nav>', re.DOTALL)
    m = nav_pattern.search(content)
    if m:
        replacement = new_nav(is_quiz)
        content = content[:m.start()] + replacement + content[m.end():]
        changed = True
    else:
        print(f"WARN (no nav found): {fname}")

    # 2. Add dropdown CSS before </style>
    if 'nav-drop-btn' not in content:
        # Find last </style> in head
        style_end = content.find('</style>')
        if style_end != -1:
            content = content[:style_end] + DROP_CSS + '\n' + content[style_end:]
            changed = True

    # 3. Add nav JS before </body>
    if 'navToggle' in content and 'addEventListener' not in content[content.rfind('navToggle')-500:content.rfind('navToggle')+200]:
        body_end = content.rfind('</body>')
        if body_end != -1:
            content = content[:body_end] + NAV_JS + '\n' + content[body_end:]
            changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {fname}")
        ok += 1
    else:
        print(f"- no change: {fname}")
        skip_count += 1

print(f"\n완료: 업데이트 {ok}, 스킵 {skip_count}, 실패 {fail}")
