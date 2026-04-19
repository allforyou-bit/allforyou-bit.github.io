#!/usr/bin/env python3
"""Add 20 application-type Hard/Medium questions to 442a.html (442A Ironworker)"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NEW_QUESTIONS = r"""
  // ── APPLICATION-TYPE ADDITIONS (2026-04-18) ──
  {id:101,topic:'rigging',topicLabel:'Rigging & Hoisting',diff:'hard',
  text:"An ironworker needs to lift a 6,000 kg steel beam using a two-leg wire rope sling with each leg at 45° from vertical. What is the tension in each sling leg?",
  options:['A) 3,000 kg — equal half the total load','B) 4,243 kg — sling tension increases with angle from vertical','C) 6,000 kg — each leg carries the full load at 45°','D) 2,121 kg — angle reduces load per leg'],
  answer:1,
  explanation:'<strong>Sling leg tension = (Load / number of legs) × (1 / cos θ).</strong> θ = 45° from vertical. Tension = (6,000/2) × (1/cos 45°) = 3,000 × 1.414 = 4,243 kg per leg. The load on each sling leg INCREASES as the angle from vertical increases. At 60°, the factor is 2.0 — each leg carries the full load. This is why angles beyond 60° from vertical are generally avoided.',
  keyConcept:'Sling tension formula: T = (W/n) × (1/cos θ). At 30°: factor=1.15. At 45°: 1.41. At 60°: 2.0. Never exceed 60° from vertical for general lifts.'},

  {id:102,topic:'rigging',topicLabel:'Rigging & Hoisting',diff:'hard',
  text:"An ironworker inspects a wire rope sling before a critical lift and finds 4 broken wires in one rope lay of a 6×19 IWRC wire rope. What action should be taken?",
  options:['A) The sling may be used — limit is 6 broken wires per lay','B) Remove from service immediately — 4 broken wires in one lay exceeds the 3-wire limit for 6×19 rope per ASME B30.9','C) Tag the sling for monitoring only','D) The sling may be used if the broken wires are not load-bearing'],
  answer:1,
  explanation:'<strong>ASME B30.9 discard criteria for 6×19 wire rope: 3 broken wires in one rope lay or 6 in any rope lay length of 6 times the rope diameter.</strong> Finding 4 broken wires in one lay exceeds the 3-wire threshold. Remove from service, cut into short pieces to prevent reuse, and report to the rigger-in-charge. All wires in a sling assembly must remain serviceable — there are no partial-use allowances.',
  keyConcept:'Wire rope inspection (ASME B30.9): 6×19 rope discard at ≥3 broken wires/lay. 6×37 rope: ≥6/lay. Also discard for: kinking, crushing, heat damage, corrosion, reduction >1/3 original diameter.'},

  {id:103,topic:'rigging',topicLabel:'Rigging & Hoisting',diff:'hard',
  text:"A crane is lifting a 20,000 kg load at a 15m radius. The load chart shows maximum lift capacity at 15m is 18,000 kg (with all outriggers fully extended on firm ground). What should the ironworker signalperson communicate to the operator?",
  options:['A) Proceed — crane charts include a 10% safety margin for occasional overloads','B) Stop — the lift exceeds the chart capacity. Reduce radius, add outrigger pads, or use a larger crane','C) Proceed if the lift will be completed in under 2 minutes','D) Proceed if the crane manufacturer approves in writing'],
  answer:1,
  explanation:'<strong>Load chart values are maximums — they MUST NOT be exceeded under any circumstances.</strong> Crane load charts already include safety factors per CSA Z150. Exceeding the chart rating voids the chart, creates an unacceptable risk of crane overturning, and is a criminal liability. The ironworker foreman must stop the lift and reassign: decrease lift radius (boom in), improve ground bearing capacity, or bring a larger crane.',
  keyConcept:'Crane load charts are absolute maximums including all safety factors. NEVER exceed rated capacity. Load = hook load + rigging weight + load block weight.'},

  {id:104,topic:'structural',topicLabel:'Structural Steel Erection',diff:'hard',
  text:"During structural steel erection, an ironworker is bolting a beam connection. The engineer specifies A325 3/4\" bolts in a slip-critical connection. What minimum number of bolts must be installed before the crane can release the member?",
  options:['A) One bolt per connection — sufficient for temporary stability','B) All bolts must be installed and tightened before crane release','C) Minimum 2 bolts per end, or enough to safely support erection loads — as specified in the erection procedure','D) 50% of final bolt count, installed hand-tight only'],
  answer:2,
  explanation:'<strong>CISC and AISC erection guidelines require a minimum of 2 bolts per connection (or per engineer specification) before the crane can release a member.</strong> One bolt provides insufficient rotation restraint — the connection can pivot. With 2 bolts at each end, the member is stable against rotation. Full bolt tightening follows per the erection sequence after multiple members create a stable structure.',
  keyConcept:'Erection bolting: minimum 2 bolts per connection before crane release. Final tightening follows erection sequence. Never release crane on a single-bolt connection.'},

  {id:105,topic:'structural',topicLabel:'Structural Steel Erection',diff:'medium',
  text:"An ironworker is connecting a steel column base plate to an anchor bolt pattern. Three of four anchor bolts are plumb and aligned, but the fourth is out of position by 25mm. What is the CORRECT course of action?",
  options:['A) Force the base plate onto all four bolts by driving with a sledgehammer','B) Flame cut the misaligned bolt and re-drill the base plate','C) Notify the engineer and general contractor — anchor bolt misalignment requires engineering assessment before proceeding','D) Weld the base plate to the three correctly positioned bolts and leave the fourth unused'],
  answer:2,
  explanation:'<strong>Anchor bolt misalignment is a structural deficiency that requires engineering assessment.</strong> Forcing the base plate distorts the anchor bolt, potentially cracking the grout and concrete embedment. Flame cutting a structural anchor bolt changes its material properties and may be prohibited. The engineer must determine if the misalignment is within tolerance, whether repositioning is possible, or if redesign is needed.',
  keyConcept:'Anchor bolt misalignment: STOP and notify engineer. Never force base plates or cut structural anchor bolts without engineering direction.'},

  {id:106,topic:'welding',topicLabel:'Welding & Joining',diff:'hard',
  text:"An ironworker is welding a moment connection on a structural beam using E71T-8 flux-cored wire. The WPS specifies a minimum preheat of 150°C. The ambient temperature is -5°C and the base metal temperature is 4°C. What must be done before welding?",
  options:['A) Begin welding immediately — preheat is for thick plate only','B) Preheat the joint to minimum 150°C using a heating torch, verify with temp sticks or pyrometer, then weld','C) No preheat needed when ambient is above freezing (-5°C is the ambient air, not metal)','D) Increase wire speed to compensate for cold metal temperature'],
  answer:1,
  explanation:'<strong>Preheat requirements are based on base metal temperature, not ambient air temperature.</strong> At 4°C base metal temperature with a 150°C preheat requirement, the joint must be heated to 150°C minimum before striking the arc. Cold steel increases the risk of hydrogen-induced cracking (HIC). Verify with temperature sticks or a contact pyrometer immediately before welding and maintain interpass temperature throughout.',
  keyConcept:'Preheat: applied to base metal, not air temperature. Verify with temp sticks or pyrometer. E71T-8 is a self-shielded FCAW wire used for structural steel — preheat critical in cold conditions.'},

  {id:107,topic:'welding',topicLabel:'Welding & Joining',diff:'hard',
  text:"An ironworker performing a fillet weld on a structural connection notices the weld is developing longitudinal cracking in the weld bead shortly after each pass. The base metal is A36 and filler is E7018. What is the MOST likely cause?",
  options:['A) Travel speed is too slow — too much heat input','B) Hydrogen-induced cracking from moisture in the electrode — electrode was left out of the oven','C) Base metal carbon content is too high for E7018','D) Arc voltage is too high, causing undercutting at the toes'],
  answer:1,
  explanation:'<strong>Longitudinal (centreline) cracking shortly after welding indicates hydrogen-induced cracking (HIC).</strong> E7018 is a low-hydrogen electrode that must be kept in a rod oven at 120-150°C after opening the package. Moisture absorbed by the flux releases hydrogen into the weld pool. Hydrogen migrates to areas of high residual stress (weld centreline) and causes cracking — sometimes hours after welding. Re-dry electrodes at 370°C for 1 hour if moisture absorption is suspected.',
  keyConcept:'E7018 low-hydrogen electrode: must be stored at 120°C in rod oven. Moisture = HIC risk. Redry at 370°C/1hr max 3 times. Longitudinal cracking = HIC until proven otherwise.'},

  {id:108,topic:'safety',topicLabel:'Safety & Fall Protection',diff:'hard',
  text:"An ironworker is working on a steel structure 8m above grade and must temporarily remove a guardrail to swing a beam into position. There are no overhead tie-off points available. What fall protection option is MOST appropriate?",
  options:['A) Proceed without fall protection — the task will take less than 5 minutes','B) Work without protection is permitted if spotters are below','C) Install a safety net below or use a positioning device with secondary restraint — never remove guardrail without alternate protection in place','D) Stop work and wait until a tie-off point is installed by others'],
  answer:2,
  explanation:'<strong>Fall protection must be maintained continuously — removing a guardrail without replacing it with equivalent protection violates provincial OH&S regulations.</strong> Options when tie-off points are unavailable above: 1) Safety net below the work level (pre-installed). 2) Personnel platform with guardrails. 3) Repositioning to access an available anchor. 4) Install a temporary structural anchor before removing the guardrail. "Less than 5 minutes" is never a valid exception.',
  keyConcept:'Fall protection: never remove guardrails without equal or better alternate protection. Safety nets, personal fall arrest, or guardrails must be in place at all times above 3m (varies by province).'},

  {id:109,topic:'blueprint',topicLabel:'Blueprints & Drawings',diff:'hard',
  text:"An ironworker reads a structural drawing showing a W310×129 beam. What does this designation tell the ironworker about the section?",
  options:['A) A wide-flange section: approximately 310mm deep, weighing 129 kg per metre','B) A 310mm square hollow section weighing 129 kg','C) A welded plate girder: 310mm web height, 129mm flange width','D) A cold-formed channel: 310mm leg, 129mm base'],
  answer:0,
  explanation:'<strong>W-shape designation: W = Wide Flange. First number = nominal depth in mm (310mm). Second number = mass in kg/m (129 kg/m).</strong> This is a standard AISC/CISC wide-flange designation used throughout Canadian structural steel practice. The actual depth may vary slightly from nominal. W310×129 is a heavy section used for heavily loaded beams and columns.',
  keyConcept:'Wide-flange designation: W[depth mm]×[mass kg/m]. W310×129 = ~310mm deep, 129 kg per metre of length. Used for structural beams, columns, bracing.'},

  {id:110,topic:'rebar',topicLabel:'Rebar & Reinforcing',diff:'hard',
  text:"An ironworker is placing rebar in a concrete footing. The drawing specifies 20M bars at 200mm c/c each way, with 75mm cover to the outside face. The footing is 400mm thick. After placing the bottom mat, the ironworker notices the total rebar height plus both covers would leave no room for a top mat. What is the CORRECT response?",
  options:['A) Reduce the bottom cover to 50mm to create space for the top mat','B) Notify the superintendent and engineer — the footing design may have an error in drawing vs. actual dimension','C) Place both mats touching — concrete cover can be eliminated for interior footings','D) Eliminate the top mat — one layer of rebar is sufficient for footings'],
  answer:1,
  explanation:'<strong>Rebar placement conflicts with dimensions must be reported to the engineer.</strong> A 400mm footing with 75mm bottom cover + 20M bar (19.5mm) + chair height + 20M top bar + 75mm top cover = physical impossibility. This indicates either a footing dimension error, a cover requirement error, or a bar size error in the drawings. NEVER reduce cover or eliminate reinforcement without engineering direction.',
  keyConcept:'Rebar cover is structural code requirement (CSA A23.3) — cannot be reduced without engineer approval. Drawing conflicts = stop and notify engineer.'},

  {id:111,topic:'structural',topicLabel:'Structural Steel Erection',diff:'medium',
  text:"An ironworker is erecting a multi-storey steel frame and notices that a column is out of plumb by 25mm in a 6m height (approximately 1:240 ratio). The spec tolerance is 1:500. What action is required?",
  options:['A) No action — 25mm is within the typical ±50mm erection tolerance','B) Column is within tolerance — 1:240 is acceptable for multi-storey columns per CISC','C) Column is out of tolerance — must be plumbed and restrained before the next tier is erected','D) Tolerance applies only to the final structure — proceed and adjust at the end'],
  answer:2,
  explanation:'<strong>CISC erection tolerances for column plumbness: typically ±1:500 (1mm per 500mm height).</strong> At 6m height, allowable deviation is 6000/500 = 12mm. The measured 25mm deviation exceeds this. Out-of-plumb columns must be corrected before adding more load (next tier) because each additional tier multiplies the eccentricity and increases the risk of progressive collapse. Use come-alongs or guy wires to plumb the column.',
  keyConcept:'Column plumb tolerance: typically ±1:500 per CISC. Correct out-of-plumb columns BEFORE adding additional loads or erecting higher tiers.'},

  {id:112,topic:'rigging',topicLabel:'Rigging & Hoisting',diff:'medium',
  text:"An ironworker is using a synthetic web sling to lift a steel plate. The plate has sharp edges that could contact the sling. What protection MUST be used?",
  options:['A) No protection needed — synthetic slings are rated for contact with steel','B) Use edge protection (corner protectors, softeners) or switch to a chain sling — sharp edges will cut through synthetic web slings','C) Reduce the Working Load Limit by 25% and proceed without edge protection','D) Double the synthetic sling to add strength against cutting'],
  answer:1,
  explanation:'<strong>Sharp edges will cut synthetic web slings even at loads well below the WLL.</strong> Synthetic slings (nylon, polyester) have no resistance to sharp metal edges. Use corner protectors, edge guards, or switch to chain slings or wire rope when lifting objects with sharp edges. This is not a load-reduction issue — a cut sling fails catastrophically regardless of load.',
  keyConcept:'Synthetic slings + sharp edges = prohibited without corner protection. Chain slings or wire rope slings are appropriate for sharp-edged loads without protection.'},

  {id:113,topic:'safety',topicLabel:'Safety & Fall Protection',diff:'medium',
  text:"An ironworker using a self-retracting lifeline (SRL) is working on a steel beam 5m above the next lower level. The SRL has a maximum arresting force of 6 kN and the worker weighs 100 kg. What is the approximate total fall distance if a fall occurs?",
  options:['A) 0.6m — SRL locks within 1 foot of fall','B) Approximately 1.8-2.4m including SRL lock distance, deceleration distance, and body height factor','C) 5m — SRL only prevents ground impact','D) 0.3m — SRL eliminates free fall completely'],
  answer:1,
  explanation:'<strong>SRL total fall distance is not zero.</strong> An SRL allows 0.3-0.6m of free fall before locking, plus 0.6-0.9m of deceleration distance during arrest, plus 1.5-1.8m of suspended body below the anchor. Total clearance required: approximately 1.8-2.4m below the anchor point. At 5m above the lower level, there is sufficient clearance. Always verify clearance before using an SRL.',
  keyConcept:'SRL clearance = free fall (0.6m) + deceleration (0.9m) + body height (1.8m) ≈ 3.3m below anchor. Verify clearance before use, especially near lower levels.'},

  {id:114,topic:'welding',topicLabel:'Welding & Joining',diff:'medium',
  text:"An ironworker-welder is completing a structural weld and notices arc blow causing the arc to deflect away from the joint, creating a poor weld profile. The process is SMAW with DC+ polarity. What is the MOST effective corrective action?",
  options:['A) Increase welding current to overcome the arc deflection','B) Switch to AC polarity, reposition the work lead, or angle the electrode toward the direction of blow','C) Change to a different electrode classification','D) Reduce arc length to compensate for deflection'],
  answer:1,
  explanation:'<strong>Arc blow occurs in DC welding when magnetic fields deflect the arc.</strong> Corrective actions: 1) Switch to AC (AC does not produce arc blow). 2) Move the work ground clamp closer to the weld (or place on both ends). 3) Angle the electrode into the direction of blow. 4) Weld toward the ground connection. 5) Reduce current. Arc blow is most common at ends of joints and near heavy metal sections.',
  keyConcept:'Arc blow: DC phenomenon caused by stray magnetic fields. Fix: switch to AC, reposition ground lead, angle electrode into blow direction, or weld toward ground.'},

  {id:115,topic:'blueprint',topicLabel:'Blueprints & Drawing',diff:'medium',
  text:"A structural drawing shows the symbol ↑ with a triangle pointing downward (▽) beside a weld symbol on a fillet weld callout. What does the downward triangle indicate?",
  options:['A) The weld is on the near side (arrow side) of the joint','B) The weld must be ground flush','C) The weld is a field weld — to be performed at the job site, not the fabrication shop','D) The weld requires non-destructive testing (NDT)'],
  answer:2,
  explanation:'<strong>A flag symbol (pennant/triangle on the reference line) indicates a field weld in AWS/CWB welding symbol notation.</strong> Field welds are performed at the erection site after steel is delivered. Shop welds are completed at the fabrication shop. The flag (triangular pennant) at the reference line-tail junction distinguishes site-welded connections from pre-fabricated connections, critical for erection sequencing.',
  keyConcept:'Welding symbol flags: Flag/pennant at reference line = field weld (on-site). All-around symbol (circle at flag junction) = weld continues all around. No flag = shop weld.'},

  {id:116,topic:'structural',topicLabel:'Structural Steel Erection',diff:'hard',
  text:"During erection of a steel structure, an ironworker notices the decking is buckling and the frame is deflecting more than expected as a concrete pour proceeds. What is the MOST likely cause and immediate action?",
  options:['A) Normal elastic deflection — continue the pour','B) Concrete pump hose is creating point loads — relocate pump hose and check shoring plan','C) Stop the pour immediately, evacuate, and notify the engineer — the structure may be overloaded or shores may be inadequate','D) Speed up the pour to reduce load duration'],
  answer:2,
  explanation:'<strong>Unexpected structural movement during a concrete pour is a serious warning sign of potential collapse.</strong> Possible causes: shores inadequate for design load, concrete is piling up (not spreading), formwork props have kicked out, or the deck load exceeds design. The safe action is to immediately stop the pour, ensure workers are clear of the affected area, and contact the engineer of record before proceeding. Progressive collapse can occur rapidly.',
  keyConcept:'Concrete pour monitoring: any unexpected deflection or movement = STOP immediately. Evacuate the area under and adjacent to the affected structure. Never accelerate a pour to outrun a developing problem.'},

  {id:117,topic:'rebar',topicLabel:'Rebar & Reinforcing',diff:'medium',
  text:"An ironworker is tying rebar for a suspended floor slab. The drawing calls for top bars (negative moment reinforcement) in the vicinity of column supports. The ironworker places these bars at the bottom of the slab instead. What is the structural consequence?",
  options:['A) No consequence — rebar works in tension or compression regardless of position','B) Top bars resist hogging moment (tension in top fiber) at supports — placing at the bottom reverses the reinforcement, causing potential failure at supports under live load','C) Minor consequence — the bars provide 75% of the required capacity in either position','D) No consequence — concrete carries tension at column supports'],
  answer:1,
  explanation:'<strong>Top reinforcement at column supports resists the hogging bending moment (negative moment) where the top fiber is in tension.</strong> Placing these bars at the bottom means the top fiber has no tension reinforcement at the critical moment. Concrete cannot carry tension — placing bars at the wrong position means the slab is unreinforced at the most critical stress location, leading to cracking and potential failure at service load.',
  keyConcept:'Top bars = negative moment (hogging) reinforcement at supports. Bottom bars = positive moment (sagging) at midspan. Placement is critical — wrong position = unrpeinforced at the peak moment location.'},

  {id:118,topic:'rigging',topicLabel:'Rigging & Hoisting',diff:'hard',
  text:"An ironworker must rig a 4,000 kg beam with an unknown centre of gravity. The beam is lifted with a spreader bar and two vertical wire rope slings of equal length. When lifted 150mm off the ground, one end rises higher than the other. What adjustment should be made?",
  options:['A) Add counterweights to the light end','B) Move the connection point on the spreader bar toward the heavy end (shorter distance from hook to heavy end) to balance the lift','C) Use longer slings on the heavy end to compensate','D) Increase crane boom angle to redistribute load'],
  answer:1,
  explanation:'<strong>To balance an uneven lift, move the crane hook attachment (or spreader bar pivot) toward the heavy end.</strong> With a spreader bar and equal-length slings, the pickup point must align over the centre of gravity for a level lift. Moving the connection toward the heavy end shortens the moment arm on that side, creating balance. A trial lift at low height before full elevation allows safe adjustment.',
  keyConcept:'Rigging balance: trial lift 150-300mm off ground to verify balance. Adjust pickup point toward heavy end. Never carry a grossly unbalanced load at full height.'},

  {id:119,topic:'safety',topicLabel:'Safety & Fall Protection',diff:'hard',
  text:"A gang of ironworkers is erecting steel 12m above grade. The controlled decking zone (CDZ) provisions allow workers within 3m of the leading edge to work without guardrails under specific conditions. Which of the following does NOT qualify as a condition for using the CDZ provision?",
  options:['A) Workers are wearing and using personal fall arrest systems (PFAS)','B) The CDZ has a designated competent person monitoring compliance','C) Decking bundles are placed to serve as barriers at the leading edge','D) No other falls hazards within the CDZ exist'],
  answer:2,
  explanation:'<strong>Decking bundles do NOT qualify as CDZ barriers.</strong> CDZ conditions (per provincial OH&S regulations and OSHA 1926 Subpart R): 1) Only decking work is performed. 2) Employees stay back 3m from edge unless using PFAS. 3) Decking is not used as a barrier (bundles shift and are removed). 4) A competent person monitors the zone. Decking bundles appear substantial but are not approved CDZ barriers — they move and are intentionally removed.',
  keyConcept:'CDZ valid conditions: PFAS in use OR 3m setback from edge. Competent person monitoring. NOT valid: decking bundles as barriers, non-decking work, or other hazards present.'},

  {id:120,topic:'structural',topicLabel:'Structural Steel Erection',diff:'medium',
  text:"An ironworker is placing shear studs on a composite steel beam using a drawn-arc stud gun. After welding, the inspection requires a bend test on 1% of studs per CSA S16. A stud is bent 30° and then straightened. The stud shows a cracked weld at the base. What is the required action?",
  options:['A) Accept the stud — bend testing is destructive and minor cracks are expected','B) Replace the failed stud with a new one, and test additional studs at twice the original rate to verify weld quality','C) Reject the entire beam — all studs must be replaced','D) Cut and re-weld the cracked stud base only'],
  answer:1,
  explanation:'<strong>CSA S16 shear stud inspection: failed bend test requires replacement of the failed stud and increased testing rate.</strong> If a stud cracks at the weld during a 30° bend test, the weld quality is suspect. Replace the failed stud with a new one welded with correct parameters. Increase subsequent inspection rate (typically double) to verify that adjacent studs are acceptable. A full beam replacement is not required for an isolated failure.',
  keyConcept:'Shear stud QC: 30° bend test, 1% per CSA S16. Failure = replace that stud + increase inspection rate. Weld failure causes: contamination, moisture, wrong current, worn ferrule.'}
"""

def main():
    f = ROOT / '442a.html'
    text = f.read_text(encoding='utf-8')
    close_idx = text.rfind('\n];')
    if close_idx < 0:
        sys.stdout.buffer.write(b'ERROR: could not find ]; in 442a.html\n')
        return
    new_text = text[:close_idx] + ',\n' + NEW_QUESTIONS.strip() + '\n' + text[close_idx:]
    f.write_text(new_text, encoding='utf-8')
    import re
    ids = re.findall(r'\bid:(\d+)', new_text)
    sys.stdout.buffer.write(f'442a.html: {len(ids)} questions total (was 100)\n'.encode())

if __name__ == '__main__':
    main()
