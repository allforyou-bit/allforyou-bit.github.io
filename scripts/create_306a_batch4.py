"""306A Sheet Metal Worker — Batch 4: Q76-100 + JS engine + HTML bottom → finalize 306a.html"""
from pathlib import Path
import re, os

Q76_100 = r"""
,{id:76,topic:'layout',topicLabel:'Layout & Pattern Dev',diff:'easy',
text:'A duct offset requires two identical 45° transition pieces. What pattern development technique is used for each mitre cut?',
options:['Radial line from the centreline of the offset','Parallel line development — each mitre is a cylinder cut at 45°','Triangulation for the angled face','The pattern is derived from a standard fitting table only'],
answer:1,
explanation:'A 45° offset cut through a cylinder produces an elliptical mitre. Parallel line development is used: heights at each stretchout division are taken from the front view of the mitre cut.',
keyConcept:'45° offset — parallel line mitre development'},
{id:77,topic:'layout',topicLabel:'Layout & Pattern Dev',diff:'medium',
text:'When a fitting has both curved and flat surfaces (e.g., a round-end rectangular plenum takeoff), what development approach is used?',
options:['Parallel line for the flat sides and triangulation for the curved transition','Radial line for all surfaces','Triangulation for all surfaces regardless of shape','The curved section is approximated as flat — no special method needed'],
answer:0,
explanation:'Compound fittings use combined methods: parallel line for developable flat/cylindrical faces and triangulation for non-developable transition zones.',
keyConcept:'Compound fittings — combined development methods'},
{id:78,topic:'fabrication',topicLabel:'Sheet Metal Fabrication',diff:'medium',
text:'A "drive cleat" (S-drive) joint connects two rectangular duct sections. What is the correct assembly sequence?',
options:['Slide drive cleat over both male edges simultaneously from one end','Snap S-cleat onto one duct edge first, then slide the mating duct edge into the open side, driving it closed','Rivet the drive cleat to both ducts before assembly','Sealant is applied first, then the drive cleat is hammered over both edges'],
answer:1,
explanation:'The S-cleat snaps over the standing seam (male) edge of one duct. The second duct\'s matching seam is then inserted into the open channel and driven closed with a hammer/mallet.',
keyConcept:'Drive cleat — snap then drive assembly'},
{id:79,topic:'fabrication',topicLabel:'Sheet Metal Fabrication',diff:'hard',
text:'When forming a wired edge on a sheet metal piece, what is the purpose of the wire inserted into the hem?',
options:['To conduct electricity for resistance welding','To give a rigid, rounded edge that is safe to handle and resists deformation','To act as a solder filler for the hem','To mark the seam location for inspection'],
answer:1,
explanation:'A wire inserted into a folded hem creates a stiff, rounded edge. This adds rigidity to the panel edge, prevents the sharp cut edge from being exposed, and is used on cylindrical fittings.',
keyConcept:'Wired edge — rigidity + safety'},
{id:80,topic:'fabrication',topicLabel:'Sheet Metal Fabrication',diff:'easy',
text:'When cutting sheet metal with aviation snips, which direction should the waste side be positioned?',
options:['Below the lower blade — curl the waste downward away from the cut line','Above the upper blade','To the left regardless of snip type','Direction does not matter'],
answer:0,
explanation:'The waste piece curls downward and away from the cut line under the lower blade. This prevents the curl from interfering with the snip handles and allows a clean, straight cut.',
keyConcept:'Snips — waste curls downward'},
{id:81,topic:'welding',topicLabel:'Welding & Joining',diff:'medium',
text:'Brazing differs from welding in that:',
options:['Brazing melts the base metal; welding does not','Brazing uses a filler metal with a liquidus above 840°F (450°C) but the base metal does not melt; welding melts the base metal','Brazing requires flux; welding never does','Brazing is only used for aluminium'],
answer:1,
explanation:'Brazing: filler melts (liquidus >450°C/840°F) but base metal remains solid. Welding: base metal melts. The key distinction is whether the base metal is melted.',
keyConcept:'Brazing vs welding — base metal not melted in brazing'},
{id:82,topic:'welding',topicLabel:'Welding & Joining',diff:'easy',
text:'What is "springback" in sheet metal bending and how is it compensated?',
options:['The vibration of the sheet during cutting — compensated by clamping','The elastic return of the metal after bending — compensated by overbending past the required angle','The thermal expansion during welding — compensated by pre-heating','The stretch of the sheet at the bend — compensated by adding material'],
answer:1,
explanation:'When a bend is released, elastic stress partially straightens the metal. To achieve the required final angle, the sheet must be overbent slightly. The overbend angle depends on material and thickness.',
keyConcept:'Springback — overbend to compensate'},
{id:83,topic:'welding',topicLabel:'Welding & Joining',diff:'hard',
text:'When soldering a flat lock seam (folded seam) on tinplate, what is the correct heating technique to ensure full solder penetration?',
options:['Heat the solder wire directly with the iron until it melts into the seam','Heat the seam (base metal) with the iron until the seam is hot enough to melt the solder when touched to the metal — not to the iron','Apply solder to the iron tip first, then wipe across the cold seam','Use a torch to melt bulk solder over the seam and allow it to flow'],
answer:1,
explanation:'Correct soldering: heat the base metal (the seam), not the solder. When the seam is hot enough, touch the solder wire to the metal — it melts and wicks into the joint by capillary action.',
keyConcept:'Soldering — heat the base metal, not the solder'},
{id:84,topic:'hvac',topicLabel:'HVAC Systems',diff:'hard',
text:'A sheet metal worker is asked to install a transfer air grille between two rooms to maintain pressure balance. Where should it be located?',
options:['At high level (near ceiling) in the partition wall — warm air naturally transfers high','At low level (near floor) for cold air transfer','At mid-height — neutral pressure zone','Location does not matter — only grille size matters for transfer'],
answer:0,
explanation:'Transfer air grilles are typically installed high in the partition wall. Warm supply air accumulates near the ceiling and pressure differences drive transfer. Some codes allow door undercuts as an alternative.',
keyConcept:'Transfer grille — high level installation'},
{id:85,topic:'hvac',topicLabel:'HVAC Systems',diff:'medium',
text:'What is "static regain" and where does it occur in a duct system?',
options:['Pressure increase when the duct narrows and velocity increases','Conversion of velocity pressure to static pressure as duct cross-section increases and velocity drops','The total pressure at the AHU outlet','Pressure loss in fittings due to turbulence'],
answer:1,
explanation:'Static regain occurs where duct area increases (e.g., at a main-to-branch transition). Velocity decreases, and by Bernoulli\'s principle, static pressure rises. This offsets friction losses downstream.',
keyConcept:'Static regain — velocity ↓ → static ↑'},
{id:86,topic:'hvac',topicLabel:'HVAC Systems',diff:'easy',
text:'What type of damper is used to prevent reverse airflow in an exhaust duct when the fan is off?',
options:['Volume control damper (manual)','Barometric (backdraft) damper — gravity-operated, opens with forward flow','Fire damper — fusible link','Motorised isolation damper'],
answer:1,
explanation:'A backdraft damper (barometric damper) has gravity-held blades that open with forward airflow from the fan and close by gravity when flow stops, preventing reverse infiltration.',
keyConcept:'Backdraft damper — prevents reverse flow'},
{id:87,topic:'hvac',topicLabel:'HVAC Systems',diff:'medium',
text:'ASHRAE 62.1 governs ventilation for acceptable indoor air quality. Which parameter does it specify for commercial occupancies?',
options:['Maximum duct velocity in m/s','Minimum outdoor air CFM per person and per unit floor area','Maximum CO2 concentration in flue gas','Minimum refrigerant charge weight'],
answer:1,
explanation:'ASHRAE 62.1 sets minimum outdoor air ventilation rates in CFM/person and CFM/ft² of floor area by occupancy type, ensuring adequate dilution of indoor pollutants.',
keyConcept:'ASHRAE 62.1 — minimum OA ventilation rates'},
{id:88,topic:'safety',topicLabel:'Safety & Code',diff:'medium',
text:'A sheet metal worker is cutting sheet metal on a layout table when a piece of sheet slips and causes a laceration. Under OH&S regulations, the employer is required to:',
options:['Document the injury internally only if the worker missed no work','Report the injury to the OH&S authority within the required timeframe and conduct an investigation','Only provide first aid — no reporting needed for minor lacerations','Conduct the investigation only if the worker requests it'],
answer:1,
explanation:'Most Canadian OH&S jurisdictions require reporting of injuries requiring medical treatment (beyond first aid) within a set period and a written investigation report.',
keyConcept:'Injury reporting — mandatory OH&S reporting requirements'},
{id:89,topic:'safety',topicLabel:'Safety & Code',diff:'easy',
text:'What is the correct method to carry a full sheet of heavy-gauge sheet metal to avoid back injury?',
options:['Carry horizontally with straight arms extended in front of body','Carry vertically with two workers — one on each end — keeping the sheet close to the body','Carry flat overhead to keep centre of gravity high','One worker carries by gripping the middle of the sheet with both hands'],
answer:1,
explanation:'Sheet metal should be carried vertically with two workers for heavy sheets, keeping the load close to the body and using proper lift technique (back straight, knees bent) to prevent cuts and back strain.',
keyConcept:'Sheet metal handling — two-person vertical carry'},
{id:90,topic:'safety',topicLabel:'Safety & Code',diff:'hard',
text:'A sheet metal worker discovers asbestos-containing pipe insulation adjacent to ductwork being replaced. What is the correct action?',
options:['Remove the asbestos insulation before installing new duct — it is in the work area','Stop work immediately, leave the area undisturbed, notify the supervisor, and follow asbestos abatement procedures','Cover the asbestos with duct sealant to encapsulate it and proceed','Wear a dust mask and continue — asbestos is only dangerous in large quantities'],
answer:1,
explanation:'Asbestos disturbance requires a certified abatement contractor. The worker must stop, leave the area, secure the zone, and notify the supervisor. Continuing work violates OH&S asbestos regulations.',
keyConcept:'Asbestos — stop work, notify supervisor, certified abatement required'},
{id:91,topic:'tools',topicLabel:'Tools & Equipment',diff:'easy',
text:'What is the purpose of a "notcher" in sheet metal fabrication?',
options:['To cut circular holes for duct collars','To cut square notches at corners of sheet metal blanks to allow bending without overlapping material','To form Pittsburgh lock seams','To punch rivet holes at set spacing'],
answer:1,
explanation:'A notcher (corner notcher) cuts square or mitre notches at the corners of flat blanks. Without notching, the corner material would overlap or interfere when the box sides are bent up.',
keyConcept:'Notcher — corner notch for box bending'},
{id:92,topic:'tools',topicLabel:'Tools & Equipment',diff:'medium',
text:'A "rotary machine" (power rotary) in a sheet metal shop can form all of the following EXCEPT:',
options:['Wired edges','Pittsburgh lock seams','Turned edges and flanges','Punched rivet holes'],
answer:3,
explanation:'A rotary machine (jenny/rotary) forms wired edges, turned edges, flanges, and similar rolled forms. Punching rivet holes requires a punch press or drill — not a rotary machine.',
keyConcept:'Rotary machine — forms edges; cannot punch holes'},
{id:93,topic:'tools',topicLabel:'Tools & Equipment',diff:'hard',
text:'When using a slip roll to form a cone (tapered cylinder), how is the taper achieved?',
options:['One end of the rear roller is set higher than the other, creating differential curvature across the sheet width','The sheet is fed at an angle to the rollers using a guide fence','A tapered forming die is inserted between the rolls','The slip roll cannot form cones — triangulation and hand forming are required'],
answer:0,
explanation:'To form a cone on a slip roll, one end of the rear roller is adjusted higher (or lower) than the other. This creates greater curvature at the narrow cone end and less at the wide end.',
keyConcept:'Slip roll cone — differential rear roller height'},
{id:94,topic:'layout',topicLabel:'Layout & Pattern Dev',diff:'medium',
text:'What is the "seam line" on a developed pattern?',
options:['The line where solder is applied','The line along which the pattern is joined (rolled and seamed) to form the fitting — typically at the shortest element','The line showing minimum material thickness','The outline of the developed flat pattern'],
answer:1,
explanation:'The seam line is where the flat pattern is joined together after rolling/forming. It is placed at the shortest element (often the throat of an elbow) to minimise seam length.',
keyConcept:'Seam line — shortest element of the pattern'},
{id:95,topic:'fabrication',topicLabel:'Sheet Metal Fabrication',diff:'easy',
text:'What is the correct name for the tool used to form the "male" standing seam edge on a duct panel using a sheet metal brake?',
options:['Pittsburgh machine','Bar folder','Notcher','Slip roll'],
answer:1,
explanation:'A bar folder (or bar-folding machine) forms a standing seam (S-lock male edge) or short flanges by folding the sheet edge back on itself. The Pittsburgh machine forms the pocket (female side).',
keyConcept:'Bar folder — male standing seam / S-lock edge'},
{id:96,topic:'hvac',topicLabel:'HVAC Systems',diff:'medium',
text:'In SMACNA duct construction, what is the purpose of intermediate reinforcement angles on a large rectangular duct panel?',
options:['They direct airflow within the duct','They provide external structural stiffening to prevent panel deflection under pressure','They are required for UL fire listing of all rectangular ducts','They replace the need for sheet metal hangers'],
answer:1,
explanation:'SMACNA specifies intermediate reinforcement (angle iron or flat bar) welded or bolted to large duct panels to prevent buckling and panel flutter under positive or negative pressure.',
keyConcept:'Intermediate reinforcement — prevents panel deflection'},
{id:97,topic:'welding',topicLabel:'Welding & Joining',diff:'medium',
text:'When using a resistance spot welder, what is the purpose of applying electrode force (squeeze pressure) before and during welding?',
options:['To drive the electrode into the sheet to create a mechanical interlock','To ensure good electrical contact and contain the molten nugget during solidification','To preheat the sheet before current is applied','To prevent electrode overheating'],
answer:1,
explanation:'Electrode force ensures intimate electrical contact (reducing contact resistance) and applies forging pressure to contain the weld nugget as it solidifies, preventing porosity and expulsion.',
keyConcept:'Spot weld — electrode force for contact and nugget containment'},
{id:98,topic:'safety',topicLabel:'Safety & Code',diff:'medium',
text:'Under BC and most Canadian OH&S regulations, what is the maximum height from which a worker can fall before fall protection is mandatory on a construction site?',
options:['1.5m (5 ft)','3m (10 ft)','4.5m (15 ft)','6m (20 ft)'],
answer:1,
explanation:'In most Canadian provinces (BC, Ontario, Alberta), fall protection (guardrail, safety net, or personal fall arrest system) is required when a worker is exposed to a fall of 3m (10 ft) or more.',
keyConcept:'Fall protection — mandatory at ≥3m on construction sites'},
{id:99,topic:'tools',topicLabel:'Tools & Equipment',diff:'easy',
text:'What is the purpose of the "squaring bar" on a layout table?',
options:['To measure sheet metal gauge','To provide a reference edge perpendicular to the table edge so patterns can be laid out square','To guide snips during straight cutting','To calibrate the press brake die alignment'],
answer:1,
explanation:'The squaring bar (or carpenter\'s square built into the table) provides a 90° reference. Sheet metal blanks are positioned against it to ensure patterns are laid out perpendicular and square.',
keyConcept:'Squaring bar — 90° reference for layout'},
{id:100,topic:'fabrication',topicLabel:'Sheet Metal Fabrication',diff:'hard',
text:'A 450mm×300mm rectangular duct section is being fabricated from 24ga galvanised steel for a 1/2" WG system. According to SMACNA HVAC Duct Construction Standards, what transverse joint is acceptable?',
options:['Slip-and-drive (S & Drive) joint','Pocket lock (button punch snap lock)','Raw (unfinished) butt joint with sealant only','Companion angle flange with bolts at 150mm spacing'],
answer:0,
explanation:'SMACNA permits slip-and-drive (S & Drive) transverse connections for low-pressure (up to 2" WG) rectangular ducts at this size. Pocket lock is used at joints; companion angle is for higher pressure or larger ducts.',
keyConcept:'SMACNA transverse joint — S&Drive acceptable at ≤2" WG'}
"""

