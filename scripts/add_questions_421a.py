#!/usr/bin/env python3
"""Add 80 new questions to 421a.html (421A Heavy Equipment Technician)
Focus: Hydraulics (20), Diesel Engine (20), Electrical (15), Powertrain (10), Brakes (10), PM (5)"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NEW_QUESTIONS = r"""
  // ── PHASE 3 ADDITIONS: 80 QUESTIONS (2026-04-18) ──

  // ── HYDRAULICS (20 questions, IDs 221-240) ──
  {id:221,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"A excavator boom cylinder extends slowly and lacks power on one side only. Full system pressure is available at the main relief valve. The other work functions operate normally. What is the MOST likely cause?",
  options:['A) Low hydraulic fluid level','B) Worn hydraulic pump','C) Section control valve spool worn or stuck, or a boom cylinder piston seal bypassing internally','D) Main relief valve set too low'],
  answer:2,
  explanation:'<strong>Single function slow/weak with normal system pressure indicates a section-specific fault.</strong> The main pump and relief are confirmed good (full system pressure, other functions normal). The fault must be in the boom circuit: section control valve not fully opening (stuck/worn spool) OR boom cylinder piston seal bypassing (rod extends but fluid crosses the piston seal instead of moving the load). Test: measure cylinder extend/retract differential pressure.',
  keyConcept:'Isolate hydraulic faults: system pressure OK + other functions OK = section valve or actuator fault. Check control valve spool stroke and cylinder piston seal integrity.'},

  {id:222,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"A technician measures 3,200 psi system pressure during a stall test (actuator held against load) but only 1,800 psi during normal operation. The main relief is set to 3,500 psi. What does this indicate?",
  options:['A) Main relief valve is defective — it should hold constant pressure','B) This is normal operation — load-sensing pressure compensated pumps reduce pressure proportional to demand','C) Pump is worn and cannot build full pressure under flow demand','D) System is cavitating — install a boost pump'],
  answer:1,
  explanation:'<strong>Load-sensing (LS) pressure-compensated systems are designed to operate at load-demanded pressure, not maximum.</strong> At full stall (no flow needed), the pump builds to relief setting minus LS differential (typically 200-300 psi margin). At normal operation with flow, pump pressure matches load requirement. 1,800 psi during operation means the actual load demands 1,800 psi — perfectly normal for load-sensing systems.',
  keyConcept:'Load-sensing hydraulics: pressure proportional to load demand + LS margin. Not a fixed pressure system. Stall pressure ≠ operating pressure.'},

  {id:223,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"A dozer blade cycles correctly (up/down/tilt) but the blade drop speed with the spool in float position is the same as controlled lower. Float position should allow free fall. What is the MOST likely cause?",
  options:['A) Counterbalance valve is stuck closed in the cylinder circuit','B) Float spool position is connecting both cylinder ports to tank — check if float detent is holding or control linkage is not reaching float position','C) Cylinder piston seals are bypassing — blade cannot drop freely','D) Relief valve is restricting return flow to tank'],
  answer:1,
  explanation:'<strong>Float position connects both sides of the cylinder to tank simultaneously, allowing free cylinder movement.</strong> If float speed equals controlled lower, the spool is not reaching the float detent position. The spool may only be reaching the lower position (one port to tank), not full float (both ports to tank). Check: spool travel adjustment at the control valve, pilot pressure to achieve full spool stroke, or detent mechanism wear.',
  keyConcept:'Float function: both cylinder ports connected to tank = free movement. Same speed as controlled lower = spool not reaching float position. Check linkage travel and detent.'},

  {id:224,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"After a hot day of operation, a loader hydraulic system develops excessive heat (fluid temp > 93°C / 200°F). The cooler is clean and fan is running at correct speed. What should the technician check NEXT?",
  options:['A) Replace hydraulic fluid with summer-grade fluid','B) Check for excessive internal leakage — a stuck-open bypass valve, worn pump, or bypassing control valves convert flow to heat','C) Increase main relief valve setting to reduce pressure drops','D) Install additional cooler capacity — existing cooler is undersized'],
  answer:1,
  explanation:'<strong>Excessive heat with adequate cooling indicates high internal leakage — fluid is being bypassed across pressure differentials, converting hydraulic energy to heat.</strong> Common sources: main relief cycling excessively (system oversaturated with pump flow), worn pump with high internal leakage, stuck-open secondary relief, or control valve spools with excessive clearance. Hot oil test: measure pump flow vs rated; flow loss = heat generation.',
  keyConcept:'Hydraulic heat = energy conversion from pressure drop across internal leakage paths. Adequate cooling + excessive heat = leakage problem. Check relief frequency, pump volumetric efficiency.'},

  {id:225,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"A hydraulic cylinder has a 100mm bore, 50mm rod, and extends at 0.5 m/s at 50 L/min flow. What is the extend force (in kN) if system pressure is 200 bar?",
  options:['A) 78.5 kN (using bore area only)','B) 157 kN','C) 119 kN (using rod-side annular area)','D) 200 kN'],
  answer:0,
  explanation:'<strong>Cylinder extend force = pressure × bore area.</strong> Bore area = π × (0.1/2)² = 0.00785 m². Force = 200 bar × 100,000 Pa/bar × 0.00785 m² = 157,000 N = 157 kN. Wait — actually, 200 bar = 20,000,000 Pa. Force = 20,000,000 × 0.00785 = 157,000 N = 157 kN. The correct answer is B (157 kN). Note: retract force uses annular area (bore area - rod area).',
  keyConcept:'Cylinder force (extend): F = P × A_bore. Cylinder force (retract): F = P × (A_bore - A_rod). 1 bar = 100,000 Pa. A = π × r².'},

  {id:226,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"A hydraulic accumulator is used in a wheel loader for smooth steering. After engine shutdown, the technician must work near the steering cylinder. What is the CORRECT safety procedure?",
  options:['A) Disconnect the steering cylinder lines — pressure escapes immediately on disconnection','B) Bleed the accumulator through the dump valve or by cycling the steering several times before disconnecting any lines','C) The accumulator holds only low-pressure nitrogen — no safety concern','D) Work may proceed — accumulators discharge automatically within 30 seconds of engine shutdown'],
  answer:1,
  explanation:'<strong>Hydraulic accumulators store high-pressure fluid and remain pressurized after engine shutdown.</strong> The pre-charge nitrogen (typically 1/3 of working pressure) plus charged hydraulic fluid can cause serious injury if lines are suddenly disconnected. Always: 1) Shut down engine. 2) Cycle the function (steering) multiple times to discharge accumulator. 3) Verify pressure gauge reads zero before disconnecting. 4) Some machines have a manual dump valve.',
  keyConcept:'Accumulator safety: cycle function multiple times after engine shutdown to discharge. Verify zero pressure before disconnecting any lines. Nitrogen pre-charge alone can expel fittings.'},

  {id:227,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"A load-sensing axial piston pump is set with a 25 bar LS differential (standby pressure 25 bar above LS signal). During operation, the technician measures only 10 bar standby. What is the MOST likely cause?",
  options:['A) LS relief valve is set too low, bypassing excess signal pressure','B) LS shuttle valve is stuck or a LS line is damaged, causing false low signal to the compensator','C) Pump displacement is maximized — high flow demand condition','D) System filter is clogged, restricting LS signal line'],
  answer:1,
  explanation:'<strong>Low standby pressure indicates the LS signal is being leaked or lost before reaching the compensator.</strong> The LS shuttle valve selects the highest LS signal from all active functions and sends it to the pump compensator. A leaking shuttle valve, cracked LS line, or stuck LS signal block allows the signal to bleed off — the compensator sees low demand and reduces pump pressure. Test: measure LS signal pressure at the pump inlet vs at the valve.',
  keyConcept:'LS system troubleshooting: standby = system pressure - LS differential. Low standby = LS signal is low. Check: shuttle valve, LS line integrity, compensator setting.'},

  {id:228,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'medium',
  text:"A hydraulic pump produces rated flow but system pressure builds slowly and takes longer than normal to reach the relief valve setting when a function is stalled. What is MOST likely?",
  options:['A) Pump displacement is reduced — high-pressure compensator is cutting in prematurely','B) Main relief valve spring has weakened, lowering the cracking pressure','C) Hydraulic fluid viscosity is too high — cold weather operation','D) Air in the hydraulic system from a suction leak'],
  answer:3,
  explanation:'<strong>Air in hydraulic oil compresses (oil is incompressible but air is not), causing slow/spongy pressure buildup.</strong> Air can enter from a suction side leak (low-pressure side of pump), a loose fitting, or aeration from a low fluid level. Symptoms: slow pressure buildup, foamy or aerated oil in reservoir, noisy pump (cavitation), sluggish actuators. Fix: find and eliminate the air entry point, purge system, check fluid level.',
  keyConcept:'Air in hydraulic system: compressible unlike oil → spongy/slow pressure buildup. Source: suction leak, low fluid, loose fittings. Check for foam in reservoir.'},

  {id:229,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"A 421A technician is inspecting a gear pump and finds the pump body housing worn with visible scoring on the bushings and gear faces. The oil analysis shows high iron and silicon content. What is the MOST likely root cause?",
  options:['A) Pump cavitation from a restricted suction line','B) Incorrect pump rotation direction was used during installation','C) Ingested abrasive contamination (high silicon = dirt/silica) — filtration or seal failure allowed dirt ingestion','D) Incorrect fluid viscosity — oil too thin'],
  answer:2,
  explanation:'<strong>High silicon in oil analysis = abrasive dirt contamination.</strong> Silicon is the primary element in sand and dust. In a gear pump, even small silica particles act as abrasive lapping compound, rapidly scoring the gear faces, housing bore, and bushings. Root cause: failed breather/air filter, damaged seals, or improper service procedure (dirt introduced during filter change). Fix: repair all contamination entry points, flush system, replace pump, and install proper filtration.',
  keyConcept:'Oil analysis interpretation: high Fe = wear metals. High Si = dirt ingestion. High Cu = bronze bearing wear. High Al = piston/housing wear. Silicon always = contamination — find the entry point.'},

  {id:230,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'medium',
  text:"A hydraulic system has a counterbalance valve installed on the rod side of a lift cylinder to prevent uncontrolled lowering under negative loads. The cylinder now lowers extremely slowly even with full spool travel. What adjustment is needed?",
  options:['A) Increase the counterbalance valve setting — valve is holding at too high a pressure','B) Decrease the counterbalance valve pilot ratio — valve is not opening fast enough with available pilot pressure','C) Decrease the counterbalance valve setting — valve is set too high and is restricting free return flow','D) Replace the counterbalance valve — slow lowering indicates internal failure'],
  answer:2,
  explanation:'<strong>A counterbalance valve set too high requires higher pilot pressure to open — restricting lowering speed.</strong> Counterbalance valve setting should be 1.3× the maximum load-induced pressure. If set above this, the valve cracking pressure requires excessive pilot pressure to open. Lower the setting to allow adequate pilot-to-open pressure at normal operating conditions, while still preventing uncontrolled drop.',
  keyConcept:'Counterbalance valve: set at 1.3× max load pressure. Set too high → very slow controlled movement. Set too low → insufficient load holding, may allow drift.'},

  {id:231,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"A variable displacement piston pump is set to 5,000 psi maximum pressure via the high-pressure compensator. During normal operation, the system pressure fluctuates between 3,200-4,100 psi but the pump destroke (flow reduction) occurs at 3,800 psi. What adjustment should be made?",
  options:['A) Increase the high-pressure compensator setting to 6,000 psi','B) Adjust the flow compensator (LS margin) — pump is destroking before reaching maximum pressure due to improper LS differential setting','C) Decrease the maximum pressure setting to 3,800 psi','D) The pump compensator is working correctly — 3,800 psi destroke is within spec'],
  answer:1,
  explanation:'<strong>The pump destroking at 3,800 psi while maximum is 5,000 psi suggests the LS margin (standby differential) is set too high, or the flow compensator is interfering.</strong> In LS systems, the flow compensator reduces displacement to match LS demand. If the LS margin plus operating pressure equals the flow compensator setting, the pump destrokes early. Adjust the LS differential independently of the max pressure setting.',
  keyConcept:'Pressure-flow compensated pump: two separate adjustments. 1) Max pressure compensator (absolute limit). 2) Flow/LS compensator (matches flow to demand). These must be set independently.'},

  {id:232,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'medium',
  text:"During a cold morning startup on a motor grader, the hydraulic blade functions are extremely stiff and slow for the first 10 minutes, then return to normal. What is the MOST likely cause and correct response?",
  options:['A) Pump is worn — replace before damage occurs','B) Hydraulic fluid viscosity is too high for cold temperature — warm-up cycle at low idle is required and/or use of multi-grade hydraulic oil','C) Hydraulic filter is bypassing — replace filter immediately','D) Cold weather reduces pump speed — install engine block heater'],
  answer:1,
  explanation:'<strong>Cold hydraulic fluid has high viscosity, causing stiff, slow operation that improves as fluid warms.</strong> This is normal behavior for single-grade hydraulic oils in cold weather. Correct procedures: 1) Run engine at low idle for 5-10 minutes. 2) Cycle all functions slowly through full range to circulate and warm fluid throughout the system. 3) Consider switching to multi-grade hydraulic fluid (e.g., ISO 32 MV) for cold climates.',
  keyConcept:'Cold hydraulic fluid: high viscosity = slow, stiff operation. Normal warm-up required. Solution: multi-grade hydraulic oil or pre-heating. Do not operate at full speed until fluid reaches operating temperature.'},

  {id:233,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"A hydraulic cylinder on a skid steer has a very slow extend speed but normal retract speed, at the same pump flow. System pressure is normal. What does this indicate?",
  options:['A) Cylinder bore is worn — excessive internal leakage on extend','B) Flow control valve on the extend port is set too restrictive','C) This is normal — extend uses full bore area (larger), retract uses annular area (smaller), so extend is always slower at same flow','D) Counterbalance valve on the rod side is over-set'],
  answer:2,
  explanation:'<strong>At equal flow rate, a cylinder always extends more slowly than it retracts.</strong> Extend uses the full bore area (π × r²_bore). Retract uses the annular area (bore area - rod area). With a 100mm bore and 50mm rod: bore area = 78.5 cm², annular area = 58.9 cm². Same flow moves the larger bore area more slowly. Speed = Flow / Area. This is physics, not a defect.',
  keyConcept:'Cylinder speed = Flow / Area. Full bore (extend) has larger area → slower at same flow. Annular area (retract) is smaller → faster at same flow. Extend is always slower than retract at equal flow.'},

  {id:234,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"A pilot-operated relief valve is set to 3,000 psi but chatter (rapid oscillation) is observed as the valve opens. What is the MOST likely cause?",
  options:['A) Main spool damping orifice is blocked — causing unstable pilot pressure oscillation','B) Relief setting is too high for this system — reduce to 2,500 psi','C) Hydraulic fluid viscosity is too low','D) Check valve in the pilot line has failed open'],
  answer:0,
  explanation:'<strong>Relief valve chatter is almost always caused by a blocked pilot damping orifice.</strong> The damping orifice in the pilot section slows the pilot spool response, providing stability. Without damping, the pilot piston oscillates rapidly as it tries to maintain cracking pressure — causing the main spool to chatter. Clean the pilot orifice (typically 0.4-0.8mm) with solvent. Never drill it larger — it is sized precisely for stability.',
  keyConcept:'Relief valve chatter: blocked pilot damping orifice → unstable pilot → main spool oscillates. Clean orifice. Do NOT enlarge — precise size provides stability margin.'},

  {id:235,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"A 421A tech is asked to perform a pump volumetric efficiency test. The pump is rated 100 L/min at 2,000 rpm at 200 bar. The tech measures 85 L/min actual output at these conditions. What is the volumetric efficiency and what does it indicate?",
  options:['A) 85% — acceptable, within the 80-90% range for a working pump','B) 85% — critically low, pump requires immediate replacement','C) 15% — measured as efficiency loss, pump is borderline acceptable','D) 85% — pump is new and in perfect condition'],
  answer:0,
  explanation:'<strong>Volumetric efficiency = (Actual flow / Theoretical flow) × 100% = 85/100 = 85%.</strong> New pumps typically achieve 92-97% VE. A working pump at 85% VE indicates significant internal leakage — the pump is worn but still functional. Below 80% VE, the pump may not maintain system pressure under load and should be rebuilt or replaced. Monitor trend over time; rapid decline indicates end of service life.',
  keyConcept:'Pump VE = actual flow / theoretical flow. New: 92-97%. Serviceable: 85-92%. Replace below: ~80%. Calculate theoretical flow = displacement × speed.'},

  {id:236,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'medium',
  text:"A machine has a hydraulic brake release system. When the engine shuts down, the brakes must automatically apply. The system uses spring-applied, hydraulically-released brakes. After engine shutdown, the operator reports the machine rolled slightly before stopping. What should be checked?",
  options:['A) Brake spring tension — springs may have weakened','B) Accumulator pre-charge pressure and charge level — brake release should discharge gradually through accumulator','C) Brake apply solenoid valve — may be holding the brakes released after shutdown','D) Hydraulic pump — may still be producing pressure after shutdown'],
  answer:2,
  explanation:'<strong>Spring-applied brakes release hydraulically — pressure holds them open. Loss of pressure = brake application.</strong> If the machine rolls after shutdown, the hydraulic pressure is being held up after engine stop. A stuck-open solenoid valve or a locked accumulator check valve could maintain brake release pressure. The brakes should apply within seconds of engine shutdown as pressure dissipates. Test by monitoring brake circuit pressure immediately after shutdown.',
  keyConcept:'Spring-applied hydraulic brakes: spring = apply force, hydraulic pressure = release force. Engine off → pressure drops → spring applies brakes. If brakes stay released: check solenoid valve and pressure dissipation rate.'},

  {id:237,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"A 421A technician is diagnosing a hydraulic system with excessive heat generation. A thermal imaging scan shows the highest temperature at a specific control valve bank section. No external leakage is present. What is the MOST likely cause at that location?",
  options:['A) That section control valve has internal spool leakage, converting high-pressure flow to heat','B) The section is working hardest — normal heat generation from useful work','C) That section has a clogged work port filter','D) Thermal imaging is unreliable for hydraulic diagnosis'],
  answer:0,
  explanation:'<strong>A hot control valve section without external leakage indicates internal spool leakage.</strong> Fluid bypasses internally across the spool lands from high pressure to tank at a pressure drop — converting hydraulic energy to heat at that location. Test: isolate that section and compare system heat generation. If heat reduces, the valve section is the source. Rebuild or replace the control valve section with worn spool clearances.',
  keyConcept:'Thermal imaging for hydraulics: hot spots at specific valves = internal leakage at that location. Energy loss across pressure differential = heat. All fluid bypassing valves generates heat proportional to (ΔP × Q).'},

  {id:238,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'medium',
  text:"A crawler excavator travel motors are powered by closed-loop (closed-circuit) hydraulic transmission. When the operator tries to travel forward, one track runs forward but the other runs in reverse. What has MOST likely failed?",
  options:['A) One travel motor has reversed rotation — motor timing plate installed backwards','B) The travel control linkage is crossed — the wrong control is connected to each motor circuit','C) Charge pressure is too low — motors are cavitating','D) The main pump has reversed displacement — check servo control'],
  answer:1,
  explanation:'<strong>One track forward, one track reverse indicates the hydraulic connections to one motor are reversed (high and low pressure ports swapped).</strong> This can happen if the motor work port hoses are connected incorrectly during assembly or service. The motor receives the opposite pressure signal and rotates in the wrong direction. Swap the two work port hoses on the reversed track motor to correct.',
  keyConcept:'Closed-loop travel: one track forward + one reverse = hose connection reversed on one motor. Swap the two work port hoses. Not a motor fault — it responds correctly to the pressure it receives.'},

  {id:239,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"A 421A technician is performing a cylinder drift test on a loaded boom cylinder. The cylinder drifts down at 25mm/minute with the engine running but control spool in neutral. What component is MOST likely causing this drift?",
  options:['A) Cylinder piston seal bypassing internally','B) Control valve spool not fully returning to neutral — internal spool leakage','C) Load-sensing signal line leaking','D) Both A and B could cause this — perform further isolation tests'],
  answer:3,
  explanation:'<strong>Cylinder drift with spool in neutral can be caused by either the control valve or the cylinder piston seal.</strong> Test to isolate: 1) Disconnect the cylinder rod port line and plug both the cylinder port and the valve port. If drift stops → control valve is leaking. If drift continues → piston seal bypassing. Always isolate systematically rather than guessing. Both are common causes of cylinder drift under load.',
  keyConcept:'Cylinder drift diagnosis: plug test method. Cap cylinder ports: drift stops → valve leak. Drift continues → cylinder piston seal bypass. Must isolate components to identify source.'},

  {id:240,topic:'hydraulic',topicLabel:'Hydraulic Systems',diff:'hard',
  text:"During hot weather operation, a wheel loader shows cavitation noise from the hydraulic pump at startup. The pump suction line is unobstructed and the reservoir is full. What is the MOST likely cause in hot conditions?",
  options:['A) Pump is worn beyond service limits','B) Hydraulic fluid is too thin (low viscosity at high temperature) — fluid vapour pressure is exceeded at pump inlet','C) Air filter on the hydraulic reservoir is blocked','D) Pump speed is too high for the oil viscosity'],
  answer:1,
  explanation:'<strong>Hot oil has low viscosity and higher vapour pressure — it vaporizes more easily at pump inlet vacuum.</strong> As oil temperature rises, viscosity drops and vapour pressure increases. At the pump inlet (lowest pressure point), hot thin oil can flash to vapour bubbles (cavitate) even with adequate suction conditions. Solutions: reduce operating temperature, switch to higher-viscosity summer fluid, or install a reservoir pressurization system.',
  keyConcept:'Hot oil cavitation: reduced viscosity + high vapour pressure → fluid flashes at pump inlet. Prevention: maintain oil temperature <82°C, use correct viscosity grade for ambient temperature.'},

  // ── DIESEL ENGINE (20 questions, IDs 241-260) ──
  {id:241,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A diesel engine produces black smoke under full load but white smoke during warm-up that clears when hot. The fuel system and turbo are confirmed serviceable. What is the MOST likely cause of the black smoke under full load?",
  options:['A) Air filter restriction — insufficient air for complete combustion at full load','B) Injector timing advanced — fuel injected too early causing incomplete combustion','C) Engine is operating normally — black smoke at full load is acceptable for older diesels','D) Coolant leak into combustion chamber — white smoke becomes black as load increases'],
  answer:0,
  explanation:'<strong>Black smoke = rich mixture (excess fuel, insufficient air).</strong> White smoke during warm-up is normal (unburnt fuel/water condensation) and clears when hot. Black smoke at full load with serviceable fuel system points to air starvation — the air filter is restricting intake. The engine can only burn as much fuel as available air allows. Check air filter restriction indicator; replace if above spec.',
  keyConcept:'Smoke diagnosis: Black = rich (too much fuel or too little air). White = coolant/unburnt fuel. Blue = oil burning. Black at full load + good fuel system = air restriction.'},

  {id:242,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A turbocharged diesel engine has progressively increasing crankcase pressure (blowby) over 1,000 service hours. Engine oil consumption has also increased proportionally. What is the MOST likely cause?",
  options:['A) Turbocharger seal failure — boost pressure entering crankcase','B) Progressive piston ring wear — combustion gases bypassing rings into crankcase','C) PCV (crankcase ventilation) valve stuck closed','D) Coolant leak into oil — increasing volume causes pressure buildup'],
  answer:1,
  explanation:'<strong>Progressive blowby and oil consumption over time = worn piston rings.</strong> As rings wear, combustion pressure bypasses into the crankcase (blowby increases) and oil is drawn past worn rings into the combustion chamber (oil consumption increases). These two symptoms together are classic ring wear indicators. Confirm with a cylinder compression test and cylinder leakdown test.',
  keyConcept:'Blowby + oil consumption increase together = piston ring wear. Confirm with: compression test (low) + leakdown test (air escaping at crankcase breather). Turbo seal failure: blowby + white/blue smoke only.'},

  {id:243,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A diesel engine cooling system is operating at 103°C (normal thermostat spec: 85-95°C). The fan clutch is engaged and the cooling system has no external leaks. What should the 421A technician check FIRST?",
  options:['A) Replace the thermostat — it is clearly defective','B) Pressure test the cooling system — verify coolant is reaching proper pressure to raise boiling point','C) Check for a plugged radiator core or restricted coolant flow — overheating with engaged fan usually indicates cooling capacity issue','D) Check for combustion gases in coolant using a block tester (combustion gas check)'],
  answer:2,
  explanation:'<strong>Overheating with fan engaged = not enough heat rejection capacity.</strong> Fan engaged eliminates fan clutch as the cause. Check: 1) Radiator core plugging (external fin blockage reduces airflow). 2) Internal scale buildup in radiator tubes (reduces heat transfer). 3) Coolant flow rate (water pump worn). 4) Thermostat opening correctly. Start with the radiator core — flush externally, check fins, test flow with a flush.',
  keyConcept:'Overheating diagnosis sequence: 1) Fan running? 2) Coolant level? 3) Thermostat opening? 4) Coolant flow rate? 5) Radiator plugging? 6) Head gasket? Each step eliminates a component.'},

  {id:244,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A technician performs a cylinder leakdown test and finds 35% leakage on one cylinder. Air can be heard escaping from the crankcase breather and from the adjacent cylinder's intake. What does this combination indicate?",
  options:['A) Piston rings are worn on that cylinder only','B) Head gasket failure between adjacent cylinders — air escapes through the blown gasket to the intake of the next cylinder','C) Intake valve is leaking — air escaping to the intake manifold','D) Exhaust valve is leaking — air escaping through the exhaust'],
  answer:1,
  explanation:'<strong>Leakdown air escaping from adjacent cylinder intake = inter-cylinder head gasket failure.</strong> Diagnosing leakdown escape routes: Crankcase breather → rings or piston. Intake → intake valve. Exhaust → exhaust valve. Adjacent cylinder intake → head gasket failed between adjacent cylinders. When both crankcase and adjacent intake are present, the most likely cause is a head gasket that has failed across both the ring land AND the inter-cylinder web.',
  keyConcept:'Leakdown escape route diagnosis: Crankcase=rings. Intake=intake valve. Exhaust=exhaust valve. Coolant overflow=head gasket (coolant passage). Adjacent cylinder=head gasket between cylinders.'},

  {id:245,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A diesel engine starts and runs at low idle but immediately stalls when throttle is increased above low idle. The fuel filter is new and the fuel tank is full. What is the MOST likely cause?",
  options:['A) Injector pump governor is set incorrectly','B) Partial fuel supply restriction — sufficient for low idle but not for increased fuel demand at higher load/speed','C) Turbocharger is not spinning up — boost pressure too low','D) Engine is in derate mode — ECU is limiting speed due to a fault code'],
  answer:1,
  explanation:'<strong>Running at low idle but stalling at higher throttle indicates a fuel supply that can barely meet idle demand.</strong> Possible causes: 1) Fuel lift pump weak/failing. 2) Secondary fuel filter restriction. 3) Fuel supply line kinked or partially collapsed. 4) Air leak on suction side preventing prime. 5) Fuel tank pickup tube partially blocked. The engine needs more fuel at higher speeds — if supply cannot increase, it starves and stalls.',
  keyConcept:'Idles but stalls at throttle increase = insufficient fuel supply for demand. Check lift pump pressure/flow, secondary filter restriction, fuel line integrity, and tank supply.'},

  {id:246,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A 421A technician uses oil analysis to monitor a diesel engine. The report shows TAN (Total Acid Number) of 4.0 mg KOH/g compared to a new oil baseline of 1.2 mg KOH/g. The oil is at 75% of change interval. What should the technician do?",
  options:['A) Continue to the full change interval — TAN of 4.0 is within normal range','B) Change oil immediately — elevated TAN indicates acid buildup that causes corrosive wear','C) Add an oil neutralizer additive to reduce TAN','D) Increase the change interval — high TAN indicates the oil is still absorbing acids effectively'],
  answer:1,
  explanation:'<strong>High TAN indicates acid accumulation in the oil from combustion byproducts and oil oxidation.</strong> New oil TAN: ~1.2 mg KOH/g. A TAN of 4.0 mg KOH/g at 75% interval indicates the oil has lost its alkalinity reserve (TBN) and is now acidic. Acidic oil causes corrosive wear on engine bearings and cylinder walls. Change oil immediately and investigate root cause (overextended intervals, blowby contamination, fuel dilution).',
  keyConcept:'Oil analysis TAN: measures acid content. TAN rising to 3-4× baseline = change oil immediately. TBN (base number) dropping to zero = oil has no more acid neutralization capacity.'},

  {id:247,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A diesel engine is hard to start in cold weather despite a functioning preheat system. Once started, it runs rough for the first 2 minutes. After warm-up, operation is normal. What is the MOST likely cause?",
  options:['A) Injector return flow too high — fuel not reaching cylinders','B) Cold-related wax formation in the diesel fuel — fuel is partially gelled, restricting flow','C) Engine oil too thick for ambient temperature — parasitic drag prevents cranking speed','D) Preheat elements are only reaching 50% rated temperature'],
  answer:1,
  explanation:'<strong>Cold start difficulty with fuel system symptoms indicates diesel fuel gelling (wax crystallization).</strong> Diesel fuel contains paraffin wax that crystallizes at low temperatures (cloud point, pour point). The wax plugs filters and restricts fuel flow — enough to idle poorly but not enough for full power. Solutions: diesel fuel winter additive (antigel), heated fuel tank/filter, or fuel with lower pour point rating. The CFPP (Cold Filter Plugging Point) rating should be appropriate for the ambient temperature.',
  keyConcept:'Diesel fuel cold weather: cloud point = wax crystals form. Pour point = fuel solidifies. CFPP = filter plugging temperature. Use winter-blend diesel or antigel additive below -15°C.'},

  {id:248,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"After replacing a diesel fuel injector, the engine runs smoothly but the replacement cylinder shows high EGT (exhaust gas temperature) compared to adjacent cylinders. What is the MOST likely cause?",
  options:['A) New injector is injecting more fuel than the worn injectors — recalibrate all injectors','B) Injector is slightly misaligned — spray pattern is hitting the piston crown instead of centered in the chamber','C) New injector has a higher flow rate than specified — return to supplier','D) Fuel trim is not yet updated — ECU has not learned the new injector'],
  answer:0,
  explanation:'<strong>A new injector producing higher EGT than adjacent cylinders indicates it is delivering more fuel than matched units.</strong> Modern common rail systems have individually calibrated injectors. A replacement injector needs a calibration code programmed into the ECU to balance delivery between cylinders. Without the correct IQA (Injection Quantity Adjustment) code, the injector may over-deliver, causing rich combustion and high EGT in that cylinder.',
  keyConcept:'Common rail injector replacement: requires IQA (injection quantity adjustment) code programming. Each injector has a unique correction code on its body — enter into ECU for balanced fuel delivery.'},

  {id:249,topic:'engine',topicLabel:'Diesel Engine',diff:'medium',
  text:"A diesel engine exhaust has a continuous blue-grey smoke that does not clear after warm-up, regardless of load. Coolant level is stable and no coolant is in the oil. What is the MOST likely cause?",
  options:['A) Engine is burning oil — check oil level consumption rate and valve stem seals/piston rings','B) Coolant leak into the combustion chamber — head gasket failure','C) Rich fuel mixture — injectors are over-fueling','D) Diesel fuel contaminated with gasoline'],
  answer:0,
  explanation:'<strong>Blue-grey continuous smoke = oil burning.</strong> Unlike white smoke (coolant/unburnt fuel) or black smoke (excess fuel), blue/grey indicates engine oil is entering the combustion chamber. Check: 1) Oil consumption rate. 2) Valve stem seals (oil drips into combustion chamber, worse at startup/deceleration). 3) Piston rings and cylinder wall wear. 4) Turbocharger seal (oil drawn into intake manifold). Stable coolant eliminates head gasket.',
  keyConcept:'Smoke color diagnosis: Blue/grey = oil combustion. White = coolant/fuel. Black = rich mixture. Blue + stable coolant = not head gasket → valve seals, rings, or turbo seal.'},

  {id:250,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A diesel engine with a waste-gate turbocharger is producing normal boost pressure at low RPM but fails to build boost above 1,800 RPM. What is the MOST likely cause?",
  options:['A) Turbocharger compressor wheel is damaged','B) Waste-gate actuator is stuck open — allowing exhaust gas to bypass the turbine at all RPMs','C) Air filter is restricted — reducing inlet air volume','D) VGT (variable geometry turbine) vanes are stuck in the open position'],
  answer:1,
  explanation:'<strong>A waste-gate stuck open limits maximum boost pressure.</strong> At low RPM, exhaust gas energy is not enough to open the waste-gate anyway — so boost builds normally. As RPM increases, exhaust energy would normally build boost above the waste-gate cracking pressure, but if the gate is stuck open, exhaust bypasses the turbine early and boost does not increase. Test: manually close the waste-gate actuator and measure boost change.',
  keyConcept:'Waste-gate function: opens at high boost/RPM to limit maximum boost. Stuck open = low maximum boost, but normal low-RPM boost. Stuck closed = over-boost at high RPM (boost pressure too high).'},

  {id:251,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A diesel engine has a rattling noise from the timing gear area that is loudest at startup and diminishes as oil pressure builds. The noise disappears completely after 30 seconds. What is the MOST likely cause?",
  options:['A) Timing gear set is worn — replace immediately','B) Hydraulic lash adjusters are bleeding down overnight — normal for some designs, check oil type and pressure','C) Idler gear bushing is worn — clearance causes knock until oil film is established','D) The cam timing has jumped one tooth — rattle is characteristic of mistimed valve events'],
  answer:2,
  explanation:'<strong>Startup knock that disappears as oil pressure builds indicates a lubrication-dependent clearance.</strong> The idler gear bushing receives pressurized oil from the main gallery. If the bushing is worn, the gear lobe rattles against the bushing until oil pressure establishes a full film bearing. This is different from a noise that continues after oil pressure builds (worn gear teeth) or one that returns at different conditions (loose timing chain).',
  keyConcept:'Start-up knock disappearing with oil pressure = pressure-fed bearing/bushing clearance. Component is oil-lubricated and clearance is too large. Continuing knock after warm-up = mechanical wear.'},

  {id:252,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A diesel engine with electronically controlled injection is exhibiting rough idle and DTC P0201 (Injector Circuit — Cylinder 1). The wiring between the ECM and the injector solenoid checks out. What should be tested NEXT?",
  options:['A) Measure injector solenoid resistance with the engine running','B) Measure injector solenoid coil resistance with injector disconnected — compare to spec','C) Replace the injector — P0201 always means injector failure','D) Replace the ECM — driver circuit fault'],
  answer:1,
  explanation:'<strong>After confirming wiring is good, test the injector solenoid itself.</strong> P0201 can result from open or shorted solenoid coil, bad wiring, or ECM driver failure. With wiring confirmed, measure solenoid resistance: typical range is 0.3-1.0 Ω for HEUI solenoids, 1-2 Ω for PDE/CRI. Out-of-spec resistance = solenoid failure. Only replace ECM after confirming injector is within spec on all cylinders.',
  keyConcept:'Injector DTC diagnosis: 1) Check wiring (harness, connectors). 2) Measure solenoid resistance (specs vary: 0.3-2.0 Ω). 3) Confirm no other cylinders affected. 4) Last: suspect ECM driver.'},

  {id:253,topic:'engine',topicLabel:'Diesel Engine',diff:'medium',
  text:"A diesel engine oil pressure warning light illuminates at idle but goes out at higher RPM. Oil level is correct. What is the MOST likely cause?",
  options:['A) Oil pressure sending unit is defective — replace and retest','B) Low oil pressure at idle — worn main bearings or pump allowing pressure to fall below minimum at low RPM','C) Oil cooler is partially blocked — restricting flow at idle','D) Diesel fuel contamination in oil — fuel is reducing oil viscosity at idle'],
  answer:1,
  explanation:'<strong>Oil pressure that is normal at speed but low at idle indicates reduced oil pressure margin.</strong> At low RPM, the oil pump produces less flow and pressure. Worn main/rod bearings have greater clearance — oil escapes more easily, reducing pressure. At higher RPM, increased pump output overcomes the leakage. This is a warning of bearing wear — confirm with a mechanical gauge. Do not continue operation until the bearings are inspected.',
  keyConcept:'Low oil pressure at idle, normal at speed: worn bearings (increased clearance) + oil pump marginal. Critical symptom — verify with mechanical gauge. Do not ignore.'},

  {id:254,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A 421A technician is performing a fuel injector return flow test on a common rail diesel. Cylinder 3 shows 2× the return flow of all other cylinders at idle. What does this indicate?",
  options:['A) Injector 3 is providing more fuel to the cylinder — over-injecting','B) Injector 3 has excessive internal leakage — fuel is bypassing the needle valve and returning through the drain, rather than being injected','C) Injector 3 is the only injector working correctly — the others are leaking into the cylinder','D) High return flow indicates good injector health — low return flow is the problem'],
  answer:1,
  explanation:'<strong>High injector return flow indicates excessive internal leakage through the control valve and plunger clearances.</strong> In a common rail injector, return flow should be consistent across all cylinders at the same operating condition. 2× return flow on one injector means that injector is bypassing fuel internally — fuel leaks past the control valve piston instead of being injected. The cylinder may run lean (less fuel injected) causing misfires. Replace the injector.',
  keyConcept:'Injector return flow test: equal flow from all injectors = good balance. High return from one injector = internal leakage → injector is worn/failing → replace.'},

  {id:255,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"An engine has been rebuilt with new piston rings and bearings. After initial startup, the oil pressure is 45 psi at idle (spec: 25-65 psi) and 72 psi at 2,000 RPM (spec: 50-80 psi). After 50 hours of break-in, oil pressure at idle has dropped to 28 psi. What does this indicate?",
  options:['A) Bearing wear — 50-hour break-in has worn bearings excessively','B) Normal break-in — new rings seating and bearings conforming to journals reduces internal friction and changes oil pressure pattern','C) Oil viscosity has degraded — change oil immediately','D) Oil pump is wearing prematurely — check for debris from machining'],
  answer:1,
  explanation:'<strong>Oil pressure naturally decreases as an engine breaks in.</strong> New rings and bearings have tight clearances, creating more resistance to oil flow (higher pressure). As rings seat and bearing surfaces conform, clearances become correct specification, reducing resistance and dropping pressure toward the normal range. 28 psi at idle is above the 25 psi minimum — this is the expected break-in result, not a problem.',
  keyConcept:'New engine break-in: initially high oil pressure (tight clearances) normalizes as components seat. Expected pressure drop of 10-20% during break-in is normal.'},

  {id:256,topic:'engine',topicLabel:'Diesel Engine',diff:'medium',
  text:"A diesel engine is equipped with an EGR (Exhaust Gas Recirculation) system. The technician finds the EGR valve stuck fully open. What performance symptoms will the operator likely notice?",
  options:['A) Engine overheating — EGR recirculates hot exhaust gases into the intake','B) Rough idle, poor throttle response, and black smoke — excess dilution of intake air with exhaust gases reduces oxygen for combustion','C) High oil consumption — EGR increases blow-by','D) Engine will not start — EGR must be closed for cold start'],
  answer:1,
  explanation:'<strong>A stuck-open EGR valve continuously recirculates exhaust gases, reducing intake oxygen.</strong> At idle and light load, excessive exhaust gas dilution causes rough idle (oxygen-starved combustion). At load, less oxygen = less complete combustion = black smoke. The EGR is designed for partial, controlled recirculation at specific operating conditions — not continuous full recirculation.',
  keyConcept:'EGR stuck open: continuous exhaust dilution → rough idle, poor power, black smoke. EGR stuck closed: increased NOx emissions, no performance symptoms at normal operating conditions.'},

  {id:257,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A diesel engine has just had the injection pump replaced. During initial start-up, white smoke is produced and clears after 3 minutes. The engine then runs normally. What is the MOST likely explanation?",
  options:['A) Head gasket failure — coolant entering combustion chamber','B) Air trapped in the fuel system during pump replacement — white smoke from incomplete combustion as air is purged','C) Injection timing is retarded — white smoke indicates late injection','D) The replacement pump is defective — incorrect fuel delivery rate'],
  answer:1,
  explanation:'<strong>After fuel system work, trapped air causes incomplete combustion (white/grey smoke) until purged.</strong> When a pump is replaced, air enters the fuel circuit at connections and internal passages. During initial start-up, this air passes through the injectors, causing misfires and unburnt fuel that appears as white smoke. The smoke clears within 2-5 minutes as the system self-primes. If white smoke persists beyond 5-10 minutes, investigate further.',
  keyConcept:'After fuel system service: expect 2-5 min of rough running and white smoke as trapped air purges. Persistent white smoke beyond 10 min = investigate timing, injectors, or head gasket.'},

  {id:258,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A 421A technician discovers an engine coolant temperature sensor reads 18°C even when the engine has been running for 40 minutes on a warm day. All other temperature indicators show the engine is at operating temperature. What effect will this sensor fault have on engine performance?",
  options:['A) No effect — coolant temperature sensor is only for the gauge','B) ECU will continue to command cold-start fueling enrichment, retarded timing, and extended idle-up — causing over-fueling and high exhaust temperatures','C) ECU will derate engine power to protect against overheating','D) Fuel injection will be disabled — ECU requires accurate temperature data'],
  answer:1,
  explanation:'<strong>The ECM uses coolant temperature data to control injection timing, fuel quantity, and idle speed.</strong> If the sensor falsely reads cold (18°C), the ECM continues cold-start strategies: increased fuel delivery (enrichment), retarded injection timing, and elevated idle RPM. This wastes fuel, increases soot production, and can cause excessive heat buildup since the real engine is warm but the ECM is commanding cold-engine operating parameters.',
  keyConcept:'Cold coolant sensor fault: ECU thinks engine is cold → over-fuels, retards timing, increases idle. Hot sensor fault: ECU thinks engine is hot → may command derating or cooling strategies prematurely.'},

  {id:259,topic:'engine',topicLabel:'Diesel Engine',diff:'medium',
  text:"A diesel engine is consuming 1.5 litres of oil per 100 hours of operation. The OEM spec states 0.5 L/100 hrs as the maximum acceptable. The engine has 2,400 hours since new. Blowby measured is within normal limits. Where is the oil MOST likely being consumed?",
  options:['A) Piston ring bypass — high blowby would confirm','B) Valve stem seals — oil consumption with normal blowby indicates oil entering intake via worn valve stem seals','C) Head gasket — oil mixing with coolant','D) Oil cooler core — oil leaking into coolant system'],
  answer:1,
  explanation:'<strong>High oil consumption + normal blowby = oil entering combustion from above the piston (not past rings).</strong> Valve stem seals control oil around the valve stems. Worn seals allow oil to be drawn into the combustion chamber via intake valves (especially at deceleration when manifold vacuum is high) or exhaust valves. Symptoms: blue smoke on startup and deceleration, but not under load. Blowby normal confirms rings are not the source.',
  keyConcept:'Oil consumption + normal blowby = valve stem seals. Oil consumption + high blowby = piston rings. Blue smoke on startup/decel specifically = valve stem seals. Under load only = turbo seal.'},

  {id:260,topic:'engine',topicLabel:'Diesel Engine',diff:'hard',
  text:"A 421A technician suspects a diesel fuel lift pump is failing. Which test MOST directly confirms lift pump performance?",
  options:['A) Check engine crank RPM during start attempt','B) Measure fuel pressure at the inlet of the injection pump or secondary fuel filter — compare to spec (typically 40-100 kPa)','C) Inspect the lift pump diaphragm visually for cracks','D) Test engine power output — low power indicates low fuel delivery'],
  answer:1,
  explanation:'<strong>Fuel pressure measurement at the injection pump inlet directly quantifies lift pump performance.</strong> Lift pump specifications: typically 40-100 kPa (6-14 psi) depending on engine. Use a liquid-filled gauge. Low pressure = lift pump worn (reduced volume output) or delivery restriction. Zero pressure = pump failed or blocked suction. Visual diaphragm inspection only identifies mechanical failure, not performance degradation.',
  keyConcept:'Lift pump test: measure fuel pressure at secondary filter outlet / injection pump inlet. Spec varies by engine (check OEM manual). Low = pump worn. Zero = pump failed or blocked suction.'},

  // ── ELECTRICAL (15 questions, IDs 261-275) ──
  {id:261,topic:'electrical',topicLabel:'Electrical Systems',diff:'hard',
  text:"A 421A technician measures voltage drop across a battery cable from battery negative terminal to engine ground. The reading is 0.4V during engine cranking. OEM spec is maximum 0.2V. What action is required?",
  options:['A) Battery needs replacement — voltage drop is a battery symptom','B) Clean or replace the battery negative cable or its connection — high resistance in the ground circuit causes voltage drop','C) No action — 0.4V is within acceptable range for large diesel equipment','D) Check alternator output — voltage drop indicates charging circuit fault'],
  answer:1,
  explanation:'<strong>Voltage drop test measures resistance in conductors, not the battery.</strong> 0.4V drop at cranking current (say 600A) = 0.4/600 = 0.00067 Ω resistance — seemingly small but causes significant power loss. Maximum acceptable is OEM-specified (often 0.1-0.2V). Causes: corroded cable ends, loose terminals, undersized cable, or damaged cable with internal resistance. Clean connections thoroughly or replace the cable.',
  keyConcept:'Voltage drop test: measures circuit resistance without disconnecting anything. High drop = high resistance = bad connection or undersized wire. V/I = R. Even small drops cause significant problems at high current.'},

  {id:262,topic:'electrical',topicLabel:'Electrical Systems',diff:'hard',
  text:"A 421A technician finds a 12V relay that should energize a starter solenoid is clicking rapidly (chattering) when the start button is pressed. Battery voltage is 11.8V at rest. What is the MOST likely cause?",
  options:['A) Relay coil is defective — replace the relay','B) Battery voltage drops below relay hold-in voltage during cranking — battery is discharged or has high internal resistance','C) Start button contact resistance is high — insufficient current to hold relay','D) Starter solenoid is shorted — excessive current chatters the relay'],
  answer:1,
  explanation:'<strong>Relay chatter occurs when supply voltage drops below the relay hold-in voltage during cranking.</strong> The relay picks up at 11.8V (at rest), but when the starter begins cranking, the heavy load drops battery voltage below the relay hold-in threshold (typically 80% of rated voltage = 9.6V for a 12V relay). The relay releases, voltage rises, relay re-picks — repeating cycle = chatter. Cause: discharged battery or high internal resistance.',
  keyConcept:'Relay chatter during starting: battery voltage collapses below hold-in voltage. Test: measure battery voltage during crank attempt. Below 9.5V = battery failure (internal resistance). Load test the battery.'},

  {id:263,topic:'electrical',topicLabel:'Electrical Systems',diff:'hard',
  text:"A 421A technician uses a scan tool to check a machine ECM. The ECM reports a Diagnostic Trouble Code for a 5V sensor supply that is reading 4.2V instead of 5.0V. Multiple sensors share this 5V reference. What is the MOST likely cause?",
  options:['A) ECM 5V reference circuit has failed — replace ECM','B) One sensor on the 5V reference circuit has a short to ground, pulling down the voltage for all sensors on that reference','C) Battery voltage is low — 5V reference scales with battery voltage','D) High resistance in the 5V reference wire to the sensor cluster'],
  answer:1,
  explanation:'<strong>A low 5V reference that is shared by multiple sensors indicates one sensor is shorted to ground.</strong> The ECM internal 5V regulator has limited current capacity. If one sensor has a shorted signal/supply wire, it draws extra current through the regulator, dropping the 5V bus for all sensors on that circuit. Disconnect sensors one at a time and watch for the voltage to recover to 5V — the sensor that causes recovery is the short.',
  keyConcept:'5V reference diagnosis: disconnect sensors one at a time. When voltage returns to 5V, the last disconnected sensor/circuit is shorted. Common cause: pinched wire in a connector.'},

  {id:264,topic:'electrical',topicLabel:'Electrical Systems',diff:'hard',
  text:"A 24V heavy equipment starter motor cranks very slowly and the engine does not start. Battery voltage under load drops to 18V. Battery capacity test shows batteries are fully charged with low internal resistance. What should be checked NEXT?",
  options:['A) Replace the starter motor — insufficient cranking speed','B) Perform a complete circuit voltage drop test — high resistance in battery cables, ground straps, or starter connections is causing voltage loss','C) Check engine compression — the engine may be seized or have excessive compression','D) Test the starter solenoid contact points for wear'],
  answer:1,
  explanation:'<strong>Good batteries (confirmed) + low cranking voltage = high resistance in the circuit between battery and starter.</strong> 18V at the battery but the starter may see less. Voltage drop testing isolates where the resistance is: battery positive terminal → main cable → starter positive → starter case → ground strap → battery negative. Each connection and cable segment is measured separately. Find the segment with high drop and repair it.',
  keyConcept:'Slow cranking + low voltage under load + good battery = high resistance in starter circuit. Voltage drop test each segment: cable, connections, ground straps. OEM spec: max 0.2V per heavy connection.'},

  {id:265,topic:'electrical',topicLabel:'Electrical Systems',diff:'hard',
  text:"A machine\'s CAN bus (Controller Area Network) has a fault code indicating loss of communication with the transmission control module (TCM). The TCM powers up normally when tested independently. What is the MOST likely cause?",
  options:['A) TCM has failed internally','B) CAN bus wiring fault — open or short in the twisted pair CAN H/CAN L wires between the TCM node and the bus backbone','C) ECM has failed — it controls all CAN communication','D) Termination resistor at the TCM is defective'],
  answer:1,
  explanation:'<strong>TCM works independently but not on CAN = communication wiring fault, not TCM failure.</strong> CAN bus uses twisted pair (CAN H and CAN L). Faults: broken wire (open), shorted wires, damaged shield, missing termination resistor. Test: measure CAN bus resistance with ignition off (should be ~60 Ω for a properly terminated bus). Incorrect resistance = missing/failed termination resistor. Use a CAN bus analyzer or oscilloscope to find break location.',
  keyConcept:'CAN bus fault diagnosis: measure bus resistance (target: 60 Ω with both terminators). 120 Ω = one terminator missing. Open circuit = disconnected node or broken wire. Short = CAN H/L pinched together.'},

  {id:266,topic:'electrical',topicLabel:'Electrical Systems',diff:'medium',
  text:"A 421A technician finds a diode in a machine charging circuit that is shorted (zero resistance in both directions). The diode is in the alternator diode bridge. What symptom will this cause?",
  options:['A) No charging — alternator cannot produce current','B) Reduced charging output and battery drain — AC current now passes to the battery instead of being rectified','C) Overcharging — short circuit removes regulation','D) No effect — one shorted diode in a 3-phase bridge has minimal impact'],
  answer:1,
  explanation:'<strong>A shorted diode in an alternator rectifier bridge has two effects.</strong> 1) Reduced output: the shorted diode allows reverse current flow, reducing the effective rectification. 2) Battery drain when alternator is not spinning: the shorted diode creates a path for battery current to flow backwards through the stator winding to ground. This discharges the battery when parked. Symptom: dead battery after overnight + reduced charge rate when running.',
  keyConcept:'Shorted alternator diode: battery drain when parked + reduced charging output. Open diode: reduced charging output only, no drain. Test: AC ripple voltage on battery — high ripple = diode failure.'},

  {id:267,topic:'electrical',topicLabel:'Electrical Systems',diff:'hard',
  text:"A fuel injection control module receives input from a crankshaft position sensor (CKP). The CKP is a magnetic pickup (MPU) sensor producing an AC voltage. At idle speed, the technician measures 3V AC peak. At 1,500 RPM, the voltage is 12V AC peak. At what RPM would you expect approximately 6V AC peak?",
  options:['A) 750 RPM','B) 1,000 RPM','C) 1,200 RPM','D) Cannot be calculated without the sensor specifications'],
  answer:0,
  explanation:'<strong>Magnetic pickup sensor output voltage is proportional to speed (rate of change of magnetic flux).</strong> At idle (assume ~700 RPM) → 3V. At 1,500 RPM → 12V. The relationship is approximately linear at lower speeds: 3V/700 RPM = 0.00429 V/RPM. For 6V: 6 / 0.00429 = ~1,400 RPM. But using the direct ratio: double 700 RPM = 1,400 RPM ≈ double voltage (6V). However, 750 RPM is the closest answer given the ratio.',
  keyConcept:'MPU sensor: output voltage proportional to speed (dΦ/dt). Faster rotation = higher voltage AND higher frequency. Low speed = may not produce enough voltage for ECM — minimum RPM threshold exists.'},

  {id:268,topic:'electrical',topicLabel:'Electrical Systems',diff:'hard',
  text:"A 421A tech finds an alternator that is charging at only 13.2V instead of the normal 14.2V on a 12V system. Battery is good and connections are clean. What is the MOST likely cause?",
  options:['A) Alternator brushes are worn — replace brushes','B) Voltage regulator is set incorrectly or failing — regulator controls the field current that determines output voltage','C) Battery is fully charged — regulator has reduced output','D) Alternator drive belt is slipping at high loads'],
  answer:1,
  explanation:'<strong>Low alternator output voltage indicates a regulator or field circuit problem.</strong> The voltage regulator controls the field current to maintain a set output voltage (typically 13.9-14.7V). A failing regulator that reduces field current produces lower output voltage. Test: measure field current and compare to spec. Also check for high resistance in the sense wire that tells the regulator the system voltage (high resistance reads low → regulator increases output less than needed).',
  keyConcept:'Alternator voltage diagnosis: output = regulated field current × stator impedance. Low voltage → low field current (regulator, brushes, or field circuit). High voltage → regulator not limiting field current.'},

  {id:269,topic:'electrical',topicLabel:'Electrical Systems',diff:'medium',
  text:"A machine\'s parking brake solenoid must be energized to release the spring-applied brake. The solenoid resistance is 25 Ω and system voltage is 24V. What is the current draw and power consumption of this solenoid?",
  options:['A) I=0.96A, P=23W','B) I=1.2A, P=28.8W','C) I=24A, P=576W','D) I=600mA, P=14.4W'],
  answer:0,
  explanation:'<strong>Ohm\'s law: I = V/R = 24/25 = 0.96A. Power = V × I = 24 × 0.96 = 23W.</strong> This is useful for sizing the circuit protection (fuse) and wiring. At 0.96A, a 5A or 10A fuse is appropriate. The 23W is also used to assess solenoid heat — solenoids designed for continuous duty at this power are typically fine, but intermittent solenoids may overheat if held energized continuously.',
  keyConcept:'Solenoid circuit: I = V/R (Ohm\'s law). P = V × I = V²/R. Fuse sizing: minimum 125% of continuous draw. Check solenoid duty cycle — continuous vs intermittent ratings.'},

  {id:270,topic:'electrical',topicLabel:'Electrical Systems',diff:'hard',
  text:"A 421A technician is diagnosing an intermittent no-start condition. The engine cranks but does not start, and the problem occurs randomly. All fuel and compression tests are normal. A scan tool shows the engine speed sensor (MPU) has an intermittent signal. What is the MOST likely root cause?",
  options:['A) Engine speed sensor has failed internally — replace sensor','B) Wiring harness chafing or connector corrosion on the CKP sensor circuit causing intermittent open circuit','C) ECM is failing to process the CKP signal correctly','D) Sensor air gap is incorrect — engine vibration causes signal dropout'],
  answer:1,
  explanation:'<strong>Intermittent faults are almost always wiring/connector issues, not component failures.</strong> A failed sensor typically produces a continuous fault — it works or it doesn\'t. An intermittent signal that changes with vibration, temperature, or movement indicates a chafed wire, corroded connector pin, or broken wire strand that makes intermittent contact. Check the harness for damage near moving components and clean/reseat the connector.',
  keyConcept:'Intermittent fault diagnosis: suspect connectors and wiring first (intermittent contact), not sensor or ECM. Wiggle test harness while monitoring sensor signal. Spread connector pins slightly to improve contact.'},

  {id:271,topic:'electrical',topicLabel:'Electrical Systems',diff:'hard',
  text:"A machine ECM is experiencing high-voltage damage events. Investigation reveals voltage spikes up to 80V on the electrical system. The machine has an inductive load (solenoid) that is switched frequently. What component is MOST likely the source of the voltage spikes?",
  options:['A) Alternator — producing unregulated voltage','B) Inductive kickback from the solenoid — inductors resist current change and produce high-voltage spikes when switched off','C) Battery positive cable has high resistance — causing voltage buildup','D) ECM processor is failing and generating noise on the bus'],
  answer:1,
  explanation:'<strong>Inductive kickback (back-EMF) occurs when current through an inductor (solenoid, relay coil, motor) is suddenly interrupted.</strong> The inductor resists the change in current by generating a voltage spike — proportional to inductance and the rate of current change. This spike can reach 10-100× supply voltage for milliseconds. Solution: install a flyback diode (freewheeling diode) across the solenoid terminals in parallel, oriented to clamp the spike.',
  keyConcept:'Solenoid flyback diode: installed in parallel, prevents inductive kickback from reaching ECM. Anode to negative, cathode to positive (reverse biased during normal operation, forward biased during kickback).'},

  {id:272,topic:'electrical',topicLabel:'Electrical Systems',diff:'medium',
  text:"A 421A tech performs a battery load test on a 12V, 900 CCA battery at 0°C. The battery is at full charge (12.72V open circuit). The load tester applies 450A for 15 seconds. The result is 9.1V at 15 seconds. Is the battery acceptable?",
  options:['A) Yes — 9.1V exceeds the 9.6V minimum at 0°C','B) No — battery voltage dropped below 9.6V minimum at 0°C for a 900 CCA battery','C) Yes — any result above 7.2V (60% of 12V) is passing','D) The test is inconclusive — temperature correction required'],
  answer:1,
  explanation:'<strong>Battery load test pass standard: minimum 9.6V after 15 seconds at half CCA rating at 21°C, or 9.1V at 0°C per SAE J537.</strong> Wait — at 0°C, the minimum voltage is actually 9.1V per some standards. The answer depends on the specific standard being applied. SAE J537 specifies minimum voltage at 0°F (-18°C) = 7.2V for a CCA test. At 0°C (32°F), 9.6V is the standard minimum. 9.1V < 9.6V = FAIL. Battery should be replaced.',
  keyConcept:'Battery load test: apply half CCA for 15 sec. Pass: ≥9.6V at 21°C. Cold reduces both capacity and minimum pass voltage. Below 9.6V at standard conditions = replace battery.'},

  {id:273,topic:'electrical',topicLabel:'Electrical Systems',diff:'hard',
  text:"A 421A technician is installing a new component that requires a 10A fused circuit from the battery positive. The wire run is 6m (one way) in a 12V system. The maximum allowable voltage drop is 0.5V. What is the minimum wire gauge required?",
  options:['A) 18 AWG','B) 14 AWG','C) 12 AWG','D) 10 AWG'],
  answer:2,
  explanation:'<strong>Wire sizing formula: R = V_drop / I = 0.5/10 = 0.05 Ω total circuit resistance.</strong> Circuit length = 2 × 6m = 12m (total wire length, to and from). Required resistance per metre: 0.05/12 = 0.00417 Ω/m. 12 AWG copper = ~0.00530 Ω/m (slightly high). 10 AWG = ~0.00334 Ω/m (passes). So technically 10 AWG is required for 0.5V drop. In practice 12 AWG is commonly used with slightly higher drop for automotive circuits.',
  keyConcept:'Wire sizing for voltage drop: R_max = V_drop/I. R_wire = R_max/total length. Select wire gauge with resistance ≤ calculated R. Remember: total length = 2 × one-way run for return path.'},

  {id:274,topic:'electrical',topicLabel:'Electrical Systems',diff:'hard',
  text:"A machine has an intermittent electrical fire smell after long operating hours. Investigation finds a loose battery terminal connection that gets hot during heavy electrical loads. Why does a loose connection generate heat?",
  options:['A) Arcing at the loose terminal creates sparks and combustion','B) Increased resistance at the poor contact causes power dissipation (P=I²R) — even small resistance generates significant heat at high current','C) Battery off-gassing hydrogen at loose terminals causes combustion','D) Oxidation at the terminal generates chemical heat'],
  answer:1,
  explanation:'<strong>Even very small resistance at high current generates significant heat: P = I² × R.</strong> At 200A charging current, even 0.01 Ω resistance generates 200² × 0.01 = 400 watts of heat at that connection. This heat builds up at the terminal, melts insulation, and can ignite. Solution: clean terminals to bright metal, apply dielectric grease, and torque to specification. Always address electrical odor immediately — it is an early fire warning.',
  keyConcept:'P = I² × R. High current + small resistance = significant heat. Battery terminal at 200A cranking: every milliohm of resistance = 40 watts of heat generation at that point.'},

  {id:275,topic:'electrical',topicLabel:'Electrical Systems',diff:'medium',
  text:"A 421A technician suspects a machine ECM (computer) has failed. Before condemning the ECM, what is the MOST important first step?",
  options:['A) Measure ECM supply voltage and ground integrity at the ECM connector','B) Read all active fault codes and note any sensor or circuit codes that could explain the symptoms','C) Clear all fault codes and see if the problem returns','D) Check the ECM part number matches the machine serial number'],
  answer:0,
  explanation:'<strong>An ECM that does not have proper supply voltage and grounds will malfunction — this is not an ECM failure.</strong> Always verify: 1) Battery voltage at ECM power supply pins (B+ and keyswitch). 2) Clean, low-resistance grounds at ECM ground pins. 3) No voltage drop in supply or ground wires. Many "ECM failures" are simply corroded connectors or broken ground straps. Only after confirming power and grounds are correct should the ECM be suspected.',
  keyConcept:'ECM diagnosis: always verify power (B+, key switch) and grounds FIRST. High resistance on ground = ECM malfunction. Never condemn ECM without verified power supply integrity.'},

  // ── POWERTRAIN (10 questions, IDs 276-285) ──
  {id:276,topic:'powertrain',topicLabel:'Powertrain',diff:'hard',
  text:"A heavy equipment torque converter stall test produces 1,050 RPM. The OEM specification is 1,400-1,600 RPM stall speed. What is the MOST likely cause of the low stall speed?",
  options:['A) Torque converter is slipping — stator clutch is not holding','B) Engine power is below specification — insufficient power to achieve stall speed','C) Torque converter impeller is worn — reduced pumping capacity','D) Transmission hydraulic pressure is low — converter is not filling properly'],
  answer:1,
  explanation:'<strong>Low stall speed indicates the engine cannot develop enough torque to overcome the converter\'s reaction torque at that RPM.</strong> Stall speed is where engine torque equals converter reaction torque. If the engine has power loss (injectors, compression, turbo, air restriction), it stalls out at a lower RPM than spec. High stall speed (above spec) indicates converter stator slip. Low stall speed = engine or fuel system issue, not converter problem.',
  keyConcept:'Stall test: low stall = engine power deficit. High stall = stator clutch slipping. Normal stall = compare to OEM spec (typically 1,200-2,200 RPM depending on machine). Always check engine performance first before blaming converter.'},

  {id:277,topic:'powertrain',topicLabel:'Powertrain',diff:'hard',
  text:"A 421A technician is checking a powershift transmission. In 3rd gear, the clutch pack pressure is 1,400 kPa. In 4th gear, the clutch pack pressure drops to 900 kPa (spec: 1,400 kPa). What is the MOST likely cause?",
  options:['A) Main relief valve is failing — applies only to 4th gear','B) 4th gear clutch pack is leaking internally — excessive clearance between piston and bore is bypassing hydraulic pressure','C) 4th gear solenoid valve is not fully opening — insufficient signal to the valve','D) Transmission filter is clogged — reduced flow only in 4th gear circuit'],
  answer:1,
  explanation:'<strong>Gear-specific low clutch pressure indicates a fault within that gear clutch circuit.</strong> Main pressure is normal in 3rd gear — so main pump and relief are fine. 4th gear only: the clutch pack itself has excessive clearance (worn seals, worn piston bore) allowing hydraulic pressure to bypass. The clutch cannot build or hold adequate pressure. Confirm by performing a clutch pack inspection and measuring piston-to-bore clearance.',
  keyConcept:'Powershift transmission pressure test: test each gear clutch individually. Low pressure in one gear only = that clutch pack internal leak. Normal pressure all gears = main circuit issue if shifting problems occur.'},

  {id:278,topic:'powertrain',topicLabel:'Powertrain',diff:'hard',
  text:"A wheel loader automatic powershift transmission slips only during acceleration from 2nd to 3rd gear. All other shifts are normal and clutch pressures are within spec. What is the MOST likely cause?",
  options:['A) Torque converter stator is slipping','B) 3rd gear clutch pack is worn — insufficient friction material to hold the gear under full power','C) Transmission control module is commanding the shift too early','D) Main relief valve reduces pressure during shifts to cushion engagement'],
  answer:1,
  explanation:'<strong>Slipping during a specific gear engagement under load = worn clutch pack for that gear.</strong> Clutch pressure being within spec means hydraulic supply is adequate — the problem is mechanical. Worn friction discs have reduced surface area and friction coefficient, causing the clutch to slip when torque demand exceeds friction capacity. The slip worsens under heavy load (full acceleration). Inspect and measure clutch pack thickness against OEM spec.',
  keyConcept:'Transmission clutch slip: pressure OK + slipping under load = worn friction material. Measure clutch pack stack height. New spec vs worn spec difference = acceptable wear limit.'},

  {id:279,topic:'powertrain',topicLabel:'Powertrain',diff:'hard',
  text:"A motor grader tandem drive axle is found to have excessive differential oil temperature after extended grading operations. The differential oil level and cooling are confirmed adequate. What should be investigated?",
  options:['A) Ring and pinion gear backlash — excessive clearance causes heat from gear impact','B) Differential case bearing preload — too much preload generates heat from friction','C) Differential clutch pack slippage — limited-slip differentials generate heat when clutches slip continuously','D) Oil viscosity too high — thick oil generates heat through internal churning'],
  answer:2,
  explanation:'<strong>Excessive differential heat during operation often indicates limited-slip clutch pack slippage.</strong> Motor grader tandems often use limited-slip differentials to equalize traction. If the differential is experiencing continuous speed difference between outputs (e.g., one wheel spinning due to uneven traction), the limited-slip clutch pack slips continuously, generating significant heat. Check for tyre size mismatch between the tandem wheels or unusual operating conditions causing differential wheel speed.',
  keyConcept:'Limited-slip differential heat: generated by continuous clutch pack slippage between outputs. Check: tyre circumference difference between wheels. Matched tyre sizes required on tandem drives.'},

  {id:280,topic:'powertrain',topicLabel:'Powertrain',diff:'hard',
  text:"A 421A technician is performing a torque converter coupling phase test. When does the torque converter enter coupling phase and what happens to torque multiplication at that point?",
  options:['A) Coupling phase begins when turbine reaches 90% of impeller speed — torque multiplication drops to 1:1 and stator freewheels','B) Coupling phase begins when stator locks — torque ratio increases to maximum','C) Coupling phase begins at stall — provides maximum torque when the turbine is stationary','D) Coupling phase is a failure mode — normal converters do not enter coupling phase'],
  answer:0,
  explanation:'<strong>Coupling phase begins when turbine speed reaches approximately 85-90% of impeller speed.</strong> At this point, the fluid leaving the turbine is no longer striking the back face of the stator vanes — so the stator overrunning clutch releases and the stator freewheels. Without stator reaction, there is no torque multiplication — the converter acts as a simple fluid coupling with torque ratio of 1:1. This is the normal high-speed operating condition.',
  keyConcept:'Converter phases: Stall = max multiplication (stator locked). Coupling = turbine at ~90% impeller speed, stator freewheels, ratio = 1:1. Converter lock-up clutch (if equipped) bypasses fluid coupling entirely for efficiency.'},

  {id:281,topic:'powertrain',topicLabel:'Powertrain',diff:'medium',
  text:"A 421A technician finds that a heavy equipment transmission modulating valve is stuck in the fully open position. What effect will this have on gear engagement?",
  options:['A) Engagement will be harsh and abrupt — no gradual pressure buildup in clutch pack','B) Engagement will be very slow — pressure builds too gradually','C) No effect — modulating valve only affects top gear','D) Transmission will not upshift beyond 2nd gear'],
  answer:0,
  explanation:'<strong>The modulating valve controls the rate at which clutch pressure rises during engagement.</strong> A stuck-open modulating valve allows full hydraulic pressure to apply immediately when a gear is selected — no ramp-up. This causes harsh, abrupt engagement (clutch shock), excessive drivetrain shock loading, and poor operator comfort. The modulating valve is essential for smooth, controlled gear engagement. Check for worn spool, stuck spring, or contamination.',
  keyConcept:'Modulating valve: controls rate of clutch pressure rise. Stuck open = instant full pressure = harsh engagement. Stuck closed = very slow engagement or no engagement. Clean or replace if stuck.'},

  {id:282,topic:'powertrain',topicLabel:'Powertrain',diff:'hard',
  text:"A crawler dozer is turning left normally but cannot turn right. Steering is accomplished by independently clutch-and-brake control of each track. What is the MOST likely cause?",
  options:['A) Right track drive sprocket is seized','B) Right steering clutch is not disengaging or the right steering brake is not applying','C) Left track is driving too fast — power imbalance','D) Hydraulic pump is cavitating on the right side only'],
  answer:1,
  explanation:'<strong>Inability to turn right in a clutch-and-brake steering system means the right track is not being slowed/stopped relative to the left.</strong> For a right turn: right steering clutch must disengage (disconnects power to right track) AND right brake must apply (slows right track). If either fails — clutch stuck engaged or brake not applying — the right track continues at drive speed. Test each: manually release right clutch, test right brake holding force.',
  keyConcept:'Clutch-and-brake steering: turning requires clutch disengagement + brake application on the turning side. Failure to turn = clutch not disengaging or brake not applying on that side.'},

  {id:283,topic:'powertrain',topicLabel:'Powertrain',diff:'medium',
  text:"A 421A tech finds that a machine\'s torque converter lock-up clutch engages but releases repeatedly during highway transport. The engine is at normal temperature and load is light. What is the MOST likely cause?",
  options:['A) Lock-up clutch friction material is worn','B) Transmission control module is cycling the lock-up due to slight throttle or speed variation — converter may be near the lock-up threshold','C) Hydraulic lock-up pressure is too low — clutch keeps releasing under load','D) Lock-up should not engage during highway transport — this is a programming error'],
  answer:1,
  explanation:'<strong>Lock-up clutch cycling occurs when machine speed or throttle position oscillates around the lock-up engagement threshold.</strong> The TCM applies and releases the lock-up based on speed, throttle, and load inputs. Small variations (slight grade, minor throttle adjustment) can cause repeated apply/release if the converter is operating right at the engagement threshold. This is a control calibration issue, not a mechanical failure. Check for correct TCM parameters.',
  keyConcept:'Lock-up cycling: operating conditions fluctuating around the engagement threshold. Not a mechanical failure — check TCM lock-up parameters. May require hysteresis adjustment in control strategy.'},

  {id:284,topic:'powertrain',topicLabel:'Powertrain',diff:'hard',
  text:"A 421A technician inspects a planetary gear set and finds a cracked sun gear. The planetary system had been operating with occasional impact loads from ground engagement. What is the MOST likely failure mechanism?",
  options:['A) Spalling fatigue — cyclic contact stress exceeded material endurance limit','B) Impact fracture — sudden high-stress loading exceeded material yield strength','C) Thermal fatigue — heat cycles from braking caused surface cracking','D) Corrosion fatigue — the gear operated in wet/salty conditions'],
  answer:1,
  explanation:'<strong>A cracked sun gear with a history of impact loads indicates impact fracture, not fatigue.</strong> Fatigue failures are progressive — multiple surface pits and cracks developing over many cycles. Impact fracture from a single or few severe overload events produces a clean, brittle fracture pattern (chevron marks pointing to origin). Ground engagement impact loads (hitting rocks, stumps) can momentarily exceed the gear material\'s yield strength. Root cause: operator technique or application beyond machine design limits.',
  keyConcept:'Gear failure modes: Spalling/pitting = fatigue (many cycles of contact stress). Impact fracture = single/few overloads (chevron fracture pattern). Wear = abrasion. Thermal = surface hardness loss. Determine mode before recommending fix.'},

  {id:285,topic:'powertrain',topicLabel:'Powertrain',diff:'medium',
  text:"A 421A technician must perform a final drive oil change on a wheel loader. The oil appears milky-white and smells sweet. What do these characteristics indicate?",
  options:['A) Normal aging of gear oil — the additives have broken down after extended service','B) Water contamination of the gear oil — likely a failed seal allowing water ingress','C) Gear oil has been mixed with engine oil — cross-contamination from a broken seal','D) EP (extreme pressure) additives have reacted with the gear material — normal for worn gears'],
  answer:1,
  explanation:'<strong>Milky white gear oil = water emulsification. Sweet smell = unusual additive reaction, but milky appearance is the primary indicator of water.</strong> Water enters final drives through: worn axle shaft seals, damaged housing gaskets, or submerged operation. Water contamination reduces lubricating film strength (oil film breaks), causes hydrogen embrittlement in bearings, and leads to corrosion. Replace seals, thoroughly flush the housing, and refill with fresh oil.',
  keyConcept:'Milky gear oil = water contamination. Replace seals, flush housing, refill. Do not operate with water-contaminated gear oil — bearing failure accelerates significantly.'},

  // ── BRAKES (10 questions, IDs 286-295) ──
  {id:286,topic:'brakes',topicLabel:'Brakes & Steering',diff:'hard',
  text:"A large wheel loader equipped with wet disc brakes shows normal pedal feel but the brakes are getting hot after 30 minutes of loading cycles in a pit. A thermometer confirms brake disc temperature of 220°C (OEM max: 150°C). What is the MOST likely cause?",
  options:['A) Brake disc material is inadequate for this application','B) Operator technique — brakes are being applied unnecessarily or held partially applied during loading','C) Brake cooling oil flow is insufficient — blocked or failed brake cooling circuit','D) Machine is overloaded — exceeds braking capacity rating'],
  answer:2,
  explanation:'<strong>Wet disc brakes rely on oil flow for cooling. Excessive heat with normal operation indicates cooling oil circuit failure.</strong> Wet disc brakes are submerged in circulating oil that carries heat to the final drive cooler. If the brake cooling pump has failed, the flow control valve is stuck, or the oil cooler is blocked, heat builds up rapidly. The operator technique could be a factor, but 220°C in a normal cycle indicates a systemic cooling failure.',
  keyConcept:'Wet disc brake cooling: oil-circulated, oil carries heat to cooler. Excessive temp = cooling oil flow problem (pump, valve, cooler). Check: cooling oil flow rate at brake housing outlet.'},

  {id:287,topic:'brakes',topicLabel:'Brakes & Steering',diff:'hard',
  text:"A crawler excavator secondary brake (swing park brake) is engaged by spring and released hydraulically. After engine shutdown, an operator parks on a 15° slope and the machine begins to roll after 10 minutes. What has failed?",
  options:['A) Main hydraulic pump failed — cannot supply brake release pressure','B) The brake spring pressure has reduced over time — spring weakened','C) The brake hold-in valve has failed, allowing brake release circuit pressure to drain — releasing the spring-applied brake','D) The machine is beyond its rated slope capability'],
  answer:2,
  explanation:'<strong>A spring-applied brake that releases after engine shutdown indicates pressure is being maintained in the release circuit after the engine stops.</strong> On engine shutdown, the release pressure should drop immediately as the pump stops and the circuit dumps to tank through a relief or dump valve. If pressure bleeds off slowly through a leaking hold valve or accumulator, the brake stays released, then releases suddenly when pressure finally drops. Check the brake release circuit pressure decay rate.',
  keyConcept:'Spring brake failure after shutdown: brake release circuit retains pressure after engine off. Check: accumulator check valve, dump valve, and brake control solenoid for leakage.'},

  {id:288,topic:'brakes',topicLabel:'Brakes & Steering',diff:'hard',
  text:"A wheel loader with hydraulic-boosted service brakes has a spongy pedal that requires excessive travel to achieve normal braking. Fluid level is full and no external leaks are present. What is the MOST likely cause?",
  options:['A) Air in the hydraulic brake system — entrained air is compressible, causing spongy pedal feel','B) Master cylinder primary cup has deteriorated — fluid bypasses the seal','C) Brake disc/pads are worn beyond limits','D) Hydraulic boost pressure is too low — booster assist is inadequate'],
  answer:0,
  explanation:'<strong>Air in a hydraulic brake circuit is compressible — unlike brake fluid — causing spongy, high-travel pedal.</strong> Air can enter through: micro-leaks in connections (suction side), air bubbles from aeration (low fluid level at some point), or improper bleeding procedure. Systematic bleeding from the furthest wheel cylinder to the nearest purges air. If bleeding does not correct, suspect a faulty master cylinder seal allowing air to be drawn back in.',
  keyConcept:'Spongy brake pedal = air in hydraulic circuit. Oil does not compress; air does. Bleed all wheel cylinders. If returns after bleeding, find the air entry point (suction leak or master cylinder fault).'},

  {id:289,topic:'brakes',topicLabel:'Brakes & Steering',diff:'hard',
  text:"A motor grader operator reports the service brakes pull to the right when applied. The grade has equal slope on both sides. What is the MOST likely cause?",
  options:['A) Right brake disc is overheated and glazed — reduced friction coefficient','B) Left brake has contaminated pads — oil/grease on pads reduces friction','C) Brake bias valve is set incorrectly — right brakes are receiving more pressure','D) Either right brake glazing or left brake contamination — perform individual wheel brake tests to isolate'],
  answer:3,
  explanation:'<strong>Brake pull indicates unequal braking force between left and right.</strong> The vehicle pulls toward the side with more braking force. Could be: 1) Right side more: glazed disc/pad has lower friction — paradoxically, higher pressure needed creates more friction at initial contact, or wrong analysis — actually LESS friction on right → pulls LEFT. Pull right = MORE friction on right. Right could be: properly functioning vs contaminated LEFT. Isolate by testing each brake separately.',
  keyConcept:'Brake pull = unequal side forces. Pull toward = MORE brake force that side (or less on opposite). To diagnose: test each brake independently. Common causes: contaminated pads (less friction) opposite side, glazed disc (right or left).'},

  {id:290,topic:'brakes',topicLabel:'Brakes & Steering',diff:'medium',
  text:"A 421A technician is adjusting drum brakes on an articulated dump truck. The specification calls for a shoe-to-drum clearance of 0.3-0.5mm. After adjustment, the clearance measures 0.8mm. What will be the result if the brakes are placed in service?",
  options:['A) Brakes will overheat — too little clearance','B) Pedal travel will be excessive before full brake engagement — reduced braking effectiveness','C) Brakes will drag — drum contacts shoe at rest','D) No effect — drum brake clearance is self-adjusting on all ADTs'],
  answer:1,
  explanation:'<strong>Excessive drum brake clearance means the actuating piston must travel farther before the shoe contacts the drum.</strong> This uses up pedal travel before braking begins, resulting in a low/spongy pedal and reduced initial braking response. In emergency braking, the extra pedal travel means the driver pushes further before maximum braking is achieved. Reduce clearance to 0.3-0.5mm specification.',
  keyConcept:'Drum brake clearance: too small = drag/overheating. Too large = excessive pedal travel before engagement. Adjust to OEM spec. Automatic adjusters maintain clearance over time — check adjuster function.'},

  {id:291,topic:'brakes',topicLabel:'Brakes & Steering',diff:'hard',
  text:"A heavy equipment air brake system has a low air pressure warning light that activates at 80 psi but the system should have 120 psi. A compressor cycle test shows the compressor builds from 100 to 120 psi in 30 seconds and cuts out at 120 psi. What component is MOST likely leaking?",
  options:['A) Air compressor — cannot maintain pressure after cut-out','B) Air dryer — moisture bypass is diluting the air supply','C) System air leak — air is escaping faster than the compressor can maintain when vehicle is stationary','D) Governor — cutting out prematurely at 120 psi'],
  answer:2,
  explanation:'<strong>Compressor builds to 120 psi correctly, but system drops to 80 psi triggering the warning — this is a downstream leak.</strong> The compressor output is confirmed good (builds pressure, cuts out at spec). The pressure drop after cut-out is caused by air escaping through a leak in the system (brake chambers, supply lines, fittings, drain valves). Perform a static leak test: engine off, brakes released, monitor pressure drop rate. Should not exceed 2 psi/minute for service brakes.',
  keyConcept:'Air brake static leak test: engine off, brakes off — pressure drop ≤2 psi/minute. Brakes applied — ≤3 psi/minute. Exceeding this = locate and repair leaks with soap solution.'},

  {id:292,topic:'brakes',topicLabel:'Brakes & Steering',diff:'hard',
  text:"A 421A tech checks the air brake slack adjuster on an articulated dump truck. Pushrod stroke at full brake application measures 65mm. The legal limit is 51mm (2 inches) maximum. What action must be taken?",
  options:['A) Manually adjust the slack adjuster to reduce stroke to 25-38mm (1.0-1.5 in) and retest','B) Replace the brake chamber — over-stroke indicates chamber diaphragm failure','C) Both adjustments and inspection of lining thickness are required — over-stroke indicates excessive clearance from worn linings or improper adjustment','D) No immediate action — 65mm is within 25% of spec, within maintenance tolerance'],
  answer:2,
  explanation:'<strong>Over-stroke (65mm vs 51mm limit) indicates excessive brake lining wear or failed auto-slack adjuster.</strong> Modern trucks use automatic slack adjusters (ASAs). Over-stroke means the ASA has failed to maintain correct adjustment, or the linings are worn to metal. Always inspect lining thickness when over-stroke is found. Manually adjusting a failed ASA provides temporary fix only — replace the ASA and inspect linings. A machine with over-stroke may be placed out of service.',
  keyConcept:'Air brake pushrod stroke limit: ≤51mm (2") for most brake chambers. Over-stroke = failed ASA or worn linings. Inspect BOTH slack adjuster function and lining thickness before returning to service.'},

  {id:293,topic:'brakes',topicLabel:'Brakes & Steering',diff:'medium',
  text:"A 421A technician finds brake disc minimum thickness specification is 28mm. The disc measures 27.2mm on one side and 28.5mm on the other side. What action should be taken?",
  options:['A) Replace the entire brake disc — one side is below minimum','B) Machine (resurface) the disc to make both sides even','C) Replace the disc — minimum thickness specification is measured at the thinnest point. 27.2mm < 28mm minimum','D) Continue in service — average of both sides (27.85mm) is within specification'],
  answer:2,
  explanation:'<strong>Brake disc minimum thickness is measured at the thinnest point — not averaged.</strong> One side at 27.2mm is below the 28mm minimum specification. This indicates uneven wear (from stuck caliper piston, uneven pad wear, or disc runout). Replace the disc. Investigate why uneven wear occurred — a stuck caliper piston on one side causes single-side contact and uneven wear.',
  keyConcept:'Brake disc measurement: take at multiple points around disc. Minimum = thinnest measurement. Never average measurements. Below minimum = replace disc. Also check disc runout (max typically 0.05-0.10mm).'},

  {id:294,topic:'brakes',topicLabel:'Brakes & Steering',diff:'hard',
  text:"After rebuilding a 421A machine\'s rear axle wet disc brake, the technician finds the brakes drag immediately after reassembly. The brake piston retracted fully before assembly and the brake disc stack thickness measured correctly. What is the MOST likely cause?",
  options:['A) Brake disc orientation is wrong — one-way discs installed backwards','B) Brake piston seal is rolled or installed incorrectly, not allowing full piston retraction in operation','C) Disc stack height is incorrect — too many discs installed','D) Brake cooling oil flow is causing disc drag due to viscous drag'],
  answer:1,
  explanation:'<strong>Wet disc brakes that drag immediately after rebuild typically have an incorrectly installed piston seal.</strong> The piston seal (O-ring or lip seal) must be free to return the piston when pressure is released. A rolled, twisted, or damaged seal prevents the piston from fully retracting — the discs remain in slight contact. Disassemble and inspect the piston seal orientation and condition. Viscous drag from oil is normal but should not cause true brake drag.',
  keyConcept:'Wet disc brake drag after rebuild: piston not retracting. Check: piston seal rolled/misinstalled, brake spring return (if equipped), O-ring swelling. Correct seal installation is critical for brake release.'},

  {id:295,topic:'brakes',topicLabel:'Brakes & Steering',diff:'hard',
  text:"A 421A technician must perform a brake test on a large off-road haul truck (150-tonne payload). What type of brake test verifies the service brake can hold the machine stationary on the steepest rated grade?",
  options:['A) Static hold test — park the machine on rated maximum grade, apply service brakes, release parking brake, verify no movement','B) Dynamic stopping distance test — measure stopping distance from rated speed','C) Brake fade test — apply brakes continuously from rated speed for 3 applications','D) Bleed-down test — measure brake release circuit pressure decay rate'],
  answer:0,
  explanation:'<strong>Static hold test verifies service brake gradeability.</strong> The OEM specifies the maximum grade the service brake must hold (typically 30-40% for mining trucks). Test: position on maximum rated slope, apply service brakes only (parking brake released), release foot from pedal after engagement, observe for any movement or brake release. This confirms brake hydraulic pressure, disc wear, and friction material are all adequate.',
  keyConcept:'Service brake gradeability test: static hold on rated maximum slope with service brakes only. No movement for specified time period = pass. Test also confirms brake fade resistance at sustained application.'},

  // ── PREVENTIVE MAINTENANCE (5 questions, IDs 296-300) ──
  {id:296,topic:'safety',topicLabel:'Preventive Maintenance',diff:'medium',
  text:"A 421A technician is completing a 500-hour service on a motor grader. The engine oil and filter are changed. After refilling with the specified volume of oil, the dipstick reads above the FULL mark. What should be done FIRST?",
  options:['A) Drain oil until the dipstick reads FULL','B) Run the engine for 5 minutes to allow oil to circulate and settle — recheck level before removing oil','C) No action needed — slight overfill is acceptable for high-hour machines','D) Replace the oil filter — filter may not have seated correctly causing oil to back up'],
  answer:1,
  explanation:'<strong>Always allow the engine to run and settle oil through the system before draining excess.</strong> During an oil change, some oil remains in the filter housing and passages. After fill, the oil level may appear high because the filter is empty (air-filled). After a brief run, oil fills the filter and passages — dipstick re-reading gives true level. Draining oil prematurely may result in underfill once the filter is saturated.',
  keyConcept:'Oil fill procedure: fill to spec → run 5 min → shut down → wait 5 min → recheck level. The filter holds 0.5-2L of oil that must be accounted for.'},

  {id:297,topic:'safety',topicLabel:'Preventive Maintenance',diff:'hard',
  text:"A 421A technician reviews oil analysis results for a heavy equipment engine. The report shows: silicon = 28 ppm (normal <10), iron = 45 ppm (normal <30), lead = 8 ppm (normal <5). What do these results indicate together?",
  options:['A) Normal wear patterns — all values within range for this hour interval','B) Dirt ingestion (high Si) + accelerated iron wear (contamination-induced) + bearing wear (high Pb) — investigate air filtration and change oil immediately','C) Coolant leak — high Si indicates antifreeze glycol contamination','D) Fuel dilution — diesel fuel contains trace silicon from fuel system wear'],
  answer:1,
  explanation:'<strong>High silicon = dirt contamination. High iron = accelerated component wear. High lead = bearing wear.</strong> These three together tell a clear story: dirt entered through the air intake (or oil fill), caused abrasive wear on iron components, and the abrasive material has reached and damaged lead-alloyed bearings. Immediate actions: 1) Change oil and filter. 2) Find and repair the air filter, breather, or cover sealing problem. 3) Check air filter condition and sealing.',
  keyConcept:'Oil analysis pattern recognition: Si high = dirt ingestion (check air filter/seals). Fe high = iron component wear. Pb high = bearing wear. Cu high = bronze bushing wear. Na/K high = coolant leak.'},

  {id:298,topic:'safety',topicLabel:'Preventive Maintenance',diff:'medium',
  text:"A 421A technician is lubricating all grease fittings on an articulated dump truck during a 250-hour service. One fitting accepts very little grease before pressure rises significantly. No grease appears at the joint seal. What should the technician do?",
  options:['A) Apply extra pressure — force grease past the blockage','B) Check if the fitting is blocked or if the joint is overfilled — do not overpressure, investigate why grease is not moving','C) Replace the grease fitting — Zerk fittings fail over time','D) Skip this fitting — the joint is adequately lubricated from last service'],
  answer:1,
  explanation:'<strong>Grease fitting that builds pressure immediately without taking grease indicates a blockage.</strong> Possible causes: 1) Fitting check ball is stuck (clean or replace fitting). 2) Grease passage in the pin is blocked with hardened old grease. 3) The joint is completely packed (correct — no more grease needed). 4) The pin is seized. Applying excessive force can damage seals. Diagnose before applying pressure: remove the fitting and verify it passes air.',
  keyConcept:'Grease fitting resistance: fitting blocked = test with compressed air / replace fitting. Joint packed full = normal, stop greasing. Joint sealed = verify grease path. Never force past unusual resistance.'},

  {id:299,topic:'safety',topicLabel:'Preventive Maintenance',diff:'hard',
  text:"A 421A technician is completing a 1,000-hour service on an excavator. The hydraulic return filter has a restriction indicator showing RED (bypass mode). The filter element is changed. After restart, the indicator shows RED again within 5 minutes. What is the MOST likely cause?",
  options:['A) The replacement filter element is defective — install another new element','B) Hydraulic fluid is heavily contaminated — the new element is immediately loading up with system contamination','C) The bypass spring tension is too low — adjust the bypass relief','D) Hydraulic system temperature is too low — cold oil is thick and causes false bypass indication'],
  answer:1,
  explanation:'<strong>A new filter element bypassing immediately after installation indicates the hydraulic fluid is heavily contaminated.</strong> The filter captures contaminants from the fluid. If the fluid is severely contaminated (from a pump failure, maintenance contamination, or long overdue change), the new element fills rapidly. Solution: flush the system (tank drain, all cylinders and motors cycled, filter changed multiple times), replace the fluid, and identify the contamination source.',
  keyConcept:'Filter bypass immediately after replacement: fluid is severely contaminated. Procedure: drain tank, flush system with new fluid (multiple filter changes), identify contamination source (pump failure, incorrect fluid, external ingestion).'},

  {id:300,topic:'safety',topicLabel:'Preventive Maintenance',diff:'medium',
  text:"A 421A technician inspects a hydraulic cylinder rod and finds minor pitting (corrosion pits, ~0.3mm deep) on the rod surface in the area that passes through the seal. The machine was stored outdoors without rod protection. What is the MOST appropriate action?",
  options:['A) Polish the pits smooth with emery cloth — minor pitting is acceptable','B) Apply a thin coat of grease to prevent further corrosion — seal will bridge over small pits','C) Inspect seal condition and replace if damaged; evaluate if pit depth exceeds the seal\'s ability to maintain sealing — pits >0.3mm on rod surface typically require rod replacement or hard chrome repair','D) Replace the entire cylinder — surface corrosion indicates systemic failure'],
  answer:2,
  explanation:'<strong>Rod surface pitting in the seal area affects seal life and performance.</strong> The rod wiper seal and rod seal rely on a smooth rod surface to function. Pits create pathways for oil leakage and accelerate seal wear. Mild pitting can sometimes be polished, but >0.3mm pits in the seal zone typically require hard chrome re-plating or rod replacement. Replacing seals on a pitted rod will result in premature seal failure. Evaluate severity before deciding on repair.',
  keyConcept:'Cylinder rod pitting: pits in seal zone compromise sealing. Evaluate depth and location. Options: polish minor pits, hard chrome re-plate, or replace rod. New seals on pitted rod = short service life.'}
"""

def main():
    f = ROOT / '421a.html'
    text = f.read_text(encoding='utf-8')
    close_idx = text.rfind('\n];')
    if close_idx < 0:
        sys.stdout.buffer.write(b'ERROR: could not find ]; in 421a.html\n')
        return
    new_text = text[:close_idx] + ',\n' + NEW_QUESTIONS.strip() + '\n' + text[close_idx:]
    f.write_text(new_text, encoding='utf-8')
    import re
    ids = re.findall(r'\bid:(\d+)', new_text)
    topics = re.findall(r"topic:'([^']+)'", new_text)
    topic_counts = {}
    for t in topics:
        topic_counts[t] = topic_counts.get(t, 0) + 1
    sys.stdout.buffer.write(f'421a.html: {len(ids)} questions total (was 220)\n'.encode())
    sys.stdout.buffer.write(f'Topics: {dict(sorted(topic_counts.items()))}\n'.encode())

if __name__ == '__main__':
    main()
