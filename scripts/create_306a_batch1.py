"""
306A Sheet Metal Worker Quiz - Batch 1/4
Writes HTML shell + Q1-25 to 306a_temp.html
"""
from pathlib import Path
BASE = Path(__file__).parent.parent

HTML_SHELL = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FSSHZMWVLW"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-FSSHZMWVLW');
</script>
<meta name="google-site-verification" content="AySEYGsNWhilNyl3EpVTQu6a3p0l6E1ZCe7P0EUN8O8" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Free 306A Red Seal Practice Exam — 100 Questions 2026</title>
<meta name="description" content="Free 306A Sheet Metal Worker Red Seal practice exam. 100 questions: pattern development, SMACNA duct standards, seams, HVAC installation, materials, safety. Canada 2026.">
<meta name="keywords" content="306A Red Seal, Sheet Metal Worker exam Canada, SMACNA practice questions, pattern development exam, 306A practice test 2026">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://allforyou-bit.github.io/306a.html">
<meta property="og:title" content="306A Sheet Metal Worker – 100 Free Red Seal Practice Questions 2026">
<meta property="og:description" content="Free 306A Red Seal practice quiz — 100 questions covering pattern development, SMACNA, seams & joints, HVAC ductwork, materials and safety. Mock Exam included.">
<meta property="og:url" content="https://allforyou-bit.github.io/306a.html">
<meta property="og:type" content="website">
<meta property="og:image" content="https://allforyou-bit.github.io/favicon.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="306A Sheet Metal Worker – 100 Free Red Seal Practice Questions 2026">
<meta name="twitter:description" content="100 free 306A Red Seal practice questions + Mock Exam. SMACNA aligned. Canada 2026.">
<meta name="twitter:image" content="https://allforyou-bit.github.io/favicon.svg">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6709396576574623" crossorigin="anonymous"></script>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How many questions are on the 306A Sheet Metal Worker Red Seal exam?","acceptedAnswer":{"@type":"Answer","text":"The 306A Sheet Metal Worker Red Seal exam contains approximately 100 multiple-choice questions. A minimum score of 70% is required to pass. The exam covers pattern development, SMACNA duct construction standards, seam types, materials, and HVAC installation."}},{"@type":"Question","name":"What is the most tested topic on the 306A Sheet Metal exam?","acceptedAnswer":{"@type":"Answer","text":"Pattern development is the most heavily tested topic at approximately 20% of the exam. Candidates must know parallel line, radial line, and triangulation methods — when to apply each and how to determine true lengths."}},{"@type":"Question","name":"What SMACNA standards apply to the 306A exam?","acceptedAnswer":{"@type":"Answer","text":"SMACNA HVAC Duct Construction Standards govern pressure class selection (1/2 to 10 WG), gauge requirements, reinforcement, duct sealing classes (A, B, C), and support spacing. Knowing how pressure class determines every construction decision is essential."}}]}
</script>
<style>
  :root{--primary:#1a3a5c;--accent:#f0a500;--green:#27ae60;--red:#e74c3c;--light:#f4f7fb;--card:#ffffff;--text:#2c3e50;--muted:#7f8c8d;--border:#dce3ec}
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:'Segoe UI',Arial,sans-serif;background:var(--light);color:var(--text)}
  .site-nav{background:#1a3a5c;padding:0 24px;display:flex;gap:18px;align-items:center;flex-wrap:wrap;position:sticky;top:0;z-index:100;box-shadow:0 2px 8px rgba(0,0,0,.18);min-height:52px}
  .site-nav a{color:white;text-decoration:none;font-weight:600;font-size:.88rem;padding:16px 0;display:inline-block}
  .site-nav a:hover,.site-nav a.active{color:#f0a500}
  header{background:var(--primary);color:white;padding:24px 20px 18px;text-align:center}
  header h1{font-size:1.6rem;font-weight:700;margin-bottom:6px}
  header p{font-size:.9rem;opacity:.85}
  .badge{display:inline-block;background:var(--accent);color:#fff;font-size:.72rem;font-weight:700;padding:3px 10px;border-radius:20px;margin-top:8px;letter-spacing:.5px}
  .update-pill{display:inline-flex;align-items:center;gap:4px;background:#e8f9ef;color:#1a6636;font-size:.68rem;font-weight:700;padding:3px 9px;border-radius:10px;border:1px solid #a9dfbf;margin-left:8px;vertical-align:middle}
  .rsos-pill{display:inline-flex;align-items:center;gap:4px;background:#eaf0f9;color:#1a3a5c;font-size:.68rem;font-weight:700;padding:3px 9px;border-radius:10px;border:1px solid #afc3dc;margin-left:4px;vertical-align:middle}
  .container{max-width:900px;margin:0 auto;padding:20px 16px}
  .intro-box{background:var(--card);border-left:5px solid var(--accent);border-radius:8px;padding:18px 20px;margin-bottom:24px;box-shadow:0 2px 8px rgba(0,0,0,.06)}
  .intro-box h2{font-size:1.05rem;margin-bottom:8px;color:var(--primary)}
  .intro-box p{font-size:.88rem;line-height:1.7;color:var(--muted)}
  .structure-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:12px 0}
  .structure-table th{background:var(--primary);color:white;padding:9px 12px;text-align:left}
  .structure-table td{padding:8px 12px;border-bottom:1px solid var(--border)}
  .structure-table tr:nth-child(even) td{background:#f9fbfd}
  .topic-tabs{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px}
  .tab-btn{padding:8px 16px;border:2px solid var(--primary);border-radius:24px;background:white;color:var(--primary);font-size:.82rem;font-weight:600;cursor:pointer;transition:all .2s}
  .tab-btn:hover,.tab-btn.active{background:var(--primary);color:white}
  .difficulty-row{display:flex;gap:10px;margin-bottom:20px;align-items:center}
  .difficulty-row span{font-size:.85rem;font-weight:600;color:var(--muted)}
  .diff-btn{padding:6px 14px;border-radius:6px;border:none;font-size:.8rem;font-weight:700;cursor:pointer}
  .diff-btn.easy{background:#d5f5e3;color:#1e8449}
  .diff-btn.medium{background:#fdebd0;color:#d35400}
  .diff-btn.hard{background:#fadbd8;color:#c0392b}
  .diff-btn.active{outline:3px solid var(--text)}
  .question-card{background:var(--card);border-radius:12px;padding:24px;box-shadow:0 3px 12px rgba(0,0,0,.08);margin-bottom:20px}
  .q-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}
  .q-topic{font-size:.75rem;font-weight:700;color:var(--accent);text-transform:uppercase;letter-spacing:.8px}
  .q-diff{font-size:.72rem;padding:3px 10px;border-radius:12px;font-weight:700}
  .q-diff.easy{background:#d5f5e3;color:#1e8449}
  .q-diff.medium{background:#fdebd0;color:#d35400}
  .q-diff.hard{background:#fadbd8;color:#c0392b}
  .q-number{font-size:.78rem;color:var(--muted);margin-bottom:6px}
  .q-text{font-size:1rem;font-weight:600;line-height:1.6;margin-bottom:20px}
  .options{display:flex;flex-direction:column;gap:10px}
  .option-btn{background:#f4f7fb;border:2px solid var(--border);border-radius:8px;padding:12px 16px;text-align:left;font-size:.92rem;cursor:pointer;transition:all .18s;display:flex;align-items:flex-start;gap:12px}
  .option-btn:hover:not(:disabled){border-color:var(--primary);background:#eaf0f9}
  .option-letter{font-weight:700;color:var(--primary);min-width:22px;margin-top:1px}
  .option-btn.correct{background:#d5f5e3;border-color:var(--green)}
  .option-btn.wrong{background:#fadbd8;border-color:var(--red)}
  .option-btn.reveal{background:#d5f5e3;border-color:var(--green)}
  .explanation{display:none;margin-top:18px;padding:16px;background:#eaf4ff;border-left:4px solid var(--primary);border-radius:6px;font-size:.88rem;line-height:1.7}
  .explanation.show{display:block}
  .explanation strong{color:var(--primary)}
  .key-concept{background:#fff8e1;border:1px solid #f9c74f;border-radius:6px;padding:10px 14px;margin-top:10px;font-size:.84rem}
  .key-concept strong{color:#c07a00}
  .nav-row{display:flex;justify-content:space-between;align-items:center;margin-top:16px}
  .nav-btn{padding:10px 22px;border-radius:8px;border:none;font-size:.88rem;font-weight:700;cursor:pointer}
  .nav-btn.next{background:var(--primary);color:white}
  .nav-btn.prev{background:#e0e0e0;color:var(--text)}
  .nav-btn:disabled{opacity:.4;cursor:not-allowed}
  .score-box{background:var(--card);border-radius:10px;padding:16px 20px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.07);margin-bottom:20px}
  .score-box .score-num{font-size:2rem;font-weight:800;color:var(--primary)}
  .score-box .score-label{font-size:.82rem;color:var(--muted);margin-top:2px}
  .progress-bar-wrap{background:var(--border);border-radius:10px;height:10px;margin-top:10px;overflow:hidden}
  .progress-bar{height:100%;border-radius:10px;background:var(--accent);transition:width .4s}
  .concept-section{background:var(--card);border-radius:12px;padding:22px;box-shadow:0 2px 10px rgba(0,0,0,.07);margin-bottom:24px}
  .concept-section h3{color:var(--primary);margin-bottom:12px;font-size:1.05rem}
  footer{background:var(--primary);color:rgba(255,255,255,.75);text-align:center;padding:20px;font-size:.8rem;margin-top:40px}
  footer a{color:var(--accent);text-decoration:none}
  .mock-launch-bar{display:flex;align-items:center;justify-content:space-between;background:#fff8e1;border:2px solid #f0a500;border-radius:10px;padding:12px 18px;margin-bottom:18px;flex-wrap:wrap;gap:10px}
  .mock-launch-bar p{font-size:.85rem;color:#5d4037;margin:0}
  .btn-mock{background:#f0a500;color:#fff;border:none;border-radius:8px;padding:10px 22px;font-weight:700;font-size:.88rem;cursor:pointer}
  .btn-mock:hover{background:#d4930a}
  .mock-count-btn{background:#f4f7fb;border:2px solid #dce3ec;border-radius:12px;padding:18px 10px;cursor:pointer;color:#1a3a5c;font-family:inherit;width:100%}
  .mock-count-btn:hover{border-color:#f0a500;background:#fff8e1}
  .mock-opt{background:#f4f7fb;border:2px solid #dce3ec;border-radius:8px;padding:12px 16px;cursor:pointer;text-align:left;font-family:inherit;font-size:.9rem;color:#2c3e50;width:100%;display:block}
  .mock-opt:hover:not(:disabled){border-color:#2d6a9f;background:#eaf0f9}
  .mock-opt.mock-c{background:#e8f9ef;border-color:#27ae60;color:#1a6636}
  .mock-opt.mock-w{background:#fdecea;border-color:#e74c3c;color:#922b21}
  .mock-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.72);z-index:400;align-items:flex-start;justify-content:center;padding:16px;overflow-y:auto}
  .mock-panel{background:#fff;border-radius:16px;width:100%;max-width:680px;margin:auto;box-shadow:0 20px 60px rgba(0,0,0,.3)}
  .mock-head{background:#1a3a5c;border-radius:16px 16px 0 0;padding:16px 20px;display:flex;align-items:center;gap:12px}
  .mock-bar-wrap{height:5px;background:#dce3ec}
  .mock-bar-fill{height:100%;background:#f0a500;transition:width .4s}
  .mock-body{padding:24px}
  .mock-q-text{font-size:.98rem;font-weight:600;color:#1a3a5c;line-height:1.65;margin-bottom:20px}
  .mock-feedback{display:none;background:#f4f7fb;border-radius:10px;padding:14px 16px;margin-top:16px;border-left:4px solid #1a3a5c;font-size:.88rem;line-height:1.7}
  .btn-mock-next{display:none;margin-top:14px;background:#1a3a5c;color:#fff;border:none;padding:13px 24px;border-radius:8px;font-weight:700;cursor:pointer;font-size:.92rem;width:100%}
  .wrong-tab-btn{background:#fdecea!important;border-color:#e74c3c!important;color:#c0392b!important}
  .wrong-tab-btn.active{background:#e74c3c!important;color:#fff!important}
  .topic-progress-panel{background:#fff;border-radius:10px;padding:14px 16px;margin-bottom:16px;box-shadow:0 2px 8px rgba(0,0,0,.07)}
  .score-hist-wrap{margin-top:10px;padding-top:10px;border-top:1px solid #eee}
  .score-hist-wrap label{font-size:.72rem;font-weight:700;color:var(--muted);display:block;margin-bottom:6px}
  .score-hist-list{display:flex;flex-wrap:wrap;gap:6px}
  .mode-switch-row{display:flex;gap:8px;margin-bottom:16px;align-items:center}
  .mode-btn{padding:7px 16px;border-radius:20px;border:2px solid var(--primary);background:#fff;color:var(--primary);font-size:.8rem;font-weight:700;cursor:pointer;transition:all .2s}
  .mode-btn.active{background:var(--primary);color:#fff}
  .flashcard-section{display:none;background:#fff;border-radius:14px;padding:24px;box-shadow:0 3px 14px rgba(0,0,0,.10);margin-bottom:20px}
  .fc-counter{font-size:.78rem;color:var(--muted);margin-bottom:12px;text-align:center}
  .fc-scene{width:100%;min-height:200px;perspective:900px;cursor:pointer;margin-bottom:16px}
  .fc-card{width:100%;min-height:200px;position:relative;transform-style:preserve-3d;transition:transform .5s}
  .fc-front,.fc-back{position:absolute;width:100%;min-height:200px;backface-visibility:hidden;border-radius:10px;padding:24px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
  .fc-front{background:#eaf0f9;border:2px solid var(--primary)}
  .fc-back{background:#e8f9ef;border:2px solid var(--green);transform:rotateY(180deg)}
  .fc-actions{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:8px}
  .fc-btn{padding:9px 20px;border-radius:8px;border:none;font-size:.85rem;font-weight:700;cursor:pointer}
  .fc-btn.know{background:#27ae60;color:#fff}
  .fc-btn.again{background:#e74c3c;color:#fff}
  .fc-nav{display:flex;gap:10px;justify-content:center;margin-top:10px}
  .fc-nav button{padding:6px 14px;border-radius:6px;border:2px solid var(--border);background:#fff;cursor:pointer;font-size:.82rem;font-weight:600}
  .nav-brand{display:none;color:white;font-weight:800;font-size:.92rem;text-decoration:none;white-space:nowrap;align-items:center}
  .nav-toggle{display:none;background:none;border:none;color:white;font-size:1.5rem;cursor:pointer;padding:0;line-height:1;flex-shrink:0;margin-left:auto;min-width:40px;text-align:center}
  .nav-links{display:flex;flex-wrap:nowrap;overflow:hidden;gap:18px;align-items:center}
  .nav-dropdown{position:relative}
  .nav-drop-btn{background:none;border:none;color:white;font-weight:600;font-size:.88rem;cursor:pointer;padding:16px 0;display:inline-block}
  .nav-drop-btn:hover{color:#f0a500}
  .nav-drop-menu{display:none;position:absolute;top:100%;left:0;background:#1a3a5c;border-radius:0 0 8px 8px;box-shadow:0 8px 24px rgba(0,0,0,.35);z-index:200;min-width:220px;padding:6px 0}
  .nav-drop-menu a{display:block;padding:10px 18px;color:white;font-size:.85rem;white-space:nowrap}
  .nav-drop-menu a:hover{background:rgba(255,255,255,.1);color:#f0a500}
  .exam-accordion{margin-bottom:20px}
  .exam-accordion summary{cursor:pointer;color:var(--primary);font-weight:700;font-size:.95rem;padding:12px 16px;background:var(--card);border-radius:8px;border-left:4px solid var(--accent);box-shadow:0 1px 5px rgba(0,0,0,.07);list-style:none;display:flex;justify-content:space-between;align-items:center}
  .exam-accordion summary::-webkit-details-marker{display:none}
  .exam-accordion summary::after{content:"\25BC";font-size:.75rem;opacity:.6;transition:transform .2s}
  .exam-accordion[open] summary::after{transform:rotate(180deg)}
  .exam-accordion .concept-section{border-radius:0 0 8px 8px;margin-top:0;box-shadow:0 2px 6px rgba(0,0,0,.06)}
  @media(max-width:860px){.site-nav{flex-wrap:nowrap!important;padding:0 14px!important;gap:0!important;position:relative}.nav-brand{display:flex;margin-right:auto}.nav-toggle{display:flex;align-items:center;justify-content:center;height:52px}.nav-links{display:none;position:absolute;top:52px;left:0;right:0;background:#1a3a5c;flex-direction:column;z-index:201;box-shadow:0 8px 24px rgba(0,0,0,.35);border-top:1px solid rgba(255,255,255,.1);max-height:75vh;overflow-y:auto;gap:0}.nav-links.open{display:flex}.nav-links a{padding:13px 20px!important;border-bottom:1px solid rgba(255,255,255,.07)!important;font-size:.9rem!important;width:100%;display:block}.topic-tabs{overflow-x:auto;flex-wrap:nowrap!important;padding-bottom:6px;scrollbar-width:none}.tab-btn{white-space:nowrap;flex-shrink:0}.mode-switch-row{flex-wrap:wrap}.mock-launch-bar{flex-direction:column;align-items:flex-start}.question-card{padding:16px 14px!important}.difficulty-row{flex-wrap:wrap;gap:6px}header h1{font-size:1.25rem}.container{padding:14px 12px}.nav-drop-btn{width:100%;text-align:left;padding:13px 20px!important;border-bottom:1px solid rgba(255,255,255,.07)!important;font-size:.9rem!important}.nav-drop-menu{position:static;box-shadow:none;border-radius:0;padding:0;display:none;background:rgba(255,255,255,.05)}.nav-drop-menu a{padding-left:36px!important}.nav-dropdown.open .nav-drop-menu{display:block}}
  @media(max-width:480px){.q-text{font-size:.93rem}.option-btn{font-size:.86rem;padding:10px 12px}}
</style>
</head>
<body>
<nav class="site-nav">
  <a href="/" class="nav-brand">&#x1F527; Red Seal Prep</a>
  <button class="nav-toggle" id="navToggle">&#9776;</button>
  <div class="nav-links" id="navLinks">
    <a href="/">Home</a>
    <div class="nav-dropdown" id="tradesDrop">
      <button class="nav-drop-btn" id="tradesBtn">Trades &#x25BE;</button>
      <div class="nav-drop-menu">
        <a href="/421a.html">&#x1F69C; 421A Heavy Equipment</a>
        <a href="/310t.html">&#x1F69B; 310T Truck &amp; Transport</a>
        <a href="/309a.html">&#x26A1; 309A Construction Electrician</a>
        <a href="/310s.html">&#x1F527; 310S Automotive</a>
        <a href="/308a.html">&#x2744;&#xFE0F; 308A HVAC/Refrigeration</a>
        <a href="/276a.html">&#x1F525; 276A Welder</a>
        <a href="/447a.html">&#x1F529; 447A Plumber</a>
        <a href="/313a.html">&#x26A1; 313A Industrial Electrician</a>
        <a href="/442a.html">&#x1F3D7;&#xFE0F; 442A Ironworker</a>
        <a href="/403a.html">&#x1F525; 403A Gas Fitter</a>
        <a href="/306a.html">&#x1F529; 306A Sheet Metal</a>
      </div>
    </div>
    <a href="/practice-quizzes.html">Quizzes</a>
    <a href="/red-seal-trades.html">Guides</a>
    <a href="/about.html">About</a>
  </div>
</nav>
<header>
  <h1>306A Red Seal &#x2014; Sheet Metal Worker</h1>
  <p>Canada Certification Exam Practice Questions | 2026</p>
  <span class="badge">Based on 2023 Red Seal Occupational Standard (RSOS)</span>
  <span class="update-pill">&#x2713; Updated Apr 2026</span>
  <span class="rsos-pill">SMACNA / 2023 RSOS Aligned</span>
</header>
<!-- AdSense banner placeholder -->
<div class="container">
  <div class="intro-box">
<h2>About the 306A Red Seal Exam &#x2014; Sheet Metal Worker</h2>
<p>The <strong>306A Sheet Metal Worker Red Seal exam</strong> is Canada's national certification for sheet metal tradespeople working in HVAC ductwork fabrication and installation, architectural sheet metal, industrial exhaust systems, and commercial building work. The Red Seal 306A is recognized in all provinces and territories.</p>
<p>The exam consists of approximately <strong>100 multiple-choice questions</strong> based on the 2023 Red Seal Occupational Standard (RSOS) and aligned with <strong>SMACNA HVAC Duct Construction Standards</strong>, with a passing score of <strong>70%</strong>. Exam time is <strong>3 hours</strong>.</p>
<h3>Topic Breakdown (2023 RSOS)</h3>
<ul>
  <li><strong>Layout &amp; Pattern Development (~20%)</strong> &#x2014; Parallel line (prisms/cylinders), radial line (cones/pyramids), and triangulation (transitions). True length, gore construction, and selecting the correct method.</li>
  <li><strong>Sheet Metal Fabrication (~24%)</strong> &#x2014; SMACNA pressure classes, gauge selection, seam types (Pittsburgh, grooved, standing seam), drive/S-cleats, forming operations, and duct reinforcement.</li>
  <li><strong>Welding &amp; Joining (~16%)</strong> &#x2014; TIG/MIG/spot welding for sheet metal, riveting, soldering, and adhesive joining. Material-specific joining methods.</li>
  <li><strong>HVAC Ductwork Installation (~20%)</strong> &#x2014; Duct support spacing, sealing classes (A/B/C), flexible connections, dampers, plenums, and commissioning.</li>
  <li><strong>Safety &amp; Code (~12%)</strong> &#x2014; WHMIS/GHS, fall protection, rigging, hearing/eye protection, and CSA standards for sheet metal work.</li>
  <li><strong>Tools &amp; Equipment (~8%)</strong> &#x2014; Throatless shears, brakes, roll formers, plasma cutters, turret punches, and hand tools. Correct tool selection for material and task.</li>
</ul>
<h3>How to Use This Practice Tool</h3>
<p>This free tool includes <strong>100 questions</strong> covering all 306A topic blocks with full explanations. Use <strong>Topic Filter</strong> to drill pattern development or SMACNA standards. Run the <strong>Mock Exam</strong> to simulate the real 100-question timed format.</p>
<p>Related reading: <a href="/how-to-pass-red-seal-306a-exam.html">How to Pass the 306A Exam</a> | <a href="/306a-sheet-metal-worker-salary-canada.html">Sheet Metal Salary Guide</a> | <a href="/306a-sheet-metal-worker-career-canada.html">Career Guide Canada</a></p>
</div>
  <details class="exam-accordion">
    <summary>Exam Structure &#x2014; Topic Breakdown</summary>
    <div class="concept-section">
    <h3>Exam Structure &#x2014; Topic Breakdown</h3>
    <table class="structure-table">
      <tr><th>Block</th><th>Topic</th><th>Approx. Questions</th></tr>
      <tr><td>A</td><td>Layout &amp; Pattern Development</td><td>20</td></tr>
      <tr><td>B</td><td>Sheet Metal Fabrication &amp; SMACNA</td><td>24</td></tr>
      <tr><td>C</td><td>Welding &amp; Joining Methods</td><td>16</td></tr>
      <tr><td>D</td><td>HVAC Ductwork Installation</td><td>20</td></tr>
      <tr><td>E</td><td>Safety &amp; Code</td><td>12</td></tr>
      <tr><td>F</td><td>Tools &amp; Equipment</td><td>8</td></tr>
    </table>
    <p style="font-size:.8rem;color:var(--muted);margin-top:6px;">* Approximate distribution. Passing score: 70%. Standard: SMACNA HVAC Duct Construction Standards.</p>
  </div>
  </details>
  <div style="display:flex;gap:10px;margin-bottom:18px;flex-wrap:wrap;">
    <button disabled style="background:#95a5a6;color:#fff;border:none;border-radius:8px;padding:9px 18px;font-size:.82rem;font-weight:700;cursor:not-allowed">&#x1F4C4; Study Sheet &#x2014; Coming Soon</button>
  </div>
  <div class="topic-tabs" id="topicTabs">
    <button class="tab-btn active" onclick="setTopic('all',this)">All Topics</button>
    <button class="tab-btn" onclick="setTopic('layout',this)">Pattern Dev</button>
    <button class="tab-btn" onclick="setTopic('fabrication',this)">Fabrication</button>
    <button class="tab-btn" onclick="setTopic('welding',this)">Welding</button>
    <button class="tab-btn" onclick="setTopic('hvac',this)">HVAC Duct</button>
    <button class="tab-btn" onclick="setTopic('safety',this)">Safety &amp; Code</button>
    <button class="tab-btn" onclick="setTopic('tools',this)">Tools</button>
    <button class="tab-btn wrong-tab-btn" id="wrongBankTabBtn" onclick="setTopic('wrongbank',this)">&#x1F4D5; Mistakes (0)</button>
  </div>
  <div class="difficulty-row">
    <span>Difficulty:</span>
    <button class="diff-btn easy active" onclick="setDiff('all',this)">All</button>
    <button class="diff-btn easy" onclick="setDiff('easy',this)">Easy</button>
    <button class="diff-btn medium" onclick="setDiff('medium',this)">Medium</button>
    <button class="diff-btn hard" onclick="setDiff('hard',this)">Hard</button>
  </div>
  <div class="mode-switch-row">
    <span style="font-size:.82rem;font-weight:700;color:var(--muted)">Mode:</span>
    <button class="mode-btn active" data-mode="quiz" onclick="setQuizMode('quiz')">&#x1F4DD; Quiz</button>
    <button class="mode-btn" data-mode="flashcard" onclick="setQuizMode('flashcard')">&#x1F0CF; Flashcards</button>
  </div>
  <div class="flashcard-section" id="flashcardSection">
    <div class="fc-counter" id="fcCounter">Card 1 / ?</div>
    <div class="fc-scene" onclick="flipFlashcard()">
      <div class="fc-card" id="fcCardInner">
        <div class="fc-front" id="fcFront"><p style="color:var(--muted)">Loading...</p></div>
        <div class="fc-back" id="fcBack"></div>
      </div>
    </div>
    <p style="text-align:center;font-size:.72rem;color:var(--muted);margin-bottom:8px">Tap card to flip</p>
    <div class="fc-actions">
      <button class="fc-btn know" onclick="fcMarkKnow()">&#x2705; Got it</button>
      <button class="fc-btn again" onclick="fcMarkAgain()">&#x1F501; Again</button>
    </div>
    <div class="fc-nav">
      <button onclick="fcNav(-1)">&#x2190; Prev</button>
      <button onclick="fcNav(1)">Next &#x2192;</button>
    </div>
  </div>
  <div class="question-card" id="questionCard"></div>
  <div class="score-box">
    <div class="score-num" id="scoreDisplay">0 / 0</div>
    <div class="score-label">Questions Answered Correctly</div>
    <div class="progress-bar-wrap"><div class="progress-bar" id="progressBar" style="width:0%"></div></div>
    <div style="font-size:.78rem;color:var(--muted);margin-top:8px;" id="streakDisplay"></div>
  </div>
  <div class="topic-progress-panel" id="topicProgressPanel"></div>
  <div class="mock-launch-bar">
    <div>
      <p>&#x1F3AF; <strong>Mock Exam Mode</strong> &#x2014; Simulate the real 306A exam with timed questions.</p>
      <div class="score-hist-wrap"><label>&#x1F4C8; Recent Mock Scores:</label><div class="score-hist-list" id="scoreHistoryList"></div></div>
    </div>
    <button class="btn-mock" onclick="openMockSetup()">&#x25B6; Start Mock Exam</button>
  </div>
  <div class="nav-row">
    <button class="nav-btn prev" id="prevBtn" onclick="navigate(-1)" disabled>&#x2190; Prev</button>
    <span id="qCounter" style="font-size:.85rem;color:var(--muted);"></span>
    <button class="nav-btn next" id="nextBtn" onclick="navigate(1)">Next &#x2192;</button>
  </div>
  <!-- AdSense banner placeholder -->
  <div class="concept-section" style="margin-top:24px;">
    <h3>Related Guides</h3>
    <p style="font-size:.88rem;">
      <a href="/how-to-pass-red-seal-306a-exam.html" style="color:var(--primary);font-weight:600;">How to Pass the 306A Exam</a> &#x2014;
      <a href="/306a-sheet-metal-worker-career-canada.html" style="color:var(--primary);font-weight:600;">306A Career Guide</a> &#x2014;
      <a href="/306a-sheet-metal-worker-salary-canada.html" style="color:var(--primary);font-weight:600;">Sheet Metal Salary 2026</a> &#x2014;
      <a href="/what-is-red-seal-certification-canada.html" style="color:var(--primary);font-weight:600;">What Is Red Seal Certification?</a>
    </p>
  </div>
</div>
<!-- MOCK OVERLAY -->
<div class="mock-overlay" id="mockOverlay">
  <div class="mock-panel">
    <div class="mock-head">
      <span style="color:white;font-weight:700;font-size:1rem;">&#x1F3AF; 306A Mock Exam</span>
      <span id="mockTimerDisplay" style="margin-left:auto;color:#f0a500;font-weight:700;font-size:1rem;"></span>
      <button onclick="closeMock()" style="margin-left:16px;background:rgba(255,255,255,.15);border:none;color:white;border-radius:6px;padding:5px 12px;cursor:pointer;font-size:.85rem;">&#x2715; Exit</button>
    </div>
    <div class="mock-bar-wrap"><div class="mock-bar-fill" id="mockBarFill" style="width:0%"></div></div>
    <div class="mock-body" id="mockBody"></div>
  </div>
</div>
<!-- COOKIE CONSENT -->
<div id="cookieBanner" style="display:none;position:fixed;bottom:0;left:0;right:0;background:#1a3a5c;color:white;padding:14px 20px;z-index:999;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
  <span style="font-size:.84rem;">We use cookies to save your study progress. <a href="/privacy.html" style="color:#f0a500;">Privacy Policy</a></span>
  <button onclick="acceptCookies()" style="background:#f0a500;color:#fff;border:none;border-radius:6px;padding:8px 18px;font-weight:700;cursor:pointer;font-size:.84rem;">Accept</button>
</div>
<script>
const MOCK_PAGE_KEY='306a';
const questions=[
'''

Q1_25 = r"""
{id:1,topic:'layout',topicLabel:'Layout & Pattern Development',diff:'easy',text:'Which pattern development method is used to lay out a straight rectangular duct section?',options:['A) Radial line development','B) Parallel line development','C) Triangulation','D) Gore construction'],answer:1,explanation:'Parallel line development is used for prisms (rectangular ducts) and cylinders (round ducts). Lines in the pattern are drawn parallel and equally spaced around the perimeter. Radial line is for cones and pyramids. Triangulation is for transition pieces between different shapes.',keyConcept:'Parallel line development: prisms (rectangular duct) and cylinders (round duct). Lines are parallel. Spacing equals perimeter segments of the cross-section.'},
{id:2,topic:'layout',topicLabel:'Layout & Pattern Development',diff:'medium',text:'A sheet metal worker needs to lay out a pattern for a fitting that transitions from a 12"x12" square duct to a 10" round duct. Which development method is MOST appropriate?',options:['A) Parallel line development — both shapes are straight','B) Radial line development — the round end is conical','C) Triangulation — the fitting connects two different shapes and requires dividing the surface into triangles to find true lengths','D) Gore construction — used for all round-to-square transitions'],answer:2,explanation:'Triangulation is used when connecting two different shapes (rectangle-to-round, offset transitions). The surface is divided into triangles; true lengths of each diagonal are determined and then the triangles are unfolded into a flat pattern. Parallel line only works when both ends are the same shape. Radial line works only for cones and pyramids with a single apex point.',keyConcept:'Triangulation: used for transitions between different shapes (rectangle-to-round, offset). Divide surface into triangles → find true length of each diagonal → unfold to flat pattern.'},
{id:3,topic:'layout',topicLabel:'Layout & Pattern Development',diff:'medium',text:'In pattern development, what is meant by "true length" of a line?',options:['A) The length shown in the front view of the drawing','B) The actual length of a line on the surface of the fitting, as it would appear if unfolded flat — not its projected length in any view','C) The shortest distance between two points on a straight duct','D) The length of the duct centerline from inlet to outlet'],answer:1,explanation:'In orthographic projection, lines that are not parallel to the projection plane appear shorter than they actually are (foreshortened). True length is the actual measurement of a line as it exists on the 3D surface — found by rotating or projecting the line until it is parallel to the projection plane. Using foreshortened lengths produces an incorrect pattern.',keyConcept:'True length: actual length of a line on the fitting surface. Projected views foreshorten angled lines. True length must be found before drawing triangulation patterns or radial line layouts.'},
{id:4,topic:'layout',topicLabel:'Layout & Pattern Development',diff:'medium',text:'When developing the pattern for a right cone using radial line development, what measurement represents the radius of the arc drawn in the pattern?',options:['A) The height of the cone','B) The slant height (true length of the slant side from apex to base circle)','C) The diameter of the cone base','D) The circumference of the cone base divided by pi'],answer:1,explanation:'In radial line development of a cone, all surface lines radiate from the apex. The radius of the arc in the flat pattern equals the slant height — the true length from the apex to the edge of the base circle. The arc length then equals the circumference of the base (2πr). The height of the cone alone is not the slant height.',keyConcept:'Cone pattern radius = slant height (apex to base edge). Arc length in pattern = base circumference. Slant height = √(height² + base_radius²).'},
{id:5,topic:'layout',topicLabel:'Layout & Pattern Development',diff:'hard',text:'A sheet metal worker is developing a pattern for an offset transition fitting — a rectangular duct offset to one side connecting to a round duct. Which sequence correctly describes the triangulation method?',options:['A) Draw the plan and elevation → divide the surfaces into triangles → find the true length of each triangle side → construct the flat pattern triangle by triangle','B) Draw the elevation only → project parallel lines to a stretch-out line → mark off the perimeter','C) Find the apex of the cone → draw radial lines from apex → swing arcs for each section','D) Divide only the round end into segments → project them to the square end directly'],answer:0,explanation:'Triangulation sequence: 1) Draw plan and elevation views. 2) Divide the surface into triangles (diagonals across each face). 3) Find the true length of each line using a true length diagram (rotate each line to horizontal and measure). 4) Draw each triangle in sequence using the true lengths, building the flat pattern triangle by triangle.',keyConcept:'Triangulation steps: plan + elevation → divide into triangles → true length diagram for each line → construct flat pattern triangle by triangle. Every diagonal must have its true length found before use.'},
{id:6,topic:'fabrication',topicLabel:'Sheet Metal Fabrication',diff:'easy',text:'What is the standard galvanized steel sheet gauge used for low-pressure residential HVAC ductwork (1/2" WG pressure class, duct sizes up to 24")?',options:['A) 14 gauge','B) 24 gauge','C) 30 gauge','D) 36 gauge'],answer:1,explanation:'SMACNA specifies 24 gauge galvanized steel for 1/2" WG pressure class ductwork in sizes up to 24". As duct size or pressure class increases, heavier gauges are required. 14 gauge is structural steel — far too heavy for standard ductwork. 30 gauge is too thin for duct construction.',keyConcept:'SMACNA 1/2" WG, duct up to 24": typically 24 gauge galvanized. Heavier gauge required for larger ducts or higher pressure class. Know the SMACNA gauge table by pressure class and size.'},
{id:7,topic:'fabrication',topicLabel:'Sheet Metal Fabrication',diff:'medium',text:'What is a Pittsburgh lock seam and for what application is it primarily used?',options:['A) A double-folded flat seam used on architectural metal roofing','B) A longitudinal seam used to close the long sides of rectangular sheet metal duct sections, made by folding one edge into a pocket and clinching the other edge into it','C) A spiral seam used on round ductwork formed by a spiral pipe machine','D) A cross-seam used to connect two sections of rectangular duct end-to-end'],answer:1,explanation:'The Pittsburgh lock (also called Pittsburgh seam) is the standard longitudinal closing seam for rectangular ducts. One edge is formed into a pocket (the "Pittsburgh pocket"), and the mating flat edge is inserted and then clinched (hammered) closed. It provides a strong, airtight closure along the full length of the duct.',keyConcept:'Pittsburgh lock: longitudinal seam for rectangular duct sides. Pocket formed on one edge, flat edge inserted and clinched. Most common rectangular duct longitudinal seam in HVAC fabrication.'},
{id:8,topic:'fabrication',topicLabel:'Sheet Metal Fabrication',diff:'medium',text:'A grooved seam is commonly used in which application?',options:['A) As the longitudinal seam on rectangular duct','B) As a standing seam on architectural metal roofing','C) As the spiral seam on round duct formed by a spiral pipe machine, or as a hand-formed seam connecting two curved edges','D) As a transverse (cross) connection between rectangular duct sections'],answer:2,explanation:'The grooved seam (or rolled groove seam) is used on round ductwork — particularly the spiral seam formed by a spiral pipe machine — and for connecting two curved edges. Both edges are formed into matching grooves and then rolled together to lock. It creates a smooth, mechanically tight seam without exposed sharp edges.',keyConcept:'Grooved seam: used on round duct (spiral pipe machine) and curved edge connections. Both edges formed into grooves and rolled together. Smooth exterior, tight seal.'},
{id:9,topic:'fabrication',topicLabel:'Sheet Metal Fabrication',diff:'medium',text:'According to SMACNA, pressure class for HVAC ductwork is defined by the maximum static pressure the duct system will operate under. Which of the following correctly lists SMACNA low-pressure classes?',options:['A) Class 1/2, Class 1, Class 2 (in inches of water gauge, WG)','B) Class A, B, C based on material gauge only','C) Class 100, 200, 300 based on CFM airflow','D) Pressure class is not defined by SMACNA — it is determined by the HVAC engineer only'],answer:0,explanation:'SMACNA classifies duct systems by static pressure: 1/2" WG, 1" WG, 2" WG, 3" WG, 4" WG, 6" WG, and 10" WG. The pressure class determines sheet metal gauge, seam types, reinforcement requirements, and joint spacing. Low-pressure residential systems are typically 1/2" or 1" WG.',keyConcept:'SMACNA pressure classes: 1/2, 1, 2, 3, 4, 6, 10 inches WG. Pressure class drives ALL construction decisions: gauge, seam type, reinforcement, joint spacing, sealing class.'},
{id:10,topic:'fabrication',topicLabel:'Sheet Metal Fabrication',diff:'hard',text:'A 24"x24" rectangular duct section is to be installed in a 2" WG positive pressure system. According to SMACNA HVAC Duct Construction Standards, what is the minimum gauge of galvanized steel required?',options:['A) 28 gauge — sufficient for all commercial duct sizes','B) 22 gauge — heavier gauge required for 2" WG class at this duct size','C) 16 gauge — all positive pressure ductwork requires structural gauge','D) 24 gauge — gauge does not change with pressure class'],answer:1,explanation:'SMACNA requires heavier gauge for higher pressure classes and larger duct sizes. At 2" WG pressure class, 24"x24" duct requires 22 gauge galvanized steel. The combination of larger size and higher pressure necessitates thicker metal to resist deformation and maintain structural integrity. Always verify with the current SMACNA table.',keyConcept:'SMACNA gauge selection: depends on BOTH pressure class AND duct size (longest side). Higher pressure or larger size → heavier gauge. 2" WG, 24": typically 22 ga.'},
{id:11,topic:'fabrication',topicLabel:'Sheet Metal Fabrication',diff:'medium',text:'What is the difference between a drive cleat and an S-cleat used in rectangular duct assembly?',options:['A) Drive cleats are used on round duct; S-cleats are for rectangular only','B) A drive cleat is a single-channel cleat hammered onto the end of one duct section to connect it to the next; an S-cleat (or S-slip) slides over both ends of two duct sections to join them','C) They are interchangeable — the choice is based on installer preference only','D) Drive cleats are for high-pressure duct; S-cleats are for low-pressure only'],answer:1,explanation:'Drive cleats (also called drive slips) have one open channel — they are hammered (driven) onto one side of a duct joint, with the other duct end inserted first. S-cleats (S-slips) have two channels — both duct ends slide in from opposite sides of the S. Drive cleats are used on the long sides of rectangular duct joints; S-cleats are used on the short sides.',keyConcept:'Drive cleat: one channel, hammered onto duct end. Used on long duct sides. S-cleat: two channels, both duct ends slide in. Used on short duct sides. Together they form the standard rectangular duct transverse joint.'},
{id:12,topic:'welding',topicLabel:'Welding & Joining',diff:'easy',text:'Which welding process is most commonly used for joining stainless steel sheet metal in HVAC and food service applications?',options:['A) Shielded Metal Arc Welding (SMAW/stick) — best for thin material','B) Gas Tungsten Arc Welding (GTAW/TIG) — produces clean, precise welds on thin stainless steel with minimal heat input','C) Flux-Core Arc Welding (FCAW) — fastest process for sheet metal','D) Oxy-Acetylene welding — preferred for stainless steel because of lower heat'],answer:1,explanation:'GTAW (TIG welding) is the preferred process for stainless steel sheet metal because it provides precise heat control, produces clean welds without spatter, and maintains the corrosion-resistant properties of stainless steel. SMAW and FCAW create too much spatter and heat distortion on thin gauge material. Oxy-acetylene may cause carbide precipitation in stainless steel.',keyConcept:'TIG (GTAW) for stainless sheet metal: precise heat control, no spatter, clean welds, maintains corrosion resistance. Use ER308L filler rod for 304 stainless. Purge back of weld with argon for critical applications.'},
{id:13,topic:'welding',topicLabel:'Welding & Joining',diff:'medium',text:'Resistance spot welding is commonly used in sheet metal fabrication because it:',options:['A) Creates the strongest possible joint for all metal thicknesses','B) Joins two sheets quickly by passing high current through electrode tips, generating localized heat that fuses the sheets at discrete spots — fast, no filler, minimal distortion','C) Requires flux to prevent oxidation at the weld spot','D) Can be used to join galvanized steel to aluminum without any special preparation'],answer:1,explanation:'Spot welding passes high current through copper electrode tips pressed against both sheet surfaces. Resistance heating at the contact point melts and fuses the sheets at discrete spots. Advantages: fast, no filler metal, minimal distortion, no flux. Limitations: only for lap joints, limited penetration, requires electrode access to both sides.',keyConcept:'Spot welding: high current through electrodes → resistance heating → fusion at spot. No filler, fast, minimal distortion. For lap joints only. Galvanized steel generates zinc fumes — use ventilation.'},
{id:14,topic:'welding',topicLabel:'Welding & Joining',diff:'medium',text:'When installing solid rivets to join two sheets of galvanized steel, what preparation is required before driving the rivet?',options:['A) No preparation — rivets self-pierce the sheet metal','B) Drill or punch a hole slightly larger than the rivet diameter, insert the rivet, support the head with a bucking bar, and drive with a rivet gun or hammer to form the shop head','C) Apply flux around the rivet hole to prevent corrosion','D) Heat the rivet to red-hot before inserting to ensure a tight fit'],answer:1,explanation:'Solid rivet installation: 1) Drill/punch hole to correct diameter (typically 1/32" larger than rivet diameter). 2) Insert rivet. 3) Support the factory head with a bucking bar (dolly) held firmly against it. 4) Drive rivet shank with pneumatic rivet gun or hammer to upset (flatten) the shank into a shop head. The resulting compression holds the sheets together.',keyConcept:'Solid rivet: drill hole → insert rivet → buck head → drive shank to form shop head. Hole size = rivet diameter + 1/32". Rivet length: grip (total thickness) + 1.5× rivet diameter for shop head.'},
{id:15,topic:'welding',topicLabel:'Welding & Joining',diff:'hard',text:'A sheet metal worker is TIG welding a 16-gauge (1.6mm) 304 stainless steel duct section. During welding, the area around the weld turns a dark gold/brown/blue colour. What does this indicate and what is the cause?',options:['A) Normal colour — stainless always discolours when welded','B) Heat tint (oxidation) indicating the weld area was exposed to oxygen at elevated temperature — the shielding gas coverage was inadequate or the part cooled too slowly in air','C) The filler rod composition is incorrect for 304 stainless','D) The material is not actually stainless steel — regular carbon steel does not discolour this way'],answer:1,explanation:'Heat tint on stainless steel is caused by chromium oxide formation when the hot metal is exposed to oxygen. Light gold = slightly exposed; blue/grey = significantly oxidized. Heavy heat tint reduces corrosion resistance in that area. Prevention: proper argon shielding gas coverage, sufficient flow rate, correct torch angle, and allowing the weld to cool under shielding gas before moving the torch.',keyConcept:'Stainless heat tint: chromium oxide from O2 exposure while hot. Gold = minor. Blue = significant loss of corrosion resistance. Fix: improve shielding gas coverage, use gas lens, extend post-flow time.'},
{id:16,topic:'hvac',topicLabel:'HVAC Ductwork',diff:'easy',text:'SMACNA defines three duct sealing classes. What does Sealing Class A require?',options:['A) No sealant required — Class A ductwork uses mechanical connections only','B) All transverse joints, longitudinal seams, AND duct wall penetrations must be sealed — the most stringent class','C) Only transverse (cross) joints between duct sections must be sealed','D) Sealing is applied to the exterior of the duct only for condensation control'],answer:1,explanation:'SMACNA Sealing Classes: Class A (most stringent) = all transverse joints, longitudinal seams, AND duct wall penetrations sealed. Class B = all transverse joints and longitudinal seams sealed. Class C (least stringent) = no specific sealing requirement. Class A is required for high-pressure or critical systems.',keyConcept:'SMACNA Sealing Class A: ALL seams + joints + penetrations sealed. Class B: transverse joints + longitudinal seams. Class C: no requirement. Higher pressure class typically requires higher sealing class.'},
{id:17,topic:'hvac',topicLabel:'HVAC Ductwork',diff:'medium',text:'Per SMACNA standards, what is the maximum support spacing for 24-gauge rectangular duct installed horizontally in a low-pressure (1/2" WG) system?',options:['A) 600 mm (2 ft)','B) 2.4 m (8 ft) — SMACNA maximum hanger spacing for standard low-pressure rectangular duct','C) 4.5 m (15 ft)','D) No spacing limit — support is based on engineering judgment only'],answer:1,explanation:'SMACNA HVAC Duct Construction Standards specify maximum hanger spacing of 8 ft (2.4 m) for standard rectangular ductwork at low-pressure class (1/2" WG). Larger or heavier duct, higher pressure class, or seismically active areas may require closer spacing. Hangers must support duct weight without allowing sag that affects airflow.',keyConcept:'SMACNA rectangular duct hanger max spacing: 8 ft (2.4 m) for standard low-pressure duct. Seismic zones, larger/heavier duct may require closer spacing. Use trapeze hangers or strap hangers per SMACNA detail.'},
{id:18,topic:'hvac',topicLabel:'HVAC Ductwork',diff:'medium',text:'When connecting flexible duct to a diffuser or branch collar, what is the maximum permitted length of flexible duct per SMACNA recommendations?',options:['A) No limit — flexible duct can be used as the primary distribution system','B) Maximum 1.8 m (6 ft) fully extended — longer runs cause excessive pressure drop and are not recommended','C) Maximum 6 m (20 ft) if fully supported','D) 300 mm (12 in) only — flexible duct is only for vibration isolation'],answer:1,explanation:'SMACNA limits flexible duct connections to approximately 6 ft (1.8 m) to minimize pressure drop. Flexible duct has significantly higher friction loss per foot than rigid duct due to its corrugated interior surface. It must be installed fully extended (not compressed), properly supported, and at minimum bending radius. Longer flexible runs cause unacceptable pressure drop and airflow reduction.',keyConcept:'Flexible duct: max 6 ft (1.8 m), fully extended, properly supported. Compressed flex = high pressure drop. Use for final connections to diffusers only, not as primary distribution.'},
{id:19,topic:'hvac',topicLabel:'HVAC Ductwork',diff:'medium',text:'What is the purpose of a turning vane installed inside a 90° rectangular duct elbow?',options:['A) To reduce sheet metal gauge requirements at the elbow','B) To guide airflow smoothly around the bend, reducing turbulence, pressure drop, and noise compared to a plain square elbow','C) To balance airflow between multiple branches at the elbow','D) To prevent condensation inside the elbow on humid days'],answer:1,explanation:'A square elbow without turning vanes creates significant turbulence, high pressure drop, and noise as air separates from the outer wall. Turning vanes (sheet metal blades inside the elbow) guide airflow in a smooth arc, reducing separation, pressure drop by up to 75%, and noise. Required by many specifications for critical systems.',keyConcept:'Turning vanes: guide airflow around square elbows. Reduce pressure drop by ~75%, reduce noise. Required in many specifications for low-turbulence airflow. Single-blade or double-blade types.'},
{id:20,topic:'hvac',topicLabel:'HVAC Ductwork',diff:'hard',text:'A sheet metal worker is installing 2" WG positive pressure ductwork and must add reinforcement to a 30" wide rectangular duct section. Per SMACNA, what type of reinforcement is typically required at this size and pressure class?',options:['A) No reinforcement needed — sheet metal gauge is sufficient at 2" WG for 30" duct','B) Intermediate reinforcement angles or T-bars are required at specified intervals to prevent duct wall deflection under positive pressure','C) External wooden strapping every 600 mm','D) Double-layer sheet metal is the only acceptable reinforcement method'],answer:1,explanation:'SMACNA requires intermediate reinforcement (angle iron, T-bars, or formed stiffeners) for wider ductwork at higher pressure classes to prevent wall deflection. A 30" wide duct at 2" WG exceeds the limit where gauge alone is sufficient. Reinforcement is welded or screwed to the duct at intervals specified in the SMACNA table. Deflection causes noise, leakage, and structural failure.',keyConcept:'SMACNA duct reinforcement: required when duct width + pressure class exceeds gauge limits. Options: T-bars, angle iron, formed standing seam stiffeners. Spacing and size per SMACNA table.'},
{id:21,topic:'safety',topicLabel:'Safety & Code',diff:'easy',text:'Under WHMIS (GHS), what does a pictogram showing a flame above an exclamation mark indicate?',options:['A) Explosive material — must not be heated','B) Flammable material — a substance that can ignite and burn at ordinary temperatures or when exposed to heat or spark','C) Corrosive material that causes skin burns','D) Oxidizer that may intensify fires'],answer:1,explanation:'The WHMIS/GHS flame pictogram indicates a flammable hazard — the material can ignite easily. Flammable liquids (flash point <60°C), flammable gases, and flammable solids all use this pictogram. Sheet metal workers encounter flammable materials including solvents, adhesives, and welding gases. An exclamation mark (!) is a separate pictogram for acute toxicity, skin sensitization, etc.',keyConcept:'GHS flame = flammable (liquids, gases, aerosols, solids). Exclamation mark (!) = acute toxicity, irritant, sensitizer. Skull = acute toxicity (severe). Environment = aquatic hazard.'},
{id:22,topic:'safety',topicLabel:'Safety & Code',diff:'medium',text:'A sheet metal worker must install flashing on a roof with a slope greater than 4:12 (18°). What fall protection is typically required when working at this height above ground?',options:['A) No fall protection required if the worker is experienced','B) Personal fall arrest system (PFAS) — harness, lanyard, and anchor point — or guardrails when working at heights exceeding 3 m (10 ft) in most provincial OHS regulations','C) Non-slip footwear is the only requirement on sloped roofs','D) Safety nets are mandatory for all roof work in Canada'],answer:1,explanation:'Provincial OHS regulations generally require fall protection (personal fall arrest system or guardrails) when working at heights of 3 m (10 ft) or greater. On sloped roofs, a PFAS with shock-absorbing lanyard and a properly rated anchor point is required. The anchor must be capable of supporting 22 kN (5,000 lbs) per worker. Non-slip footwear is an additional requirement, not a substitute for fall protection.',keyConcept:'Fall protection: required at heights ≥3 m (most provinces). On slopes ≥4:12: PFAS mandatory. Anchor: minimum 22 kN capacity. Inspect harness before each use. Provincial regulations may vary.'},
{id:23,topic:'safety',topicLabel:'Safety & Code',diff:'easy',text:'When operating sheet metal plasma cutting equipment, which eye protection is required?',options:['A) Clear safety glasses — plasma arc is not bright enough to require darkened lenses','B) Welding shade lens — typically shade #5 to #8 depending on amperage — in a face shield or welding helmet, plus UV protection','C) Standard prescription glasses are sufficient','D) No eye protection required if the operator is behind a screen'],answer:1,explanation:'Plasma cutting generates intense UV and IR radiation similar to arc welding. A welding helmet or face shield with appropriate shade lens (typically #5 to #8 for plasma cutting) is required to prevent arc eye (photokeratitis) and retinal damage. The shade number depends on the cutting amperage — higher amperage requires darker shade.',keyConcept:'Plasma cutting eye protection: welding helmet with shade #5-8 (amperage dependent). UV/IR radiation = arc eye risk. Also: hearing protection (plasma is loud), respiratory protection for fume, leather gloves and jacket.'},
{id:24,topic:'tools',topicLabel:'Tools & Equipment',diff:'easy',text:'What is a throatless shear used for in sheet metal work?',options:['A) Cutting sheet metal only in straight lines','B) Cutting curves, irregular shapes, and inside cuts in sheet metal — the "throatless" design allows the metal to be rotated freely around the blade without the throat of the machine limiting movement','C) Shearing sheet metal to exact widths using a back gauge','D) Punching holes in sheet metal for fastener installation'],answer:1,explanation:'A throatless shear (Beverly shear) has a blade mounted without a limiting throat, so sheet metal can be maneuvered in any direction while cutting. This allows cutting curves, circles, irregular shapes, and inside openings — impossible with a standard straight-bar shear. Essential for pattern work in sheet metal fabrication.',keyConcept:'Throatless shear: cuts curves and irregular shapes. No throat = metal rotates freely. Cannot cut long straight lines efficiently. For curves, circles, inside cuts. Standard shear = straight cuts only.'},
{id:25,topic:'tools',topicLabel:'Tools & Equipment',diff:'medium',text:'A box and pan brake is used for what sheet metal forming operation?',options:['A) Cutting sheet metal to exact lengths only','B) Bending sheet metal to precise angles — the segmented upper beam allows forming U-shapes, boxes, and pans by repositioning fingers to clear previously formed flanges','C) Rolling sheet metal into cylindrical shapes','D) Forming the Pittsburgh lock seam on duct sections'],answer:1,explanation:'A box and pan brake (finger brake) has a segmented upper beam that can be configured to clear flanges already formed on the workpiece. This allows bending multiple sides of a box or pan without removing the previously bent flanges. Individual fingers can be removed to create different-width segments for complex shapes.',keyConcept:'Box and pan brake: segmented upper fingers → clears existing flanges → allows multi-side bending of boxes and pans. Fingers are removable/reconfigurable. Standard press brake cannot form boxes.'}
"""

out = BASE / '306a_temp.html'
out.write_text(HTML_SHELL + Q1_25, encoding='utf-8')
import re
q_count = len(re.findall(r'\bid:\d+', Q1_25))
print(f"Batch 1 written: Q1-{q_count} ({q_count} questions)")
print(f"File: 306a_temp.html ({len(HTML_SHELL)+len(Q1_25):,} chars)")
print("Run create_306a_batch2.py next")