# JS engine + HTML bottom
JS_AND_BOTTOM = r"""
];

// ── Quiz Engine ──────────────────────────────────────────────────────────────
const MOCK_PAGE_KEY = '306a';
let current = 0, score = 0, answered = false;
let filteredQs = [...questions];
let mockActive = false, mockQs = [], mockIdx = 0, mockScore = 0, mockTimer = null, mockTimeLeft = 0;
let quizMode = 'quiz'; // 'quiz' | 'flashcard'
let fcIdx = 0, fcQs = [], fcFlipped = false;

function initStreak() {
  const today = new Date().toDateString();
  let streak = parseInt(localStorage.getItem('studyStreak') || '0');
  let streakDate = localStorage.getItem('streakDate');
  let todayCorrect = parseInt(localStorage.getItem('todayCorrect_' + MOCK_PAGE_KEY) || '0');
  let todayDate = localStorage.getItem('todayDate_' + MOCK_PAGE_KEY);
  if (todayDate !== today) { todayCorrect = 0; localStorage.setItem('todayDate_' + MOCK_PAGE_KEY, today); }
  if (streakDate === today) { /* same day */ }
  else if (streakDate === new Date(Date.now() - 86400000).toDateString()) { /* consecutive */ }
  else { streak = 0; }
  document.getElementById('streakCount').textContent = streak;
  document.getElementById('todayCorrect').textContent = todayCorrect;
}

function applyFilter() {
  const topic = document.getElementById('topicFilter').value;
  const diff = document.getElementById('diffFilter').value;
  const tab = document.querySelector('.tab-btn.active')?.dataset.tab;
  let pool = tab === 'mistakes' ? getWrongBank() : questions;
  filteredQs = pool.filter(q =>
    (topic === 'all' || q.topic === topic) &&
    (diff === 'all' || q.diff === diff)
  );
  current = 0; score = 0; answered = false;
  document.getElementById('scoreDisplay').textContent = '0';
  document.getElementById('totalDisplay').textContent = filteredQs.length;
  loadQuestion();
}

function getWrongBank() {
  return JSON.parse(localStorage.getItem('wrongBank_' + MOCK_PAGE_KEY) || '[]')
    .map(id => questions.find(q => q.id === id)).filter(Boolean);
}

function loadQuestion() {
  if (!filteredQs.length) {
    document.getElementById('questionText').textContent = 'No questions match the selected filter.';
    document.getElementById('optionsContainer').innerHTML = '';
    document.getElementById('explanationBox').classList.add('hidden');
    document.getElementById('navBtns').classList.add('hidden');
    return;
  }
  const q = filteredQs[current];
  document.getElementById('questionNum').textContent = current + 1;
  document.getElementById('questionTotal').textContent = filteredQs.length;
  document.getElementById('topicTag').textContent = q.topicLabel;
  document.getElementById('diffTag').textContent = q.diff.charAt(0).toUpperCase() + q.diff.slice(1);
  document.getElementById('questionText').textContent = q.text;
  document.getElementById('explanationBox').classList.add('hidden');
  document.getElementById('navBtns').classList.remove('hidden');
  answered = false;
  const opts = document.getElementById('optionsContainer');
  opts.innerHTML = '';
  q.options.forEach((opt, i) => {
    const btn = document.createElement('button');
    btn.className = 'option-btn'; btn.textContent = opt;
    btn.onclick = () => selectAnswer(i);
    opts.appendChild(btn);
  });
  updateProgressBar();
}

function selectAnswer(idx) {
  if (answered) return;
  answered = true;
  const q = filteredQs[current];
  const btns = document.querySelectorAll('.option-btn');
  btns[q.answer].classList.add('correct');
  if (idx !== q.answer) { btns[idx].classList.add('wrong'); addToWrongBank(q.id); }
  else { score++; document.getElementById('scoreDisplay').textContent = score; recordTopicStat(q.topic, true); updateStreak(); }
  if (idx !== q.answer) recordTopicStat(q.topic, false);
  document.getElementById('explanationText').textContent = q.explanation;
  document.getElementById('keyConceptText').textContent = q.keyConcept;
  document.getElementById('explanationBox').classList.remove('hidden');
  saveProgress();
}

function navigate(dir) {
  current = Math.max(0, Math.min(filteredQs.length - 1, current + dir));
  answered = false; loadQuestion();
}

function updateProgressBar() {
  const pct = filteredQs.length ? ((current + 1) / filteredQs.length * 100) : 0;
  document.getElementById('progressFill').style.width = pct + '%';
}

function updateStreak() {
  const today = new Date().toDateString();
  let streak = parseInt(localStorage.getItem('studyStreak') || '0');
  let streakDate = localStorage.getItem('streakDate');
  let todayCorrect = parseInt(localStorage.getItem('todayCorrect_' + MOCK_PAGE_KEY) || '0') + 1;
  if (streakDate !== today) {
    streak = (streakDate === new Date(Date.now() - 86400000).toDateString()) ? streak + 1 : 1;
    localStorage.setItem('streakDate', today);
    localStorage.setItem('studyStreak', streak);
  }
  localStorage.setItem('todayCorrect_' + MOCK_PAGE_KEY, todayCorrect);
  document.getElementById('streakCount').textContent = streak;
  document.getElementById('todayCorrect').textContent = todayCorrect;
}

function addToWrongBank(id) {
  let wb = JSON.parse(localStorage.getItem('wrongBank_' + MOCK_PAGE_KEY) || '[]');
  if (!wb.includes(id)) { wb.push(id); localStorage.setItem('wrongBank_' + MOCK_PAGE_KEY, JSON.stringify(wb)); }
  document.getElementById('wrongCount').textContent = wb.length;
}

function recordTopicStat(topic, correct) {
  let stats = JSON.parse(localStorage.getItem('topicStats_' + MOCK_PAGE_KEY) || '{}');
  if (!stats[topic]) stats[topic] = { correct: 0, total: 0 };
  stats[topic].total++; if (correct) stats[topic].correct++;
  localStorage.setItem('topicStats_' + MOCK_PAGE_KEY, JSON.stringify(stats));
  renderTopicProgress();
}

function renderTopicProgress() {
  const stats = JSON.parse(localStorage.getItem('topicStats_' + MOCK_PAGE_KEY) || '{}');
  const container = document.getElementById('topicProgressBars');
  if (!container) return;
  const topicLabels = { layout: 'Layout & Pattern Dev', fabrication: 'Fabrication', welding: 'Welding & Joining', hvac: 'HVAC Systems', safety: 'Safety & Code', tools: 'Tools & Equipment' };
  container.innerHTML = Object.entries(topicLabels).map(([k, label]) => {
    const s = stats[k] || { correct: 0, total: 0 };
    const pct = s.total ? Math.round(s.correct / s.total * 100) : 0;
    return `<div class="topic-bar-item"><span class="topic-bar-label">${label}</span><div class="topic-bar-track"><div class="topic-bar-fill" style="width:${pct}%"></div></div><span class="topic-bar-pct">${pct}%</span></div>`;
  }).join('');
}

function saveProgress() {
  localStorage.setItem('progress_' + MOCK_PAGE_KEY, JSON.stringify({ current, score, total: filteredQs.length }));
}

// Mock Exam
function buildMockQs(n) {
  const topicKeys = ['layout', 'fabrication', 'welding', 'hvac', 'safety', 'tools'];
  const topicCounts = { layout: 20, fabrication: 24, welding: 16, hvac: 20, safety: 12, tools: 8 };
  const total = Object.values(topicCounts).reduce((a, b) => a + b, 0);
  let pool = [];
  topicKeys.forEach(t => {
    const tQs = questions.filter(q => q.topic === t);
    const cnt = Math.round(n * topicCounts[t] / total);
    const shuffled = [...tQs].sort(() => Math.random() - 0.5);
    pool.push(...shuffled.slice(0, cnt));
  });
  return pool.sort(() => Math.random() - 0.5).slice(0, n);
}

function openMockSetup() { document.getElementById('mockSetup').classList.remove('hidden'); }

function startMockExam() {
  const n = parseInt(document.getElementById('mockQCount').value);
  mockQs = buildMockQs(n); mockIdx = 0; mockScore = 0;
  document.getElementById('mockSetup').classList.add('hidden');
  document.getElementById('mockExam').classList.remove('hidden');
  document.getElementById('mockTotal').textContent = mockQs.length;
  const secsPerQ = 90;
  mockTimeLeft = n * secsPerQ;
  renderMockQ(); startMockTimer();
}

function startMockTimer() {
  if (mockTimer) clearInterval(mockTimer);
  mockTimer = setInterval(() => {
    mockTimeLeft--;
    const m = Math.floor(mockTimeLeft / 60), s = mockTimeLeft % 60;
    document.getElementById('mockTimer').textContent = m + ':' + String(s).padStart(2, '0');
    if (mockTimeLeft <= 0) { clearInterval(mockTimer); showMockResults(); }
  }, 1000);
}

function renderMockQ() {
  const q = mockQs[mockIdx];
  document.getElementById('mockQNum').textContent = mockIdx + 1;
  document.getElementById('mockQText').textContent = q.text;
  const opts = document.getElementById('mockOptions');
  opts.innerHTML = '';
  q.options.forEach((opt, i) => {
    const btn = document.createElement('button');
    btn.className = 'option-btn'; btn.textContent = opt;
    btn.onclick = () => answerMockQ(i);
    opts.appendChild(btn);
  });
  document.getElementById('mockFeedback').classList.add('hidden');
  document.getElementById('mockNextBtn').classList.add('hidden');
}

function answerMockQ(idx) {
  const q = mockQs[mockIdx];
  const btns = document.querySelectorAll('#mockOptions .option-btn');
  btns.forEach(b => b.disabled = true);
  btns[q.answer].classList.add('correct');
  if (idx !== q.answer) { btns[idx].classList.add('wrong'); addToWrongBank(q.id); }
  else { mockScore++; }
  document.getElementById('mockFeedback').textContent = q.explanation;
  document.getElementById('mockFeedback').classList.remove('hidden');
  document.getElementById('mockNextBtn').classList.remove('hidden');
}

function nextMockQ() {
  mockIdx++;
  if (mockIdx >= mockQs.length) showMockResults();
  else renderMockQ();
}

function showMockResults() {
  if (mockTimer) clearInterval(mockTimer);
  document.getElementById('mockExam').classList.add('hidden');
  const pct = Math.round(mockScore / mockQs.length * 100);
  document.getElementById('mockResultScore').textContent = mockScore + '/' + mockQs.length + ' (' + pct + '%)';
  document.getElementById('mockResultMsg').textContent = pct >= 70 ? '✅ Above the 70% pass threshold — great work!' : '📚 Below 70% — keep reviewing and try again!';
  document.getElementById('mockResults').classList.remove('hidden');
  saveMockHistory(pct);
}

function saveMockHistory(pct) {
  let hist = JSON.parse(localStorage.getItem('mockHistory_' + MOCK_PAGE_KEY) || '[]');
  hist.unshift({ date: new Date().toLocaleDateString(), score: mockScore, total: mockQs.length, pct });
  if (hist.length > 5) hist = hist.slice(0, 5);
  localStorage.setItem('mockHistory_' + MOCK_PAGE_KEY, JSON.stringify(hist));
  renderScoreHistory();
}

function renderScoreHistory() {
  const hist = JSON.parse(localStorage.getItem('mockHistory_' + MOCK_PAGE_KEY) || '[]');
  const el = document.getElementById('scoreHistory');
  if (!el) return;
  el.innerHTML = hist.length ? hist.map(h => `<div class="hist-row"><span>${h.date}</span><span>${h.score}/${h.total} (${h.pct}%)</span></div>`).join('') : '<p>No mock exam history yet.</p>';
}

function shareMockScore() {
  const score = document.getElementById('mockResultScore').textContent;
  const text = `I scored ${score} on the 306A Sheet Metal Worker practice exam! Try it free: https://allforyou-bit.github.io/306a.html`;
  if (navigator.share) { navigator.share({ title: '306A Mock Exam Score', text, url: 'https://allforyou-bit.github.io/306a.html' }); }
  else { navigator.clipboard.writeText(text).then(() => alert('Score copied to clipboard!')); }
}

function downloadMockResults() {
  const win = window.open('', '_blank');
  win.document.write('<html><head><title>306A Mock Results</title></head><body>');
  win.document.write('<h1>306A Sheet Metal Worker — Mock Exam Results</h1>');
  win.document.write('<p>Score: ' + document.getElementById('mockResultScore').textContent + '</p>');
  win.document.write('<p>Date: ' + new Date().toLocaleDateString() + '</p>');
  win.document.write('<h2>Questions Review</h2>');
  mockQs.forEach((q, i) => {
    win.document.write('<div style="margin:16px 0;padding:12px;border:1px solid #ddd"><p><b>Q' + (i+1) + ':</b> ' + q.text + '</p>');
    win.document.write('<p><b>Answer:</b> ' + q.options[q.answer] + '</p>');
    win.document.write('<p><b>Explanation:</b> ' + q.explanation + '</p></div>');
  });
  win.document.write('</body></html>');
  win.document.close(); win.print();
}

function closeMock() {
  if (mockTimer) clearInterval(mockTimer);
  document.getElementById('mockSetup').classList.add('hidden');
  document.getElementById('mockExam').classList.add('hidden');
  document.getElementById('mockResults').classList.add('hidden');
}

// Cookie Consent
function acceptCookies() {
  localStorage.setItem('cookieOk', '1');
  document.getElementById('cookieBanner').style.display = 'none';
}

function initCookieBanner() {
  if (!localStorage.getItem('cookieOk')) {
    document.getElementById('cookieBanner').style.display = 'flex';
  }
}

// Wrong Bank Tab
function updateWrongBankTab() {
  const wb = JSON.parse(localStorage.getItem('wrongBank_' + MOCK_PAGE_KEY) || '[]');
  document.getElementById('wrongCount').textContent = wb.length;
}

// Tab switching
function switchTab(tab) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.toggle('active', b.dataset.tab === tab));
  if (tab === 'mistakes') {
    quizMode = 'quiz';
    document.getElementById('quizView').classList.remove('hidden');
    document.getElementById('flashcardView').classList.add('hidden');
  }
  applyFilter();
}

// Flashcard mode
function setQuizMode(mode) {
  quizMode = mode;
  if (mode === 'flashcard') {
    document.getElementById('quizView').classList.add('hidden');
    document.getElementById('flashcardView').classList.remove('hidden');
    fcQs = [...filteredQs]; fcIdx = 0; fcFlipped = false;
    renderFlashcard();
  } else {
    document.getElementById('flashcardView').classList.add('hidden');
    document.getElementById('quizView').classList.remove('hidden');
  }
}

function renderFlashcard() {
  if (!fcQs.length) return;
  const q = fcQs[fcIdx];
  document.getElementById('fcNum').textContent = fcIdx + 1;
  document.getElementById('fcTotal').textContent = fcQs.length;
  document.getElementById('fcFront').textContent = q.text;
  document.getElementById('fcBack').textContent = q.options[q.answer] + '\n\n' + q.explanation;
  document.getElementById('fcCard').classList.remove('flipped');
  fcFlipped = false;
}

function flipFlashcard() {
  fcFlipped = !fcFlipped;
  document.getElementById('fcCard').classList.toggle('flipped', fcFlipped);
}

function fcNav(dir) {
  fcIdx = Math.max(0, Math.min(fcQs.length - 1, fcIdx + dir));
  renderFlashcard();
}

function fcMarkKnow() { fcNav(1); }
function fcMarkAgain() { const q = fcQs.splice(fcIdx, 1)[0]; fcQs.push(q); renderFlashcard(); }

// Init
document.addEventListener('DOMContentLoaded', () => {
  initStreak();
  initCookieBanner();
  updateWrongBankTab();
  renderTopicProgress();
  renderScoreHistory();
  applyFilter();
  document.getElementById('topicFilter').addEventListener('change', applyFilter);
  document.getElementById('diffFilter').addEventListener('change', applyFilter);
});
</script>

<!-- Email Capture -->
<section class="email-capture">
  <h3>Get Free 306A Study Tips</h3>
  <p>Join fellow Red Seal candidates preparing for their Sheet Metal Worker exam.</p>
  <form action="https://formsubmit.co/lidbil515@gmail.com" method="POST">
    <input type="hidden" name="_subject" value="New 306A Study Subscriber">
    <input type="hidden" name="_captcha" value="false">
    <input type="email" name="email" placeholder="your@email.com" required>
    <button type="submit">Send Me Tips</button>
  </form>
</section>

<!-- Related Articles -->
<section class="related-articles">
  <h3>Related Guides</h3>
  <div class="related-grid">
    <a href="306a-sheet-metal-worker-career-canada.html" class="related-card">306A Career Guide</a>
    <a href="306a-sheet-metal-worker-salary-canada.html" class="related-card">306A Salary Guide</a>
    <a href="how-to-pass-red-seal-306a-exam.html" class="related-card">How to Pass 306A Exam</a>
    <a href="common-mistakes-306a-exam.html" class="related-card">306A Common Mistakes</a>
  </div>
</section>

<!-- Ko-fi -->
<div class="kofi-wrapper">
  <a href="https://ko-fi.com/redsealexamprep" target="_blank" rel="noopener">
    <img src="https://storage.ko-fi.com/cdn/kofi2.png?v=3" alt="Buy Me a Coffee at ko-fi.com" loading="lazy" width="143" height="32">
  </a>
</div>

<!-- Cookie Banner -->
<div id="cookieBanner" style="display:none;position:fixed;bottom:0;left:0;right:0;background:#1e293b;color:#f1f5f9;padding:14px 20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;z-index:9999;">
  <span style="font-size:0.9rem">We use cookies for analytics and to save your study progress. <a href="privacy.html" style="color:#60a5fa">Privacy Policy</a></span>
  <button onclick="acceptCookies()" style="background:#3b82f6;color:#fff;border:none;padding:8px 18px;border-radius:6px;cursor:pointer;font-weight:600">Accept</button>
</div>

<!-- Footer -->
<footer>
  <p>&copy; 2026 Red Seal Exam Prep &nbsp;|&nbsp; <a href="privacy.html">Privacy</a> &nbsp;|&nbsp; <a href="terms.html">Terms</a> &nbsp;|&nbsp; <a href="disclaimer.html">Disclaimer</a> &nbsp;|&nbsp; <a href="contact.html">Contact</a></p>
  <p style="font-size:0.78rem;color:#94a3b8;margin-top:6px">Not affiliated with Red Seal Program or ICTC. For exam preparation only.</p>
</footer>

<script>
function toggleNav() { document.getElementById('navMenu').classList.toggle('open'); }
</script>
</body>
</html>
"""

# Read temp file, append Q76-100 + close array + engine + bottom
temp = Path('306a_temp.html')
txt = temp.read_text(encoding='utf-8')
txt += Q76_100
txt += JS_AND_BOTTOM

# Write final 306a.html
out = Path('306a.html')
out.write_text(txt, encoding='utf-8')

# Remove temp file
temp.unlink()

# Verify
import re
content = out.read_text(encoding='utf-8')
ids = re.findall(r'id:\s*(\d+)', content)
unique_ids = set(ids)
print(f'Questions found: {len(ids)}')
print(f'ID range: {min(int(i) for i in ids)}-{max(int(i) for i in ids)}')
print(f'Unique IDs: {len(unique_ids)} ({"OK" if len(unique_ids)==len(ids) else "DUPLICATE FOUND"})')
print(f'File size: {len(content):,} chars')
print(f'Has MOCK_PAGE_KEY 306a: {"YES" if "MOCK_PAGE_KEY = \'306a\'" in content else "NO"}')
print(f'HTML closes properly: {"YES" if content.strip().endswith("</html>") else "NO"}')
print('306a.html finalized! Delete batch scripts and update sitemap.')
