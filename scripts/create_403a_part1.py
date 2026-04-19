"""
403a.html Quiz - Part 1
Writes the HTML head + styles + nav + header + intro + questions 1-50
Output: 403a_new.html (intermediate file, will be completed by part2)
"""
from pathlib import Path

BASE = Path(__file__).parent.parent

HTML_TOP = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FSSHZMWVLW"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag(\'js\', new Date());
  gtag(\'config\', \'G-FSSHZMWVLW\');
</script>
<meta name="google-site-verification" content="AySEYGsNWhilNyl3EpVTQu6a3p0l6E1ZCe7P0EUN8O8" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Free 403A Red Seal Practice Exam — 100 Questions 2026</title>
<meta name="description" content="Free 403A Gas Fitter Red Seal practice exam. 100 questions: CSA B149.1, gas supply, appliances, venting, combustion theory, safety. Mock Exam + scoring. Canada 2026.">
<meta name="keywords" content="403A Red Seal, Gas Fitter exam Canada, CSA B149.1 practice, natural gas technician exam, 403A practice questions 2026">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://allforyou-bit.github.io/403a.html">
<meta property="og:title" content="403A Gas Fitter – 100 Free Red Seal Practice Questions 2026">
<meta property="og:description" content="Free 403A Red Seal practice quiz — 100 questions covering CSA B149.1, gas supply, appliances, venting, combustion theory and safety. Mock Exam included.">
<meta property="og:url" content="https://allforyou-bit.github.io/403a.html">
<meta property="og:type" content="website">
<meta property="og:image" content="https://allforyou-bit.github.io/favicon.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="403A Gas Fitter – 100 Free Red Seal Practice Questions 2026">
<meta name="twitter:description" content="100 free 403A Red Seal practice questions + Mock Exam mode. CSA B149.1 aligned. Canada\'s top free gas fitter exam prep.">
<meta name="twitter:image" content="https://allforyou-bit.github.io/favicon.svg">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6709396576574623" crossorigin="anonymous"></script>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How many questions are on the 403A Gas Fitter Red Seal exam?","acceptedAnswer":{"@type":"Answer","text":"The 403A Gasfitter (Class A) Red Seal exam contains approximately 100 multiple-choice questions. A minimum score of 70% is required to pass. The exam is based on the current Red Seal Occupational Standard and tests CSA B149.1, combustion theory, gas supply systems, appliance service, venting, and safety."}},{"@type":"Question","name":"What is the hardest topic on the 403A Gas Fitter Red Seal exam?","acceptedAnswer":{"@type":"Answer","text":"The most challenging topics are combustion air calculations (0.08 m\u00b2/kW rule), venting category classification (Cat I\u2013IV), pipe sizing using pressure drop tables, and regulator pressure settings. Understanding CSA B149.1 code application is the key to passing."}},{"@type":"Question","name":"What code governs gas fitting work in Canada?","acceptedAnswer":{"@type":"Answer","text":"CSA B149.1 Natural Gas and Propane Installation Code is Canada\'s primary code for gas fitter work. It covers gas supply systems, piping, appliances, venting, combustion air, and safety requirements."}}]}
</script>
<style>
  :root{--primary:#1a3a5c;--accent:#f0a500;--green:#27ae60;--red:#e74c3c;--light:#f4f7fb;--card:#ffffff;--text:#2c3e50;--muted:#7f8c8d;--border:#dce3ec}
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:\'Segoe UI\',Arial,sans-serif;background:var(--light);color:var(--text)}
  .site-nav{background:#1a3a5c;padding:0 24px;display:flex;gap:18px;align-items:center;flex-wrap:wrap;position:sticky;top:0;z-index:100;box-shadow:0 2px 8px rgba(0,0,0,.18);min-height:52px}
  .site-nav a{color:white;text-decoration:none;font-weight:600;font-size:.88rem;padding:16px 0;display:inline-block}
  .site-nav a:hover,.site-nav a.active{color:#f0a500}
  header{background:var(--primary);color:white;padding:24px 20px 18px;text-align:center}
  header h1{font-size:1.6rem;font-weight:700;margin-bottom:6px}
  header p{font-size:.9rem;opacity:.85}
  .badge{display:inline-block;background:var(--accent);color:#fff;font-size:.72rem;font-weight:700;padding:3px 10px;border-radius:20px;margin-top:8px;letter-spacing:.5px}
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
  .concept-section p{font-size:.88rem;line-height:1.75;color:var(--text);margin-bottom:10px}
  footer{background:var(--primary);color:rgba(255,255,255,.75);text-align:center;padding:20px;font-size:.8rem;margin-top:40px}
  footer a{color:var(--accent);text-decoration:none}
  @media(max-width:600px){header h1{font-size:1.2rem}.tab-btn{font-size:.75rem;padding:7px 12px}.q-text{font-size:.92rem}}
  .mock-launch-bar{display:flex;align-items:center;justify-content:space-between;background:#fff8e1;border:2px solid #f0a500;border-radius:10px;padding:12px 18px;margin-bottom:18px;flex-wrap:wrap;gap:10px}
  .mock-launch-bar p{font-size:.85rem;color:#5d4037;margin:0}
  .mock-launch-bar strong{color:#b7770d}
  .btn-mock{background:#f0a500;color:#fff;border:none;border-radius:8px;padding:10px 22px;font-weight:700;font-size:.88rem;cursor:pointer;display:inline-flex;align-items:center;gap:6px}
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
  .btn-mock-next:hover{background:#2d6a9f}
  .update-pill{display:inline-flex;align-items:center;gap:4px;background:#e8f9ef;color:#1a6636;font-size:.68rem;font-weight:700;padding:3px 9px;border-radius:10px;border:1px solid #a9dfbf;margin-left:8px;vertical-align:middle}
  .rsos-pill{display:inline-flex;align-items:center;gap:4px;background:#eaf0f9;color:#1a3a5c;font-size:.68rem;font-weight:700;padding:3px 9px;border-radius:10px;border:1px solid #afc3dc;margin-left:4px;vertical-align:middle}
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
  .nav-dropdown:hover .nav-drop-menu{display:block}
  .exam-accordion{margin-bottom:20px}
  .exam-accordion summary{cursor:pointer;color:var(--primary);font-weight:700;font-size:.95rem;padding:12px 16px;background:var(--card);border-radius:8px;border-left:4px solid var(--accent);box-shadow:0 1px 5px rgba(0,0,0,.07);list-style:none;display:flex;justify-content:space-between;align-items:center}
  .exam-accordion summary::-webkit-details-marker{display:none}
  .exam-accordion summary::after{content:"\\25BC";font-size:.75rem;opacity:.6;transition:transform .2s}
  .exam-accordion[open] summary::after{transform:rotate(180deg)}
  .exam-accordion .concept-section{border-radius:0 0 8px 8px;margin-top:0;box-shadow:0 2px 6px rgba(0,0,0,.06)}
  @media(max-width:860px){.site-nav{flex-wrap:nowrap!important;padding:0 14px!important;gap:0!important;position:relative}.nav-brand{display:flex;margin-right:auto}.nav-toggle{display:flex;align-items:center;justify-content:center;height:52px}.nav-links{display:none;position:absolute;top:52px;left:0;right:0;background:#1a3a5c;flex-direction:column;z-index:201;box-shadow:0 8px 24px rgba(0,0,0,.35);border-top:1px solid rgba(255,255,255,.1);max-height:75vh;overflow-y:auto;gap:0}.nav-links.open{display:flex}.nav-links a{padding:13px 20px!important;border-bottom:1px solid rgba(255,255,255,.07)!important;font-size:.9rem!important;width:100%;display:block}.topic-tabs{overflow-x:auto;flex-wrap:nowrap!important;-webkit-overflow-scrolling:touch;padding-bottom:6px;scrollbar-width:none}.topic-tabs::-webkit-scrollbar{display:none}.tab-btn{white-space:nowrap;flex-shrink:0}.mode-switch-row{flex-wrap:wrap}.mock-launch-bar{flex-direction:column;align-items:flex-start}.question-card{padding:16px 14px!important}.difficulty-row{flex-wrap:wrap;gap:6px}header h1{font-size:1.25rem}.container{padding:14px 12px}.nav-drop-btn{width:100%;text-align:left;padding:13px 20px!important;border-bottom:1px solid rgba(255,255,255,.07)!important;font-size:.9rem!important}.nav-drop-menu{position:static;box-shadow:none;border-radius:0;padding:0;display:none;background:rgba(255,255,255,.05)}.nav-drop-menu a{padding-left:36px!important}.nav-dropdown.open .nav-drop-menu{display:block}}
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
  <h1>403A Red Seal &#x2014; Gas Fitter (Class A)</h1>
  <p>Canada Certification Exam Practice Questions | 2026</p>
  <span class="badge">Based on 2023 Red Seal Occupational Standard (RSOS)</span>
  <span class="update-pill">&#x2713; Updated Apr 2026</span>
  <span class="rsos-pill">CSA B149.1 / 2023 RSOS Aligned</span>
</header>
<!-- AdSense banner placeholder -->
<div class="container">
  <div class="intro-box">
<h2>About the 403A Red Seal Exam &#x2014; Gas Fitter (Class A)</h2>
<p>The <strong>403A Gasfitter (Class A) Red Seal exam</strong> is Canada\'s national certification for gas fitters working on all types and pressures of natural gas and propane systems. Class A certification covers residential, commercial, and industrial gas installations including high-pressure supply, appliance commissioning, venting design, and combustion analysis.</p>
<p>The exam consists of approximately <strong>100 multiple-choice questions</strong> based on the 2023 Red Seal Occupational Standard (RSOS) and aligned with <strong>CSA B149.1 Natural Gas and Propane Installation Code</strong>, with a passing score of <strong>70%</strong>. Exam time is <strong>3 hours</strong>.</p>
<h3>Topic Breakdown (2023 RSOS)</h3>
<ul>
  <li><strong>Appliances &amp; Combustion Equipment (~22%)</strong> &#x2014; Furnaces, boilers, water heaters, unit heaters, infrared heaters. Burner adjustment, heat exchanger inspection, ignition systems, and commissioning.</li>
  <li><strong>Gas Supply Systems (~18%)</strong> &#x2014; Meter sets, regulators (service, line, appliance), pressure testing, odourant, and first/second stage regulation.</li>
  <li><strong>Piping Systems (~16%)</strong> &#x2014; Pipe sizing using pressure drop tables, pipe materials (black steel, CSST, copper, PE), fittings, supports, and leak detection.</li>
  <li><strong>Venting Systems (~16%)</strong> &#x2014; Category I&#x2013;IV venting, natural/induced/direct vent, common vent sizing, termination clearances.</li>
  <li><strong>Combustion Theory &amp; Air (~14%)</strong> &#x2014; Stoichiometric combustion, excess air, CO/CO&#x2082; analysis, combustion air requirements (0.08 m&#xB2;/kW).</li>
  <li><strong>Safety, Codes &amp; Regulations (~14%)</strong> &#x2014; CSA B149.1, provincial requirements, permits, pressure testing, gas leak response, purging.</li>
</ul>
<h3>How to Use This Practice Tool</h3>
<p>This free tool includes <strong>100 questions</strong> covering all 403A topic blocks with full explanations citing the relevant CSA B149.1 section for every answer. Use <strong>Topic Filter</strong> to drill your weakest areas. Run the <strong>Mock Exam</strong> to simulate the real 100-question timed format.</p>
<p>Related reading: <a href="/how-to-pass-red-seal-403a-exam.html">How to Pass the 403A Red Seal Exam</a> | <a href="/403a-gas-fitter-salary-canada.html">Gas Fitter Salary Guide</a> | <a href="/403a-gas-fitter-career-canada.html">Gas Fitter Career Guide Canada</a></p>
</div>
  <details class="exam-accordion">
    <summary>Exam Structure &#x2014; Topic Breakdown</summary>
    <div class="concept-section">
    <h3>Exam Structure &#x2014; Topic Breakdown</h3>
    <table class="structure-table">
      <tr><th>Block</th><th>Topic</th><th>Approx. Questions</th></tr>
      <tr><td>A</td><td>Appliances &amp; Combustion Equipment</td><td>22</td></tr>
      <tr><td>B</td><td>Gas Supply Systems</td><td>18</td></tr>
      <tr><td>C</td><td>Piping Systems</td><td>16</td></tr>
      <tr><td>D</td><td>Venting Systems</td><td>16</td></tr>
      <tr><td>E</td><td>Combustion Theory &amp; Air</td><td>14</td></tr>
      <tr><td>F</td><td>Safety, Codes &amp; Regulations</td><td>14</td></tr>
    </table>
    <p style="font-size:.8rem;color:var(--muted);margin-top:6px;">* Approximate distribution. Passing score: 70%. Code: CSA B149.1.</p>
  </div>
  </details>
  <div style="display:flex;gap:10px;margin-bottom:18px;flex-wrap:wrap;">
    <button disabled style="background:#95a5a6;color:#fff;border:none;border-radius:8px;padding:9px 18px;font-size:.82rem;font-weight:700;cursor:not-allowed;display:inline-flex;align-items:center;gap:6px">&#x1F4C4; Study Sheet &#x2014; Coming Soon</button>
  </div>
  <div class="topic-tabs" id="topicTabs">
    <button class="tab-btn active" onclick="setTopic(\'all\',this)">All Topics</button>
    <button class="tab-btn" onclick="setTopic(\'appliance\',this)">Appliances</button>
    <button class="tab-btn" onclick="setTopic(\'supply\',this)">Gas Supply</button>
    <button class="tab-btn" onclick="setTopic(\'piping\',this)">Piping</button>
    <button class="tab-btn" onclick="setTopic(\'venting\',this)">Venting</button>
    <button class="tab-btn" onclick="setTopic(\'combustion\',this)">Combustion</button>
    <button class="tab-btn" onclick="setTopic(\'safety\',this)">Safety &amp; Code</button>
    <button class="tab-btn wrong-tab-btn" id="wrongBankTabBtn" onclick="setTopic(\'wrongbank\',this)">&#x1F4D5; Mistakes (0)</button>
  </div>
  <div class="difficulty-row">
    <span>Difficulty:</span>
    <button class="diff-btn easy active" onclick="setDiff(\'all\',this)">All</button>
    <button class="diff-btn easy" onclick="setDiff(\'easy\',this)">Easy</button>
    <button class="diff-btn medium" onclick="setDiff(\'medium\',this)">Medium</button>
    <button class="diff-btn hard" onclick="setDiff(\'hard\',this)">Hard</button>
  </div>
  <div class="mode-switch-row">
    <span style="font-size:.82rem;font-weight:700;color:var(--muted)">Mode:</span>
    <button class="mode-btn active" data-mode="quiz" onclick="setQuizMode(\'quiz\')">&#x1F4DD; Quiz</button>
    <button class="mode-btn" data-mode="flashcard" onclick="setQuizMode(\'flashcard\')">&#x1F0CF; Flashcards</button>
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
      <p>&#x1F3AF; <strong>Mock Exam Mode</strong> &#x2014; Simulate the real 403A exam with timed questions.</p>
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
      <a href="/how-to-pass-red-seal-403a-exam.html" style="color:var(--primary);font-weight:600;">How to Pass the 403A Exam</a> &#x2014;
      <a href="/403a-gas-fitter-career-canada.html" style="color:var(--primary);font-weight:600;">403A Gas Fitter Career Guide</a> &#x2014;
      <a href="/403a-gas-fitter-salary-canada.html" style="color:var(--primary);font-weight:600;">Gas Fitter Salary 2026</a> &#x2014;
      <a href="/what-is-red-seal-certification-canada.html" style="color:var(--primary);font-weight:600;">What Is Red Seal Certification?</a>
    </p>
  </div>
</div>
<!-- MOCK OVERLAY -->
<div class="mock-overlay" id="mockOverlay">
  <div class="mock-panel">
    <div class="mock-head">
      <span style="color:white;font-weight:700;font-size:1rem;">&#x1F3AF; 403A Mock Exam</span>
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
(function(){
  var t=document.createElement(\'div\');t.id=\'comboToast\';
  t.style.cssText=\'position:fixed;bottom:90px;left:50%;transform:translateX(-50%) scale(.85);background:linear-gradient(135deg,#ff6b35,#f0a500);color:white;padding:12px 26px;border-radius:30px;font-weight:800;font-size:1rem;z-index:9999;opacity:0;transition:opacity .25s,transform .25s;pointer-events:none;white-space:nowrap;box-shadow:0 4px 20px rgba(255,107,53,.45)\';
  document.body.appendChild(t);
  var r=document.createElement(\'div\');r.style.cssText=\'text-align:right;max-width:820px;margin:-4px auto 8px;padding:0 8px\';
  r.innerHTML=\'<button onclick="reportQuestion()" style="background:none;border:none;color:#b0bec5;font-size:.75rem;cursor:pointer;padding:4px 8px;font-family:inherit">&#x26D4; Report issue</button>\';
  var qc=document.getElementById(\'questionCard\');if(qc&&qc.parentNode)qc.parentNode.insertBefore(r,qc.nextSibling);
})();
window._cs=0;
function showComboToast(n){var t=document.getElementById(\'comboToast\');if(!t)return;t.textContent=(n>=5?\'\\uD83D\\uDD25\\uD83D\\uDD25 \':\' \\uD83D\\uDD25 \')+n+\' in a row!\';t.style.opacity=\'1\';t.style.transform=\'translateX(-50%) scale(1)\';clearTimeout(t._tmr);t._tmr=setTimeout(function(){t.style.opacity=\'0\';t.style.transform=\'translateX(-50%) scale(.85)\';},2200);}
function reportQuestion(){var el=document.getElementById(\'qText\')||document.querySelector(\'.q-text\');var qt=el?el.textContent.trim():\'Unknown\';window.open(\'mailto:lidbil515@gmail.com?subject=\'+encodeURIComponent(\'Question Error Report\')+\'&body=\'+encodeURIComponent(\'Question: \'+qt+\'\\n\\nDescribe the error:\'));}
</script>
<script>
const MOCK_PAGE_KEY=\'403a\';
const questions=[
'''

# Questions 1-50
QUESTIONS_1_50 = r"""
// ── APPLIANCES (1-22) ──
{id:1,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'easy',text:'What is the primary function of a thermocouple in a standing pilot gas appliance?',options:['A) To regulate gas pressure to the burner','B) To generate a small voltage that keeps the pilot safety valve open when the pilot flame is present','C) To ignite the main burner automatically','D) To modulate the main burner flame'],answer:1,explanation:'A thermocouple generates millivolts when heated by the pilot flame. This voltage holds the pilot safety valve (electromagnet) open. If the pilot extinguishes, voltage drops and the valve closes, shutting off gas to both pilot and main burner.',keyConcept:'Thermocouple: pilot flame heats junction → generates millivolts → holds safety valve open. Pilot out = no voltage = valve closes = gas off.'},
{id:2,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'easy',text:'What does AFUE stand for and what does it measure?',options:['A) Actual Fuel Utilization Efficiency — measures pilot flame size','B) Annual Fuel Utilization Efficiency — measures what percentage of fuel energy is converted to useful heat over a heating season','C) Adjusted Furnace Unit Efficiency — measures the BTU output at the flue','D) Average Flue Utilization Efficiency — measures stack temperature'],answer:1,explanation:'AFUE (Annual Fuel Utilization Efficiency) is the standard measure of furnace efficiency. An 80% AFUE furnace converts 80% of fuel energy to heat; 20% is lost through flue gases. High-efficiency condensing furnaces achieve 90–98% AFUE.',keyConcept:'AFUE: % of fuel energy converted to heat annually. 80% AFUE = 20% flue loss. High-efficiency (condensing) furnaces: 90–98% AFUE.'},
{id:3,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'easy',text:'What is the difference between an atmospheric (natural draft) water heater and a power-vent water heater?',options:['A) Atmospheric uses electricity; power-vent uses natural gas','B) Atmospheric relies on buoyancy of hot flue gases to vent; power-vent uses a blower to force flue gases out through a horizontal PVC pipe','C) Power-vent is always more efficient than atmospheric','D) Atmospheric vents horizontally; power-vent vents vertically only'],answer:1,explanation:'Atmospheric (natural draft) water heaters rely on the buoyancy of hot combustion gases rising through a B-vent to the exterior. Power-vent units use a blower motor to push flue gases through smaller-diameter PVC vent pipes horizontally or vertically, allowing installation without a chimney.',keyConcept:'Atmospheric: hot gases rise through B-vent (buoyancy). Power-vent: blower + PVC horizontal vent. Power-vent allows installation away from chimney.'},
{id:4,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'What is a hot surface ignitor (HSI) and how does it work in a modern gas furnace?',options:['A) A spark ignitor that creates a high-voltage arc to light the burner','B) A silicon carbide or silicon nitride element that glows red-hot when energized, igniting the gas burner on contact','C) A pilot burner that remains lit continuously between heating cycles','D) A UV flame sensor that monitors the main burner flame'],answer:1,explanation:'HSI (hot surface ignitor) is made of silicon carbide or silicon nitride. The control board energizes it for a warm-up period (15-30 seconds), then opens the gas valve. The glowing element ignites the gas. HSI replaced standing pilots in mid-efficiency and high-efficiency furnaces.',keyConcept:'HSI: electric element heats to ~1000°C → ignites gas on contact. Fragile — do not touch ceramic element. Check with amp clamp: typically 3-6A draw.'},
{id:5,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'What is the purpose of a combination gas valve on a residential furnace?',options:['A) To combine natural gas and propane in a dual-fuel system','B) To integrate multiple functions: manual shutoff, pressure regulator, redundant safety valves (redundant design), and main burner valve in a single assembly','C) To mix combustion air with gas before the burner','D) To combine the pilot and main burner gas supply lines'],answer:1,explanation:'A combination gas valve (also called a multifunctional gas valve) contains: manual shutoff, inlet/outlet pressure regulation, redundant automatic safety valves (two solenoids in series), and sometimes a pilot solenoid — all in one unit. Redundant design ensures gas shuts off even if one solenoid fails.',keyConcept:'Combination gas valve: manual shutoff + regulator + two safety solenoids in one unit. Redundant = two solenoids must both open for gas to flow.'},
{id:6,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'A high-efficiency condensing furnace produces liquid condensate that drains from the heat exchanger. What is special about this condensate?',options:['A) It is pure water that can be discharged anywhere','B) It is slightly acidic (pH 3-4) due to carbonic and sulfurous acids and may require a neutralizer before discharging to certain drains','C) It is alkaline and must be diluted before discharge','D) It contains natural gas byproducts and is considered hazardous waste'],answer:1,explanation:'Condensing furnaces extract so much heat that flue gases cool below the dew point, producing liquid condensate. The condensate contains carbonic acid (CO2 + H2O) and sulfurous acid, making it acidic (pH 3-4). Many municipalities require a condensate neutralizer before discharging to copper or cast iron drain systems.',keyConcept:'Condensing furnace condensate: acidic (pH 3-4) from carbonic/sulfurous acids. May require neutralizer — check local code. Drain to floor drain or condensate pump.'},
{id:7,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'What is the purpose of an inducer (induced draft) motor on a mid-efficiency or high-efficiency gas furnace?',options:['A) To supply combustion air to the burner before ignition','B) To pull combustion gases through the heat exchanger and push them out the flue pipe, creating negative pressure in the heat exchanger','C) To circulate conditioned air through the building duct system','D) To induce a draft in the chimney by heating the flue pipe'],answer:1,explanation:'The inducer fan draws combustion gases through the heat exchanger and forces them out the vent pipe. It creates negative pressure in the heat exchanger, ensuring complete flue gas evacuation and allowing use of smaller-diameter vent pipes. A pressure switch verifies inducer is running before allowing ignition.',keyConcept:'Inducer motor: pulls flue gases through heat exchanger → negative pressure → smaller vent pipe allowed. Draft proving switch confirms operation before ignition.'},
{id:8,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'What is the rollout limit switch on a gas furnace and what does it detect?',options:['A) A safety limit on the heat exchanger that detects overheating','B) A safety device that detects flame rollout — flames escaping the burner compartment — and shuts off the gas valve','C) A switch that prevents the inducer from reversing direction','D) A limit switch that cuts power if the furnace tips over'],answer:1,explanation:'Rollout limit switches are mounted at the burner compartment opening. If flames "roll out" of the burner (due to cracked heat exchanger, blocked flue, or pressure reversal), the thermal element opens and shuts off the gas. Rollout switches are often manual-reset for safety.',keyConcept:'Rollout limit: detects flames escaping burner compartment. Causes: cracked heat exchanger, blocked flue, restricted combustion air. Manual-reset — investigate root cause before resetting.'},
{id:9,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'When installing a gas-fired unit heater in a commercial space, what minimum clearance to combustibles is typically required above the unit?',options:['A) 150 mm (6 in)','B) 300 mm (12 in)','C) As specified on the appliance rating plate — clearances vary by model','D) No clearance required if a heat shield is installed'],answer:2,explanation:'Clearances to combustibles for gas appliances are specified on the appliance rating plate (data plate) and in the manufacturer\'s installation manual. These clearances vary by model and output rating. Always follow the rating plate — code requires installation per manufacturer\'s instructions.',keyConcept:'Appliance clearances: always check the rating plate (data plate) on the appliance. Rating plate clearances are code-required minimums and override general guidelines.'},
{id:10,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'What type of venting is required for a Category I gas appliance?',options:['A) Category I requires positive pressure PVC venting','B) Category I appliances use Type B (double-wall metal) vent or masonry chimney — natural draft, non-positive pressure, flue gas temperature above dew point','C) Category I appliances require direct vent (sealed combustion) only','D) Category I uses single-wall metal flue pipe only'],answer:1,explanation:'Category I appliances operate with non-positive vent static pressure and produce flue gas above its dew point temperature. They vent using natural draft through Type B double-wall metal vent or a listed masonry chimney. Examples: 80% AFUE furnaces, atmospheric water heaters.',keyConcept:'Category I: non-positive pressure, above dew point. Vent with Type B metal vent or masonry chimney. Natural draft. Examples: 80% furnace, atmospheric water heater.'},
{id:11,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'What is the purpose of a dip tube in a gas storage water heater?',options:['A) To protect the anode rod from sediment','B) To direct cold inlet water to the bottom of the tank, preventing mixing with hot water at the top','C) To connect the T&P relief valve to the drain','D) To measure water level inside the tank'],answer:1,explanation:'The dip tube is a plastic tube that extends from the cold water inlet at the top of the tank down to near the bottom. Cold incoming water is delivered to the bottom where it can be heated. Without a dip tube, cold and hot water would mix at the top, reducing efficiency and hot water delivery.',keyConcept:'Dip tube: directs cold water to tank bottom → prevents mixing with hot water at top → ensures hot water available at outlet. A broken dip tube causes short cycling of hot water.'},
{id:12,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'A gas dryer venting system must terminate where?',options:['A) Into the attic space to reduce moisture in the house','B) To the exterior of the building — never into an attic, crawlspace, or wall cavity','C) Into a laundry room if it has a window','D) Into an approved lint trap inside the building'],answer:1,explanation:'Gas dryer exhaust contains moisture, heat, lint, and combustion gases (CO). CSA B149.1 and building codes require all gas dryer venting to terminate at the exterior of the building. Venting into enclosed spaces creates fire hazard (lint), moisture damage, and CO poisoning risk.',keyConcept:'Gas dryer venting: must terminate at exterior. Never vent into attic, crawlspace, garage, or wall cavity. Maximum 45° elbows, minimum 4" duct, backdraft damper at termination.'},
{id:13,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'What is the function of an aquastat on a hot water boiler?',options:['A) To measure water flow rate through the boiler','B) To monitor and control boiler water temperature — shutting off the burner when water reaches setpoint and allowing re-ignition when temperature drops','C) To test water quality in the boiler system','D) To control zone valves in a multi-zone system'],answer:1,explanation:'An aquastat (aquathermostat) is a temperature controller immersed in or clamped to the boiler water. It has high-limit and low-limit settings: the high limit shuts off the burner if water exceeds safe temperature; the low limit maintains minimum water temperature for domestic hot water priority.',keyConcept:'Aquastat: boiler water temperature controller. High limit: shuts burner at max temp. Low limit: maintains minimum temp for DHW or circulation.'},
{id:14,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'A direct-vent (sealed combustion) gas appliance draws combustion air from where?',options:['A) From the building interior through a grille on the appliance','B) From the exterior through a dedicated sealed combustion air pipe, completely isolated from interior air','C) From the furnace room through a draft hood','D) From a combination of interior and exterior air'],answer:1,explanation:'Direct-vent (sealed combustion) appliances use a two-pipe system: one pipe draws combustion air from outside, and the other exhausts flue gases to outside. The combustion process is completely isolated from the building interior, making them ideal for tight buildings and eliminating combustion air requirements.',keyConcept:'Direct-vent (sealed combustion): combustion air from exterior, flue to exterior — two-pipe system. No interior combustion air needed. Ideal for tight/energy-efficient buildings.'},
{id:15,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'hard',text:'A gas technician finds that the high-efficiency furnace heat exchanger has a crack. What is the MOST significant danger and the correct action?',options:['A) Reduced efficiency — replace the heat exchanger at next maintenance','B) Carbon monoxide contamination of circulating air — immediately shut down the furnace, tag it out, and advise the homeowner not to operate it until repaired','C) Gas leak risk — check for gas smell and ventilate','D) Condensate leakage — seal the crack with high-temperature sealant'],answer:1,explanation:'A cracked heat exchanger allows combustion gases (including CO) to mix with the circulating air supply. CO is odourless and toxic — it can reach dangerous levels in the building quickly. The technician must immediately shut down the furnace, tag it out of service, advise the occupants, and the unit must not operate until the heat exchanger is replaced.',keyConcept:'Cracked heat exchanger = CO contamination of air supply. IMMEDIATE shutdown required. Tag out. Advise occupants of CO risk. Must not operate until heat exchanger is replaced.'},
{id:16,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'hard',text:'A condensing boiler is installed with a return water temperature of 38°C (100°F). What is the implication of this return temperature?',options:['A) The boiler is inefficient — return temperature must be above 60°C','B) The low return temperature enables condensing operation, which extracts latent heat from flue gases and achieves the highest efficiency (90%+ AFUE)','C) Return temperature is too low — the boiler will short-cycle','D) Low return temperature causes carbonic acid corrosion of the heat exchanger'],answer:1,explanation:'Condensing boilers are designed to operate at low return water temperatures (below 55°C/130°F). At low temperatures, the flue gases cool below their dew point and condense, releasing latent heat. This is the condensing effect — extracting extra energy from the fuel. High return temps prevent condensing and reduce efficiency to non-condensing levels.',keyConcept:'Condensing boiler: low return water temp (<55°C) → flue gases condense → latent heat recovery → 90-98% AFUE. High return temp = no condensing = reduced efficiency.'},
{id:17,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'hard',text:'During commissioning of a new gas furnace, the technician measures a CO reading of 200 ppm in the undiluted flue gas. What does this indicate?',options:['A) Normal — 200 ppm in flue gas is acceptable for residential furnaces','B) Incomplete combustion — high CO indicates insufficient air, incorrect gas pressure, or heat exchanger restriction. Investigate before leaving the appliance running','C) The CO detector is malfunctioning — CO should never be present in flue gas','D) The furnace is operating normally in high-fire mode'],answer:1,explanation:'For residential gas furnaces, acceptable CO in undiluted flue gas is typically below 100 ppm (some standards allow up to 400 ppm, but best practice targets <100 ppm). A reading of 200 ppm indicates incomplete combustion caused by insufficient combustion air, incorrect gas pressure, or heat exchanger restriction. Investigate before leaving.',keyConcept:'CO in flue gas: target <100 ppm, investigate >200 ppm. Causes: low combustion air, high gas pressure, dirty burner, cracked heat exchanger. Measure undiluted flue gas with combustion analyzer.'},
{id:18,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'hard',text:'A 403A gas fitter is commissioning a new gas boiler. What is the correct sequence for commissioning?',options:['A) Light appliance → check gas pressure → test safety controls → check combustion','B) Verify gas supply pressure → purge piping → light appliance → check burner pressure → verify controls → combustion analysis → document results','C) Check combustion first, then adjust controls → verify gas supply','D) Test safety controls → light appliance → purge piping → check pressure'],answer:1,explanation:'Proper commissioning sequence: 1) Verify supply gas pressure, 2) Inspect and purge new piping, 3) Light appliance per manufacturer instructions, 4) Verify manifold/burner pressure, 5) Verify all safety controls (high limit, pressure switches), 6) Conduct combustion analysis (CO2, O2, CO, flue temp), 7) Document all readings. Always follow manufacturer commissioning checklist.',keyConcept:'Commissioning sequence: supply pressure → purge → ignite → burner pressure → safety controls → combustion analysis → document. Never skip combustion analysis on first start.'},
{id:19,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'hard',text:'A gas appliance rating plate states "Input: 100,000 BTU/h, AFUE: 80%". What is the useful heat output?',options:['A) 100,000 BTU/h — all input is usable heat','B) 80,000 BTU/h — 80% of input is converted to useful heat','C) 120,000 BTU/h — efficiency multiplies the input','D) 60,000 BTU/h — safety factor reduces output'],answer:1,explanation:'AFUE of 80% means 80% of fuel energy is converted to heat delivered to the space. Output = Input × AFUE = 100,000 × 0.80 = 80,000 BTU/h. The remaining 20,000 BTU/h (20%) is lost through the flue.',keyConcept:'Heat output = Input BTU/h × AFUE%. 100,000 BTU/h × 80% = 80,000 BTU/h useful heat. 20,000 BTU/h flue loss.'},
{id:20,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'What is the purpose of a gas fireplace pilot orifice vs. the main burner orifice?',options:['A) They are the same size — no difference','B) The pilot orifice is much smaller than the main burner orifice, metering a very small flow of gas to maintain a continuous small pilot flame','C) The pilot orifice is larger to ensure reliable ignition of the main burner','D) Main burner orifice is adjustable; pilot orifice is fixed'],answer:1,explanation:'Gas orifices are precision-drilled holes that meter gas flow to produce the correct BTU output. The pilot orifice is very small (typically 0.012"-0.020" diameter) for a small continuous flame. Main burner orifices are larger and sized for the appliance BTU rating.',keyConcept:'Orifice size = gas flow rate = BTU output. Pilot orifice: very small (0.3-0.5mm). Main burner: larger, sized for BTU rating. Orifice size determines whether NG or LP use — never interchange.'},
{id:21,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'What is the difference between an intermittent pilot (IPI) and a direct spark ignition (DSI) system?',options:['A) IPI uses a standing pilot; DSI uses a hot surface ignitor','B) IPI lights a pilot flame for each call for heat, then the pilot ignites the main burner; DSI uses a spark to ignite the main burner directly without a pilot','C) They are identical ignition systems with different names','D) IPI is for high-efficiency furnaces only; DSI is for boilers only'],answer:1,explanation:'IPI (Intermittent Pilot Ignition): a spark creates a pilot flame at the start of each heat cycle; the flame sensor confirms pilot is lit, then the main gas valve opens. DSI (Direct Spark Ignition): the spark fires directly at the main burner without a pilot. DSI is faster but requires the spark to be at the burner.',keyConcept:'IPI: spark → pilot flame → flame proven → main valve opens. DSI: spark fires directly at main burner (no pilot). Both eliminate standing pilots and save fuel.'},
{id:22,topic:'appliance',topicLabel:'Appliances & Equipment',diff:'medium',text:'What is a B-vent (Type B double-wall metal vent) designed for?',options:['A) Direct vent appliances requiring sealed combustion air','B) Category I and II natural draft gas appliances — designed to maintain warm flue gas temperature to prevent condensation inside the vent','C) Category IV positive-pressure condensing appliances','D) Commercial high-pressure gas appliances only'],answer:1,explanation:'Type B double-wall metal vent (B-vent) consists of an inner aluminum liner and outer galvanized steel shell with air space insulation. The insulated design keeps inner wall warm, preventing condensation of flue gases and maintaining draft. Used for natural draft Category I gas appliances.',keyConcept:'B-vent (Type B): double-wall insulated metal vent for natural draft Category I gas appliances. Keeps flue gas warm → prevents condensation. Not for sealed combustion or positive-pressure appliances.'},
// ── GAS SUPPLY (23-40) ──
{id:23,topic:'supply',topicLabel:'Gas Supply Systems',diff:'easy',text:'What is the specific gravity of natural gas (methane) relative to air?',options:['A) 1.52 — heavier than air','B) 0.55 — lighter than air','C) 1.00 — equal to air','D) 2.01 — much heavier than air'],answer:1,explanation:'Natural gas (primarily methane, CH4) has a specific gravity of approximately 0.55 relative to air. Being lighter than air, it rises and disperses upward if leaked. This is why natural gas detectors are mounted near the ceiling. In contrast, propane (SG=1.52) is heavier and settles in low areas.',keyConcept:'Natural gas SG: ~0.55 (lighter than air) → rises and disperses upward. Propane SG: ~1.52 (heavier than air) → settles in low areas. This determines detector placement.'},
{id:24,topic:'supply',topicLabel:'Gas Supply Systems',diff:'easy',text:'What is the standard low-pressure natural gas outlet pressure from a service regulator to a residential building?',options:['A) 3.5 in WC (0.87 kPa)','B) 7 in WC (1.75 kPa)','C) 14 in WC (3.5 kPa)','D) 2 psig (13.8 kPa)'],answer:1,explanation:'The standard residential natural gas service pressure (low pressure) is approximately 7 inches of water column (7 in WC or 1.75 kPa). This is the outlet pressure from the service regulator at the meter set. Most residential appliances operate at this pressure, then further reduced by an appliance regulator if needed.',keyConcept:'Residential NG supply pressure: 7 in WC (1.75 kPa). Appliance inlet pressure: typically 3.5 in WC (0.87 kPa) for most NG appliances. LP gas: 11 in WC (2.74 kPa).'},
{id:25,topic:'supply',topicLabel:'Gas Supply Systems',diff:'easy',text:'Approximately how many BTU of heat are in one cubic foot of natural gas?',options:['A) 500 BTU/ft³','B) 1,000 BTU/ft³','C) 2,500 BTU/ft³','D) 5,000 BTU/ft³'],answer:1,explanation:'Natural gas has an energy content of approximately 1,000 BTU per cubic foot (higher heating value). This is a fundamental value for pipe sizing, appliance sizing, and combustion calculations. Propane contains approximately 2,500 BTU per cubic foot (as gas).',keyConcept:'Natural gas: ~1,000 BTU/ft³ (or 37 MJ/m³). Propane: ~2,500 BTU/ft³. Use energy content to convert appliance BTU/h rating to gas flow rate (ft³/h).'},
{id:26,topic:'supply',topicLabel:'Gas Supply Systems',diff:'medium',text:'What is "lockup pressure" for a gas regulator and why is it important?',options:['A) The minimum inlet pressure for the regulator to open','B) The outlet pressure when gas flow is zero (no-flow condition) — should not exceed the design working pressure of the downstream system','C) The pressure at which the regulator lock-out valve activates','D) The maximum inlet pressure the regulator can handle'],answer:1,explanation:'Lockup pressure is the outlet pressure of a regulator when downstream demand is zero (all appliances off, valves closed). CSA B149.1 requires lockup pressure not to exceed the maximum allowable pressure for the downstream piping and appliances. Typical lockup: 125% of setpoint.',keyConcept:'Lockup pressure: regulator outlet pressure at zero flow. Should be ≤ max allowable downstream pressure. Typically 125% of set pressure. Verify during commissioning with all valves closed.'},
{id:27,topic:'supply',topicLabel:'Gas Supply Systems',diff:'medium',text:'What is the purpose of an excess flow valve (EFV) in a gas service?',options:['A) To prevent excess pressure from reaching the building','B) To automatically close when gas flow exceeds a set threshold, such as during a pipe break or major leak','C) To limit the gas meter flow rate to the billing maximum','D) To prevent reverse flow into the distribution main'],answer:1,explanation:'Excess flow valves (EFVs) are installed in the service line to automatically shut off gas flow if the flow rate exceeds a set threshold (e.g., from a broken service line). They protect against major leaks downstream. EFVs are required in new residential services in many jurisdictions.',keyConcept:'EFV: automatically closes when flow exceeds threshold → protects against broken pipes. Installed in service line at property line or curb box. May need manual reset after closing.'},
{id:28,topic:'supply',topicLabel:'Gas Supply Systems',diff:'medium',text:'A gas meter is rated for a maximum capacity of 250 ft³/h. The total connected load for the building is 400,000 BTU/h of natural gas appliances. Is the meter adequate?',options:['A) Yes — 250 ft³/h is always sufficient for residential use','B) No — 400,000 BTU/h ÷ 1,000 BTU/ft³ = 400 ft³/h required, which exceeds the meter capacity of 250 ft³/h','C) Yes — connected load does not equal actual demand','D) Cannot determine without knowing the number of appliances'],answer:1,explanation:'To check meter adequacy: convert BTU/h to ft³/h by dividing by 1,000 (BTU/ft³). 400,000 BTU/h ÷ 1,000 = 400 ft³/h. The meter at 250 ft³/h capacity is insufficient. A larger meter (e.g., 400 ft³/h or larger) is required. Note: diversity factor may apply for large installations.',keyConcept:'Meter sizing: BTU/h ÷ 1,000 BTU/ft³ = ft³/h required. Compare to meter capacity. Upgrade if required flow exceeds meter rating.'},
{id:29,topic:'supply',topicLabel:'Gas Supply Systems',diff:'medium',text:'What is the difference between a service regulator and an appliance regulator?',options:['A) Service regulators are indoors; appliance regulators are outdoors','B) Service regulator: reduces high distribution pressure to service pressure (~7 in WC); appliance regulator: further reduces service pressure to appliance inlet pressure (~3.5 in WC)','C) They are interchangeable and perform the same function','D) Appliance regulators handle higher pressures than service regulators'],answer:1,explanation:'Service regulators (at the meter set) reduce gas utility distribution pressure to standard service pressure (~7 in WC / 1.75 kPa for NG). Appliance regulators (built into appliances or installed on the supply) further reduce service pressure to the burner inlet pressure specified by the appliance manufacturer.',keyConcept:'Two-stage regulation: Service regulator → 7 in WC. Appliance regulator → 3.5 in WC (NG) or 11 in WC (LP). Each stage provides pressure stability and safety.'},
{id:30,topic:'supply',topicLabel:'Gas Supply Systems',diff:'medium',text:'What odourant is added to natural gas and why?',options:['A) Mercaptan (ethyl mercaptan/THT) is added because natural gas is naturally odourless and the odourant provides warning of leaks','B) Natural gas naturally smells like rotten eggs — no additive required','C) Carbon monoxide is added to give gas a detectable smell','D) The odour comes from sulfur in the natural gas itself'],answer:1,explanation:'Natural gas (methane) is naturally odourless and colourless. Mercaptans (typically tert-butyl mercaptan/THT blend) are added at the distribution level to give gas its distinctive "rotten egg" smell, allowing people to detect leaks. The odourant concentration is regulated to ensure detectability at 1/5 the LEL.',keyConcept:'Gas odourant: mercaptan/THT added to natural gas. Detectable at 1% concentration (1/5 of LEL of ~5%). Propane also odourized. Odourant can fade in old pipes — "odour fade."'},
{id:31,topic:'supply',topicLabel:'Gas Supply Systems',diff:'medium',text:'What is second-stage regulation in a propane (LP gas) system?',options:['A) The second regulator in a two-stage natural gas system at the meter','B) The second regulator in an LP system that reduces the outlet pressure from the first stage (~10 psig) to appliance operating pressure (~11 in WC / 2.74 kPa)','C) A backup regulator that activates if the primary fails','D) The second stage of pressure testing for LP systems'],answer:1,explanation:'LP gas systems typically use two-stage regulation: First stage at the tank reduces vapor pressure (which varies with temperature) to a constant ~10 psig (69 kPa). Second stage at or near the building reduces 10 psig to appliance operating pressure (~11 in WC / 2.74 kPa). This provides stable pressure regardless of tank level or temperature.',keyConcept:'LP two-stage regulation: Tank vapor → First stage (~10 psig) → Second stage (~11 in WC). Stable appliance pressure regardless of tank pressure variation.'},
{id:32,topic:'supply',topicLabel:'Gas Supply Systems',diff:'medium',text:'What unit is typically used to measure gas pressure in low-pressure residential systems?',options:['A) psi (pounds per square inch)','B) Inches of water column (in WC) measured with a manometer','C) Bar (metric pressure unit)','D) Pascals only'],answer:1,explanation:'Low-pressure gas systems (residential/commercial) operate at pressures too low for standard pressure gauges. Inches of water column (in WC) — measured with a manometer or magnehelic gauge — is the standard unit. 1 psi = 27.7 in WC. Standard residential NG: 7 in WC. High-pressure systems use kPa or psi.',keyConcept:'Low pressure gas measurement: inches of water column (in WC) using a manometer. 7 in WC = ~1.75 kPa = ~0.25 psi. Manometer must be connected at test port.'},
{id:33,topic:'supply',topicLabel:'Gas Supply Systems',diff:'medium',text:'When must the gas supply be shut off and the building evacuated during a gas leak response?',options:['A) Only if a gas smell persists for more than 10 minutes','B) Immediately when a gas leak is detected or suspected — shut off gas at the meter, do not operate any electrical switches, leave the building, and call the gas utility from outside','C) After checking appliances and attempting to find the leak with soapy water','D) Only if the gas concentration exceeds 50% LEL on a detector'],answer:1,explanation:'Gas leak response: DO NOT operate any electrical switches (can spark ignition), DO NOT use phone inside, shut off gas at the meter exterior shutoff, leave the building immediately, call the utility from outside. Even a small ignition source can ignite gas-air mixture at concentrations between 5-15% (LEL-UEL for natural gas).',keyConcept:'Gas leak response: no switches/phones → shut off at meter → leave immediately → call utility from outside. Never re-enter until utility clears the building.'},
{id:34,topic:'supply',topicLabel:'Gas Supply Systems',diff:'hard',text:'A service regulator has an inlet pressure of 60 psig and is set for 7 in WC outlet. The lockup pressure measured at the test port is 14 in WC. Is this acceptable?',options:['A) Yes — 14 in WC lockup is within tolerance for this regulator type','B) Yes — lockup pressure at 2× setpoint is normal and acceptable as long as it does not exceed the maximum allowable pressure of downstream piping','C) No — lockup pressure should never exceed the setpoint','D) No — lockup of 14 in WC indicates the regulator is over-pressuring the system'],answer:1,explanation:'Lockup pressure of 14 in WC = 2× the 7 in WC setpoint. For residential low-pressure service, the maximum allowable downstream pressure is typically 14 in WC per CSA B149.1. If the downstream piping and appliances are rated for 14 in WC maximum, this lockup is acceptable. If the spec is 125% = 8.75 in WC, further investigation is needed. Verify against appliance and piping ratings.',keyConcept:'Lockup pressure acceptability: compare to maximum allowable downstream pressure. Residential systems: max typically 14 in WC. If lockup exceeds max allowable, regulator needs adjustment or replacement.'},
{id:35,topic:'supply',topicLabel:'Gas Supply Systems',diff:'hard',text:'Underground gas distribution pipes are protected from external corrosion by cathodic protection. What does this system do?',options:['A) Applies a coating of zinc to the outside of the pipe','B) Applies a small DC electrical current or sacrificial anode to make the pipe cathodic (positive), preventing corrosion by reversing the electrochemical reaction','C) Fills the trench with limestone to neutralize soil acids','D) Adds a corrosion inhibitor to the gas stream'],answer:1,explanation:'Cathodic protection reverses the electrochemical corrosion process. In impressed current systems, a DC rectifier makes the pipe cathodic (negative terminal) — corrosion only occurs at the anode. In sacrificial anode systems, a more active metal (magnesium) corrodes instead of the steel pipe. Required by CSA Z662 for steel underground pipelines.',keyConcept:'Cathodic protection: impressed current (rectifier + inert anode) OR sacrificial anode (magnesium). Makes steel pipe cathodic → corrosion directed to anode instead. Required for underground steel gas pipe.'},
{id:36,topic:'supply',topicLabel:'Gas Supply Systems',diff:'hard',text:'A gas fitter needs to verify the supply pressure at a new gas appliance installation. What is the correct method?',options:['A) Use a standard dial pressure gauge at the appliance inlet','B) Connect a manometer to the appliance test port (inlet pressure tap) or a test tee installed in the supply line before the appliance shutoff valve','C) Use a multi-meter set to voltage to measure supply pressure','D) Rely on the regulator setpoint — actual measurement is not required for service work'],answer:1,explanation:'Measuring gas supply pressure requires a manometer (water column or digital) connected to the test port on the appliance gas valve, or a test tee installed in the supply line. Standard dial gauges are not accurate enough for low gas pressures. Both inlet and manifold (burner) pressure should be measured and documented during commissioning.',keyConcept:'Gas pressure measurement: manometer at test port or test tee. Measure: inlet pressure (upstream of appliance valve) AND manifold pressure (at burner). Document both. Never use dial gauge for low pressures.'},
{id:37,topic:'supply',topicLabel:'Gas Supply Systems',diff:'medium',text:'What is the purpose of a gas meter bypass valve?',options:['A) To allow gas to flow at reduced pressure when the meter is at maximum capacity','B) To permit maintenance or replacement of the meter without interrupting gas service to the building','C) To bypass the service regulator during peak demand periods','D) To allow the homeowner to manually increase gas pressure'],answer:1,explanation:'A meter bypass (also called a "three-valve bypass" at the meter set) allows the meter to be removed or replaced while maintaining gas flow to the building through the bypass valve. This is used by the utility for meter maintenance, testing, and replacement without service interruption.',keyConcept:'Meter bypass: three-valve arrangement allows meter replacement without service interruption. Utility-operated. Gas fitter should not manipulate utility-owned equipment without authorization.'},
{id:38,topic:'supply',topicLabel:'Gas Supply Systems',diff:'medium',text:'How does propane vapor pressure change with temperature and what is the practical implication?',options:['A) Propane vapor pressure decreases as temperature increases — tanks must be kept cool','B) Propane vapor pressure increases with temperature — cold weather reduces tank pressure and may prevent adequate vapor supply','C) Propane vapor pressure is constant regardless of temperature','D) Temperature has no effect — only tank level affects vapor pressure'],answer:1,explanation:'Propane exists as a liquid in the tank with vapor above. Vapor pressure increases with temperature (like any volatile liquid). In cold weather, low temperatures reduce vapor pressure significantly. Below -42°C (-44°F), propane vapor pressure drops below atmospheric and won\'t vaporize. Practical implication: outdoor LP tanks may not supply adequate vapor on very cold days without tank heating.',keyConcept:'Propane vapor pressure vs temperature: decreases with cold. Risk: inadequate vapor supply in extreme cold. Solution: use natural gas in very cold climates or install tank heaters for LP systems.'},
{id:39,topic:'supply',topicLabel:'Gas Supply Systems',diff:'medium',text:'What is a medium-pressure gas system and what pressure range does it operate at?',options:['A) A system operating at 7 in WC to 14 in WC','B) A system operating above 1/2 psi (3.45 kPa) up to 5 psig (34.5 kPa) — common in commercial and industrial applications','C) Any system between residential and industrial pressure levels','D) A system operating at exactly 2 psig (13.8 kPa) — the most common commercial gas pressure'],answer:1,explanation:'CSA B149.1 defines medium pressure as above 1/2 psig up to 5 psig. Medium pressure systems are common in commercial buildings where higher flows are required, allowing smaller pipe sizes. A regulator at each appliance (or zone) reduces medium pressure to appliance operating pressure.',keyConcept:'Gas pressure classifications per CSA B149.1: Low = <1/2 psig. Medium = 1/2 to 5 psig. High = >5 psig. Medium pressure allows smaller pipes for higher flows.'},
{id:40,topic:'supply',topicLabel:'Gas Supply Systems',diff:'hard',text:'A 403A gas fitter calculates that the gas supply pressure at a building 300 m from the main drops to 4 in WC during peak demand. The appliances require minimum 5 in WC inlet. What is the solution?',options:['A) Increase the appliance orifice size to compensate for low pressure','B) Install a booster regulator at the building to increase supply pressure — this is not a valid solution for low upstream pressure','C) Increase the service pipe diameter to reduce pressure drop, or request higher supply pressure from the utility','D) Accept 4 in WC — most appliances will operate at reduced pressure'],answer:2,explanation:'The correct solution for inadequate supply pressure is reducing pressure drop in the supply pipe (increase pipe diameter) or requesting higher supply pressure from the utility. A booster regulator cannot boost pressure beyond what is supplied. Oversizing orifices is dangerous and code-violating. Appliances must receive minimum pressure specified by the manufacturer.',keyConcept:'Low supply pressure: increase pipe size (reduce pressure drop) OR request higher supply pressure from utility. Booster pumps for gas are specialized and not a general solution.'},
// ── PIPING (41-56) ──
{id:41,topic:'piping',topicLabel:'Piping Systems',diff:'easy',text:'What is the most common pipe material for above-ground natural gas distribution within buildings?',options:['A) Copper tubing','B) Black steel pipe (Schedule 40) with malleable iron or black steel fittings','C) PVC plastic pipe','D) Galvanized steel pipe'],answer:1,explanation:'Black steel pipe (ASTM A53 or equivalent) with malleable iron fittings is the standard for above-ground interior gas piping. Galvanized pipe is not approved inside buildings (zinc flakes can clog appliance components). PVC is not approved for gas.',keyConcept:'Above-ground gas piping: black steel pipe + malleable iron fittings. NOT galvanized (inside buildings). NOT PVC. CSST also approved but requires bonding. Copper approved for NG, not LP.'},
{id:42,topic:'piping',topicLabel:'Piping Systems',diff:'easy',text:'What thread sealant must be used on gas pipe NPT connections?',options:['A) Standard white PTFE tape (plumber\'s tape)','B) Yellow PTFE tape or pipe thread compound specifically rated and listed for gas service','C) Loctite thread sealant (any grade)','D) No sealant needed for tapered NPT threads — they self-seal'],answer:1,explanation:'Standard white PTFE tape is NOT rated for gas service. Gas connections require yellow PTFE tape or pipe thread compound specifically listed for gas (e.g., Rector Seal T+2, Gas-Tite). Using non-rated sealants can result in leaks that develop over time. CSA B149.1 requires listed sealants.',keyConcept:'Gas thread sealant: yellow PTFE tape OR gas-rated pipe compound. NOT white PTFE tape (not rated for gas). Apply to male threads only, leave first thread bare.'},
{id:43,topic:'piping',topicLabel:'Piping Systems',diff:'easy',text:'What is the purpose of a drip leg (sediment trap) installed before a gas appliance?',options:['A) To reduce gas pressure to the appliance','B) To trap condensate, debris, and scale from the gas supply before they enter the appliance regulator and valves','C) To serve as an emergency shutoff in case of fire','D) To allow pressure testing of the appliance separately'],answer:1,explanation:'A drip leg is a short vertical pipe extension below the horizontal run, capped at the bottom, installed as the last fitting before connecting to the appliance. Condensate, pipe scale, and debris fall into the drip leg instead of entering the appliance regulator and gas valve, preventing blockage and damage.',keyConcept:'Drip leg: vertical pocket before appliance inlet. Collects moisture and debris. Required by CSA B149.1 for most appliances. Must be accessible for periodic cleaning.'},
{id:44,topic:'piping',topicLabel:'Piping Systems',diff:'medium',text:'CSST (corrugated stainless steel tubing) requires electrical bonding. What specific hazard does bonding mitigate?',options:['A) Static buildup from gas flowing through the corrugated tube','B) Lightning-induced electrical surges that can arc through CSST walls, causing perforation and potential gas leak or ignition','C) Galvanic corrosion between CSST and copper fittings','D) Induction heating from nearby electrical conduit'],answer:1,explanation:'CSST is vulnerable to perforation from lightning-induced electrical surges travelling through a building\'s structure. The thin corrugated stainless steel walls can be perforated by arc discharge. Bonding CSST to the building\'s electrical grounding system equalizes electrical potential and reduces the arc risk. Required by CGA/CSA and CSST manufacturers.',keyConcept:'CSST bonding: required to prevent lightning-induced arc perforation. Bond to electrical grounding system at each segment using listed bonding clamp. Not grounding — it\'s bonding (equipotential).'},
{id:45,topic:'piping',topicLabel:'Piping Systems',diff:'medium',text:'What is the maximum spacing for supports on 1-inch (25 mm) black steel gas pipe run horizontally?',options:['A) 1 m (3 ft)','B) 2.4 m (8 ft) — check CSA B149.1 or manufacturer specs for exact requirement','C) 4.5 m (15 ft)','D) No spacing requirement for rigid steel pipe'],answer:1,explanation:'CSA B149.1 requires support spacing for gas pipe. For 1" rigid steel pipe, maximum support spacing is typically 2.4 m (8 ft) horizontally. Smaller pipe requires closer spacing: 3/4" = 1.8 m, 1/2" = 1.5 m. Check current code as values may vary by jurisdiction.',keyConcept:'Gas pipe support spacing (CSA B149.1): 1/2" = 1.5m, 3/4" = 1.8m, 1" = 2.4m, 1.25"+ = 3.0m. Unsupported pipe sags, causes stress at fittings, and can pull joints apart.'},
{id:46,topic:'piping',topicLabel:'Piping Systems',diff:'medium',text:'What pressure test is required for a new gas piping system before it is connected to appliances and the gas supply per CSA B149.1?',options:['A) Visual inspection only — pressure testing is optional','B) Pressure test with air or nitrogen at 1.5× the maximum allowable operating pressure for a minimum of 10 minutes with no pressure drop','C) Fill with water at full supply pressure for 30 minutes','D) Test at the exact operating pressure for 5 minutes'],answer:1,explanation:'CSA B149.1 requires new gas piping to be pressure tested with air or nitrogen (never with gas) at 1.5× the maximum allowable operating pressure for a minimum of 10 minutes with no measurable pressure drop. The inspector must witness this test before the system is connected to the gas supply.',keyConcept:'Gas pipe pressure test (CSA B149.1): air or nitrogen, 1.5× max operating pressure, 10 min minimum, zero pressure drop. Never test with natural gas. Document and inspector witness required.'},
{id:47,topic:'piping',topicLabel:'Piping Systems',diff:'medium',text:'When installing gas piping underground, what protection is required for metallic pipe?',options:['A) No protection needed for schedule 40 steel pipe','B) Metallic underground gas pipe must be protected from corrosion with approved coating (polyethylene wrap or fusion-bonded epoxy) and/or cathodic protection, and must not have mechanical joints below grade','C) Paint with zinc-based coating and install in concrete conduit','D) Install in corrugated plastic sleeve only'],answer:1,explanation:'Underground metallic gas pipe must be protected against soil corrosion per CSA B149.1. Methods include factory polyethylene coating, field-applied tape wrapping, or fusion-bonded epoxy coating. Cathodic protection is also required for many installations. Mechanical joints (unions, threaded fittings) are not permitted underground — use welded or properly coated fittings.',keyConcept:'Underground gas pipe: corrosion protection required (PE coating, tape wrap, or FBE). No mechanical joints below grade — use welded joints. Cathodic protection for steel systems.'},
{id:48,topic:'piping',topicLabel:'Piping Systems',diff:'medium',text:'What is the maximum length of a flexible gas connector that can be used to connect an appliance to the rigid gas supply piping?',options:['A) 300 mm (12 in) — flexible connectors are rarely used','B) 1.8 m (6 ft) — check CSA B149.1 and local code for exact limit','C) Unlimited length — flexible connectors can be any length','D) 600 mm (24 in) maximum for all appliances'],answer:1,explanation:'CSA B149.1 limits flexible gas connectors to a maximum of 1.8 m (6 ft) total length. They must be listed for gas service, must not pass through walls or ceilings, must not be concealed, and should not be kinked. Gas ranges and dryers commonly use flexible connectors.',keyConcept:'Flexible gas connector: max 1.8 m (6 ft), listed for gas, not concealed, not through walls/floors. Replace if kinked, damaged, or corroded. One connector per appliance connection.'},
{id:49,topic:'piping',topicLabel:'Piping Systems',diff:'medium',text:'What is the minimum clearance required between gas piping and electrical conductors or conduit?',options:['A) No clearance required if pipe is grounded','B) A minimum of 25 mm (1 in) separation from electrical conductors, conduit, or meters','C) 150 mm (6 in) from all electrical equipment','D) 300 mm (12 in) from electrical panels'],answer:1,explanation:'CSA B149.1 requires a minimum 25 mm (1 in) clearance between gas piping and electrical conductors, wiring, or conduit. Larger clearances are required near electrical panels and meters. Proper clearances prevent arc ignition and allow inspection of both systems.',keyConcept:'Gas pipe clearance from electrical: minimum 25 mm from wiring/conduit. 150 mm from electrical meters. 300 mm from open-flame devices. Prevents arc ignition if electrical fault occurs.'},
{id:50,topic:'piping',topicLabel:'Piping Systems',diff:'medium',text:'What type of valve is required as the individual appliance shutoff valve for a gas appliance?',options:['A) Ball valve or straight-through plug valve — must be manually operated, accessible, and located within 1.8 m (6 ft) of the appliance','B) Gate valve — provides better throttling control','C) Any valve type is acceptable as long as it is rated for gas','D) A solenoid valve controlled remotely'],answer:0,explanation:'CSA B149.1 requires a manual appliance shutoff valve within 1.8 m (6 ft) of each gas appliance, in the same room, accessible without tools. Ball valves and plug valves are preferred — they provide a clear open/closed indication (handle parallel = open, perpendicular = closed). Gate valves are not recommended due to seat erosion.',keyConcept:'Appliance shutoff: manual ball valve or plug valve, within 1.8 m, same room, accessible. Clear visual indication of open/closed. Must not be concealed or require tools to access.'}
"""

# Write part 1 file
out = BASE / '403a_new.html'
out.write_text(HTML_TOP + QUESTIONS_1_50, encoding='utf-8')
print(f"Part 1 written: {len(HTML_TOP) + len(QUESTIONS_1_50)} chars")
print("HTML_TOP + Questions 1-50 saved to 403a_new.html")
print("Run create_403a_part2.py next")
