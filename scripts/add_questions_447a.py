#!/usr/bin/env python3
"""Add 25 application-type Hard/Medium questions to 447a.html (Plumber)"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NEW_QUESTIONS = r"""
  // ── APPLICATION-TYPE ADDITIONS (2026-04-18) ──
  {id:111,topic:'dwv',topicLabel:'DWV Systems',diff:'hard',
  text:"A plumber is testing a new DWV system and finds that a floor drain in a basement gurgling every time an upstairs fixture drains. There is no evidence of blockage. What is the MOST likely cause?",
  options:['A) The floor drain trap has evaporated','B) Insufficient venting — suction is pulling the trap seal from the floor drain','C) The branch drain slope is too steep (>1/4 inch per foot)','D) Floor drain is connected to the storm system by mistake'],
  answer:1,
  explanation:'<strong>Gurgling drains indicate siphoning caused by negative pressure (insufficient venting).</strong> When an upper fixture drains, it creates a pressure wave in the drain stack. Without adequate venting, this creates negative pressure that pulls the floor drain trap seal, causing gurgling. The fix is to properly vent the floor drain or install an air admittance valve.',
  keyConcept:'Gurgling trap = negative pressure in drain = venting problem. Floor drain gurgles when upper fixtures drain = stack not vented adequately at that branch.'},

  {id:112,topic:'dwv',topicLabel:'DWV Systems',diff:'hard',
  text:"A 447A plumber notices that a fixture drain trap loses its water seal overnight even though the fixture is not used. No gurgling is observed and there is no evidence of leakage. What is the MOST likely explanation?",
  options:['A) Trap evaporation — fixture is not used frequently enough','B) Siphoning from an adjacent draining fixture','C) Back pressure from the drain stack pushing water out','D) Capillary action pulling the water seal away'],
  answer:0,
  explanation:'<strong>Trap evaporation occurs in infrequently used floor drains and fixtures.</strong> A standard P-trap holds 25-50mm of water. In low-humidity environments, this evaporates in 3-7 days without use. The solution is a trap primer, deep-seal trap (100mm seal depth), or regular manual filling. This is distinct from siphoning (which causes gurgling) or capillary action (requires wick material in the trap).',
  keyConcept:'Trap seal lost: 1) Evaporation (no sound, infrequent use) → deep seal trap or primer. 2) Siphoning (gurgling) → venting issue. 3) Back pressure (bubbling) → stack pressure problem.'},

  {id:113,topic:'gas',topicLabel:'Gas Piping',diff:'hard',
  text:"A 447A plumber tests a new natural gas line at 7 kPa test pressure and observes a 0.5 kPa drop over 30 minutes. The NPC requires the pressure hold for 10 minutes with no drop. What is the CORRECT action?",
  options:['A) Accept the test — 0.5 kPa is within the 10% tolerance for natural gas','B) The test fails — locate and repair the leak before any rework or approval','C) Purge the line and retest at higher pressure','D) Accept the test — ambient temperature change could account for this drop'],
  answer:1,
  explanation:'<strong>Gas pressure tests require zero pressure drop for the full test duration.</strong> Any measurable pressure drop indicates a leak. The NPC (National Plumbing Code) and B149.1 require a pressure hold with no indication of leakage. Temperature changes can cause minor variation, but 0.5 kPa over 30 minutes on a 7 kPa test is significant. Find and repair all leaks before proceeding.',
  keyConcept:'Gas test (B149.1/NPC): no measurable pressure loss during test period. Any drop = leak. Locate with approved leak detection solution, not flame.'},

  {id:114,topic:'water',topicLabel:'Water Supply',diff:'hard',
  text:"A new building has water hammer occurring every time the washing machine valve closes. The water pressure is 550 kPa and no air chambers were installed. What is the MOST effective permanent fix?",
  options:['A) Reduce water pressure at the main to 400 kPa','B) Install a water hammer arrestor (WHA) of the correct size at the washing machine supply','C) Add an air chamber pipe stub at the washing machine valve','D) Install a pressure-reducing valve at the building entry'],
  answer:1,
  explanation:'<strong>Water hammer arrestors (WHAs) are the Code-preferred solution over air chambers.</strong> Air chambers eventually become waterlogged and ineffective. WHAs contain a piston with a nitrogen-charged chamber that absorbs the pressure wave when fast-acting valves (solenoids) close suddenly. Size by fixture unit count and install as close as possible to the solenoid valve.',
  keyConcept:'Water hammer: fast-closing valves → pressure wave. Fix: install water hammer arrestor (WHA) — not air chambers (waterlog over time). Size per ASME A112.26.1.'},

  {id:115,topic:'water',topicLabel:'Water Supply',diff:'hard',
  text:"A 447A plumber is sizing a cold water service for a 6-storey residential building. The basement static pressure is 620 kPa. The building is 18m tall. What is the pressure available at the top-floor fixtures and is a booster pump required? (1 kPa ≈ 0.1m head)",
  options:['A) 620 - (18 × 10) = 440 kPa available — no booster needed (minimum is 140 kPa)','B) 620 - 180 = 440 kPa — booster needed for high-pressure fixtures','C) 620 + 180 = 800 kPa — excess pressure, PRV required','D) Cannot be calculated without flow rate data'],
  answer:0,
  explanation:'<strong>Static pressure at height = available pressure − pressure loss due to elevation.</strong> Elevation loss: 18m × 10 kPa/m = 180 kPa. Available at top floor: 620 - 180 = 440 kPa. NPC minimum pressure at fixtures: 140 kPa (20 psi). 440 kPa far exceeds this — no booster pump required. However, if operating pressure (with flow) drops below 140 kPa, a booster would be needed.',
  keyConcept:'Pressure at height: P_available = P_static - (height × 10 kPa/m). NPC minimum fixture pressure: 140 kPa. Maximum: typically 550 kPa (PRV required above this).'},

  {id:116,topic:'water',topicLabel:'Water Supply',diff:'medium',
  text:"A hot water heater is producing discoloured (rusty) water but the cold water is clear. What should the plumber suspect FIRST and recommend?",
  options:['A) The water main has a main break upstream — flush the system','B) The anode rod in the hot water tank has depleted — replace the sacrificial anode','C) Hot water piping corrosion — replace all copper piping','D) Water softener malfunction — check salt levels'],
  answer:1,
  explanation:'<strong>Rusty hot water with clear cold water indicates tank corrosion — the sacrificial anode rod has failed.</strong> Magnesium or aluminum anode rods protect the glass-lined steel tank through galvanic action. Once depleted, the tank corrodes internally. Replacing the anode rod early extends tank life. If the tank interior is already significantly corroded, replacement of the whole tank may be more cost-effective.',
  keyConcept:'Rusty hot water only = anode rod depleted. Cold water clear = not a main problem. Anode rods typically last 3-5 years depending on water chemistry.'},

  {id:117,topic:'dwv',topicLabel:'DWV Systems',diff:'hard',
  text:"A 447A plumber is installing a 100mm (4\") diameter cast iron drain stack in a 3-storey building. Per the NPC, what is the maximum number of 90° bends permitted at the base of the stack before transitioning to the building drain?",
  options:['A) No bends allowed — must use two 45° elbows instead','B) A single 90° bend is acceptable at the base of any stack','C) Two 90° bends separated by at least 600mm of straight pipe','D) Maximum one 90° bend, or two 45° elbows — no restriction on straight section length'],
  answer:0,
  explanation:'<strong>NPC prohibits sharp 90° elbows at the base of a drain stack.</strong> The high-velocity vertical flow at the base creates significant turbulence. Two 45° elbows (total 90°) provide a gradual direction change, reducing turbulence and pressure buildup. A single 90° short-turn elbow at the base of a loaded stack can cause serious back-pressure problems and is not permitted.',
  keyConcept:'Stack base: use two 45° elbows (not one 90°) to transition from vertical stack to horizontal building drain. Reduces turbulence and back-pressure.'},

  {id:118,topic:'fixtures',topicLabel:'Fixtures & Appliances',diff:'medium',
  text:"A tankless (on-demand) water heater is installed but produces only lukewarm water when multiple fixtures are used simultaneously. The heater is sized for 12 L/min. What is MOST likely occurring?",
  options:['A) The unit has a defective heat exchanger','B) Total simultaneous flow demand exceeds the unit capacity — the heater cannot heat at the required flow rate','C) Cold water inlet temperature is below design','D) Gas pressure is too high, causing incomplete combustion'],
  answer:1,
  explanation:'<strong>Tankless heaters are flow-limited — they heat a fixed volume per minute at a set temperature rise.</strong> If simultaneous demand (shower + tap + dishwasher) exceeds 12 L/min, the heater cannot maintain set temperature. The fix is either adding a second unit in parallel, installing a buffer tank, or reducing simultaneous demand. This is a sizing error, not a unit failure.',
  keyConcept:'Tankless heater sizing: calculate peak simultaneous demand (L/min) and required temperature rise. Undersizing = lukewarm water at peak demand.'},

  {id:119,topic:'code',topicLabel:'Code & Inspection',diff:'hard',
  text:"A 447A plumber is roughing in a bathroom. The floor drain requires a trap with a minimum water seal depth per the NPC. What is the minimum trap seal depth required?",
  options:['A) 25 mm (1 inch)','B) 38 mm (1.5 inches)','C) 50 mm (2 inches)','D) 75 mm (3 inches)'],
  answer:1,
  explanation:'<strong>NPC requires trap seals between 38 mm minimum and 100 mm maximum.</strong> The minimum 38mm ensures sufficient depth to maintain the water seal under normal operating pressure fluctuations (±250 Pa). Seals less than 38mm are vulnerable to evaporation and slight pressure fluctuations. Maximum 100mm prevents seal-loss from back pressure in the drain system.',
  keyConcept:'NPC trap seal: minimum 38mm (1.5"), maximum 100mm (4"). Deep-seal traps (75-100mm) are used for floor drains susceptible to evaporation.'},

  {id:120,topic:'code',topicLabel:'Code & Inspection',diff:'hard',
  text:"A 447A plumber is installing copper water service pipe in soil. The NPC requires the pipe to be protected from corrosion. What is the minimum requirement for Type K copper buried in corrosive soil?",
  options:['A) No protection needed — copper is naturally corrosion resistant in all soils','B) Copper must be sleeved in plastic conduit or wrapped with protective tape in corrosive soils','C) Type K copper may not be buried — use only plastic pipe','D) Paint the pipe with a rubber-based coating'],
  answer:1,
  explanation:'<strong>Copper can corrode in acidic or high-chloride soils.</strong> NPC and CSA B651 require protection for copper pipe in corrosive soils. Methods include polyethylene sleeving, bituminous coating, or use of plastic pipe (PVC, CPVC, or PE). Type K is the thickest-walled copper and is preferred for underground, but soil corrosion protection is still required when soil conditions warrant.',
  keyConcept:'Buried copper: Type K preferred for underground. Protect in corrosive soils with polyethylene sleeving or bituminous wrap. Verify soil conditions before selecting materials.'},

  {id:121,topic:'safety',topicLabel:'Safety & Tools',diff:'medium',
  text:"A plumber is soldering copper pipe using an open-flame torch in a wall cavity near wood framing. What is the SAFEST procedure to prevent fire?",
  options:['A) Soak the framing with water before soldering','B) Use a heat shield (flame spreader or fire-resistant barrier) behind the fitting and have a fire watch for 30 minutes after completing work','C) Keep a fire extinguisher within 3 metres and proceed normally','D) Use push-fit fittings instead — open flame prohibited near wood'],
  answer:1,
  explanation:'<strong>Heat shields protect adjacent combustibles and fire watch is required after torch work.</strong> Smoldering fires in wood framing can ignite hours after work is complete. Provincial fire codes require a 30-60 minute fire watch after open-flame work near combustibles. A metal heat shield reflects heat away from wood. Push-fit fittings are an alternative but not always required.',
  keyConcept:'Soldering near combustibles: use heat shield + fire watch (30-60 min minimum). Provincial fire codes typically require permits for open-flame work in wall cavities.'},

  {id:122,topic:'dwv',topicLabel:'DWV Systems',diff:'hard',
  text:"A 447A plumber installs a wet vent serving a lavatory (DN50/2\") that is 2.4m from the stack connection. The NPC limits wet vent length based on pipe diameter. Is this installation compliant?",
  options:['A) Yes — wet vent length limit for DN50 is 1.8m, so this fails','B) No — wet vent must be DN75 minimum for 2.4m length','C) Yes — DN50 wet vent is permitted up to 2.4m per NPC','D) Wet venting is prohibited in Canada — use individual vents only'],
  answer:2,
  explanation:'<strong>NPC wet vent length limits vary by pipe size.</strong> DN32 (1.25"): max 1.2m. DN38 (1.5"): max 1.5m. DN50 (2"): max 2.4m. DN75 (3"): max 4.5m. A 2.4m wet vent in DN50 pipe is at the maximum permitted length — compliant. Wet venting is permitted and commonly used in NPC jurisdictions for lavatory/sink installations.',
  keyConcept:'NPC wet vent max lengths: 32mm=1.2m, 38mm=1.5m, 50mm=2.4m, 75mm=4.5m. The fixture drain acts as both drain and vent simultaneously.'},

  {id:123,topic:'water',topicLabel:'Water Supply',diff:'hard',
  text:"A 447A plumber is sizing a 25mm (1\") domestic hot water recirculation pump. The system has 45m of 25mm pipe and a total heat loss of 800 W. The pump must maintain the system at minimum 55°C. Which factor is MOST important to prevent Legionella growth in the recirculation system?",
  options:['A) Pump flow rate must exceed 10 L/min','B) Hot water must be stored at minimum 60°C and delivered at minimum 49°C at fixtures','C) Return pipe temperature must stay above 45°C at all points','D) System must be flushed monthly with 70°C water'],
  answer:1,
  explanation:'<strong>Legionella pneumophila thrives at 25-50°C and is killed above 60°C.</strong> NPC and CSA B214 require hot water storage at minimum 60°C and delivery at minimum 49°C to prevent Legionella colonization. Return pipe temperature in a recirculation system should maintain above 55°C. The 60°C storage with 49°C delivery is the standard Legionella control range for domestic water systems.',
  keyConcept:'Legionella prevention: store hot water at ≥60°C, deliver at ≥49°C. Danger zone: 25-50°C. Killed at 60°C. Recirculation maintains temperature throughout the system.'},

  {id:124,topic:'fixtures',topicLabel:'Fixtures & Appliances',diff:'medium',
  text:"A 447A plumber is installing a wall-mounted water closet (toilet) in a commercial washroom. After installation, the toilet rocks slightly side to side. What should be done?",
  options:['A) Tighten the closet bolts as much as possible to eliminate movement','B) Shim the toilet and then apply silicone — excessive bolt tightening can crack the porcelain','C) Replace the toilet — movement indicates a defective unit','D) The toilet must be re-hung on a different carrier'],
  answer:1,
  explanation:'<strong>Wall-mounted toilets must be shimmed level before silicone sealing — never torqued tight without a level base.</strong> Porcelain is brittle — over-tightening closet bolts on an unlevel surface will crack the fixture. Proper procedure: level and shim the toilet, hand-tighten bolts, apply silicone bead at the base, then snug bolts. Check torque spec if provided by manufacturer.',
  keyConcept:'Water closet installation: shim level first → hand-tighten → silicone seal → torque to spec. Over-tightening unlevel fixtures cracks porcelain.'},

  {id:125,topic:'gas',topicLabel:'Gas Piping',diff:'hard',
  text:"A 447A gas fitter is sizing a natural gas supply for a commercial kitchen. The total connected BTU/h load is 350,000 BTU/h (102.6 kW) at 7\" W.C. (1.75 kPa) supply pressure. The run from the meter is 30m of 2\" pipe. Using a pipe capacity table, which sized pipe is required?",
  options:['A) 1.5\" pipe — sufficient for up to 400,000 BTU/h at 30m','B) 2\" pipe — matches the installed run and handles 350,000 BTU/h','C) 2.5\" pipe — 2\" is undersized for this flow at 30m','D) 1\" pipe — over-designed for restaurant use'],
  answer:1,
  explanation:'<strong>2\" pipe at 30m run typically carries 350,000-450,000 BTU/h at 7\" W.C. pressure with 0.5\" pressure drop.</strong> Always verify against the actual CSA B149.1 pipe sizing tables for your specific supply pressure and allowable pressure drop. The key variables are: pipe diameter, length, fitting allowances, and allowable pressure drop. 30m at 350,000 BTU/h is well within 2" capacity at 7" W.C.',
  keyConcept:'Gas pipe sizing: use CSA B149.1 tables. Inputs: BTU/h load, pipe length, supply pressure, allowable pressure drop. Always add equivalent length for fittings.'},

  {id:126,topic:'dwv',topicLabel:'DWV Systems',diff:'medium',
  text:"A 447A plumber is testing a new DWV system using the air pressure test method. The NPC requires what test pressure and hold duration for this test?",
  options:['A) 7 kPa (1 psi) for 15 minutes','B) 35 kPa (5 psi) for 15 minutes','C) 100 kPa (14.5 psi) for 10 minutes','D) 14 kPa (2 psi) for 30 minutes'],
  answer:1,
  explanation:'<strong>NPC air test for DWV: 35 kPa (5 psi) for a minimum of 15 minutes with no pressure loss.</strong> Air tests are safer than water tests in completed buildings (no risk of water damage if a joint fails). The 35 kPa test pressure is lower than water test pressure because water adds hydrostatic load. All openings must be capped and the pressure maintained without addition of air.',
  keyConcept:'DWV air test (NPC): 35 kPa for 15 minutes, no loss. Water test alternative: fill to highest point and hold. Never use oxygen or flammable gas for pressure testing.'},

  {id:127,topic:'water',topicLabel:'Water Supply',diff:'hard',
  text:"A 447A plumber discovers cross-connection between a municipal potable water supply and a non-potable irrigation system. The system currently has a double check valve assembly (DCVA) installed. The water authority requires upgrading. What is the correct upgrade and why?",
  options:['A) No upgrade needed — DCVA is the highest level of protection available','B) Upgrade to a reduced pressure zone (RPZ) backflow preventer — required for high-hazard cross-connections where contamination could be health-threatening','C) Add a second DCVA in series — doubles the protection level','D) Install a vacuum breaker — simpler and equivalent protection'],
  answer:1,
  explanation:'<strong>Irrigation systems with fertilizer injectors or chemical application are high-hazard cross-connections requiring RPZ protection.</strong> DCVA provides protection against back-siphonage and back-pressure but cannot protect against high-hazard contamination. RPZ backflow preventers include a relief valve that opens to atmosphere if the check valves fail, preventing contamination from entering the potable supply.',
  keyConcept:'Backflow protection hierarchy: Air gap (highest) > RPZ > DCVA > PVB (lowest). High-hazard connections (pesticides, chemicals) require RPZ or air gap minimum.'},

  {id:128,topic:'safety',topicLabel:'Safety & Tools',diff:'hard',
  text:"A plumber is installing drain-waste-vent piping in a confined space (pump room, 4m x 3m x 2.5m) and must use a solvent cement (ABS or PVC cement). What safety precautions are REQUIRED before beginning work?",
  options:['A) Open one window for ventilation and proceed normally','B) Atmospheric testing for oxygen level and flammable vapours, plus forced-air ventilation before entry and continuous monitoring during work','C) Wear a dust mask rated N95 and safety glasses','D) Work for maximum 15-minute intervals then exit for fresh air'],
  answer:1,
  explanation:'<strong>Solvent cement contains volatile organic compounds (VOCs) — flammable and toxic in confined spaces.</strong> Confined space entry requires: atmospheric testing (oxygen 19.5-23.5%, LEL <10%, toxic below TLV), continuous forced-air ventilation, continuous atmospheric monitoring, and a trained attendant outside. A solvent-wet confined space can accumulate vapours to explosive levels quickly.',
  keyConcept:'Confined space + solvent cement: atmospheric test before entry, forced ventilation, continuous monitoring, attendant outside. Solvent cement VOCs are heavier than air — accumulate at floor level.'},

  {id:129,topic:'fixtures',topicLabel:'Fixtures & Appliances',diff:'hard',
  text:"A 447A plumber is replacing a bathroom exhaust fan that vents through the roof. The duct run is 7m with two 90° elbows. The manufacturer minimum CFM is 50 CFM. Per ASHRAE 62.2, what is the minimum ventilation requirement for a typical bathroom and is the fan adequate?",
  options:['A) ASHRAE requires 20 CFM minimum — fan is adequate','B) ASHRAE 62.2 requires 50 CFM intermittent or 20 CFM continuous — the fan meets minimum but duct resistance must be verified','C) No minimum standard applies to residential bathrooms in Canada','D) ASHRAE requires 100 CFM for all bathrooms — fan is undersized'],
  answer:1,
  explanation:'<strong>ASHRAE 62.2 bathroom ventilation: 50 CFM intermittent or 20 CFM continuous.</strong> The fan meets the minimum CFM, but published fan ratings are at 0 static pressure. Each 90° elbow adds ~7.5Pa of resistance; 7m of duct adds more. Total static pressure in the duct system may reduce actual CFM below 50. Verify fan CFM at the expected system static pressure using the fan curve.',
  keyConcept:'Exhaust fan sizing: published CFM is at zero static pressure. Real CFM drops with duct resistance. Always check fan curve at estimated system resistance.'},

  {id:130,topic:'code',topicLabel:'Code & Inspection',diff:'hard',
  text:"A 447A plumber completes rough-in for a 3-piece bathroom in a new residential build. Before proceeding with drywall, what inspections are typically required in most Canadian jurisdictions?",
  options:['A) Only a final plumbing inspection after all fixtures are installed','B) Rough-in inspection (before concealment) plus final inspection after fixture installation — two inspections minimum','C) Self-certification by the licensed plumber is sufficient in most provinces','D) Only the authority having jurisdiction (AHJ) determines if inspection is required'],
  answer:1,
  explanation:'<strong>Most provincial plumbing codes require a rough-in inspection before any work is concealed.</strong> This allows the AHJ (inspector) to verify pipe sizing, venting, drainage grades, and pressure test results before walls are closed. A final inspection after fixture installation is also typically required. Self-certification is not permitted for plumbing in most Canadian jurisdictions.',
  keyConcept:'Required plumbing inspections: 1) Rough-in (before concealment) — verify DWV + pressure test. 2) Final (after fixtures) — verify operation and Code compliance.'},

  {id:131,topic:'dwv',topicLabel:'DWV Systems',diff:'medium',
  text:"A 447A plumber finds that a lavatory drain is running very slowly but is not completely blocked. Snaking the drain clears it, but it becomes slow again within 2 weeks. What does this pattern MOST likely indicate?",
  options:['A) The drain has a belly (sag) that is trapping solids — structural correction required','B) The drain is the wrong size for the fixture','C) The trap arm slope is too steep, causing solids to deposit','D) The P-trap is partially blocked with hair — annual cleaning only solution'],
  answer:0,
  explanation:'<strong>A recurring slow drain that clears with snaking but returns quickly indicates a structural problem.</strong> A belly (low sag in horizontal drain pipe caused by settlement or improper support) traps solids that accumulate until the pipe is slow or blocked again. Snaking removes the accumulation but not the belly. Camera inspection confirms the low spot — re-grading or replacement of that pipe section is the permanent fix.',
  keyConcept:'Recurring slow drain after snaking = structural issue (belly/sag). Confirm with drain camera. Fix: re-grade or replace the affected pipe section.'},

  {id:132,topic:'water',topicLabel:'Water Supply',diff:'medium',
  text:"A new residence has copper water pipe that shows blue-green staining on fixtures and pinhole leaks after 2 years. What is the MOST likely cause and recommended solution?",
  options:['A) Type M copper was used — upgrade to Type L','B) Water has low pH (acidic) — corroding copper pipe from inside. pH adjustment or pipe replacement with CPVC/PEX','C) Copper pipe was installed in direct contact with concrete','D) The joints were soldered with 95/5 solder instead of lead-free solder'],
  answer:1,
  explanation:'<strong>Blue-green staining on fixtures indicates copper dissolution — the water is attacking the pipe.</strong> Acidic water (pH below 6.5) aggressively corrodes copper, causing blue-green deposits on fixtures and eventually pinhole leaks. Solutions: pH adjustment (neutralizing filter), water softener bypass, or replace with plastic pipe (PEX, CPVC) that resists acidic water. Report to local water authority.',
  keyConcept:'Copper + acidic water: blue-green staining + pinholes. pH < 6.5 is corrosive to copper. Fix: neutralize pH or switch to plastic pipe. Not a defect in the copper itself.'},

  {id:133,topic:'gas',topicLabel:'Gas Piping',diff:'medium',
  text:"A gas range is producing a yellow-orange flame instead of a blue flame on the burners. The gas pressure at the manifold is correct. What is the MOST likely cause?",
  options:['A) LP (propane) gas is being used instead of natural gas','B) Primary air ports (venturi) are partially blocked — insufficient air mixing with gas before combustion','C) Gas pressure regulator is set too high','D) The gas orifice is the wrong size for the BTU rating'],
  answer:1,
  explanation:'<strong>Yellow/orange flame indicates incomplete combustion due to insufficient primary air.</strong> The Bunsen burner principle: primary air mixes with gas in the venturi before the burner. Blockage from grease, food debris, or insect nests reduces primary air, causing incomplete combustion (yellow, sooty, CO-producing flame). Clean the burner ports and venturi. A blue flame with yellow tips is normal; a fully yellow flame is not.',
  keyConcept:'Gas burner flame: Blue = complete combustion (correct air/fuel). Yellow/orange = insufficient primary air or wrong gas type. Yellow = CO risk — do not operate.'},

  {id:134,topic:'fixtures',topicLabel:'Fixtures & Appliances',diff:'medium',
  text:"A 447A plumber is installing a dishwasher in a residential kitchen. The drain hose must be connected to prevent backflow of drain water into the dishwasher. What is the NPC-compliant method?",
  options:['A) Connect directly to the P-trap of the kitchen sink','B) Form a high loop in the drain hose to the underside of the countertop, or use an air gap fitting','C) Install a check valve in the drain hose near the dishwasher','D) Connect to the garbage disposal inlet only — no backflow protection needed'],
  answer:1,
  explanation:'<strong>NPC requires an air gap or high loop to prevent backflow from the drain into the dishwasher.</strong> A direct connection without backflow protection allows contaminated drain water to siphon back into the clean dishwasher. The air gap (preferred, NPC-compliant) provides a physical break. A high loop under the countertop is commonly accepted and reduces siphoning risk through elevation.',
  keyConcept:'Dishwasher drain: NPC requires air gap or high loop. Air gap = physical break from drain contamination. High loop = elevation prevents siphon but not backpressure.'},

  {id:135,topic:'water',topicLabel:'Water Supply',diff:'hard',
  text:"A 447A plumber is conducting a domestic hot water recirculation system commissioning check. The temperature at the end of the recirculation loop measures 42°C during peak morning demand. What is the significance of this reading and what action is required?",
  options:['A) 42°C is acceptable — within normal range for occupied buildings','B) 42°C is in the Legionella danger zone (25-50°C) — increase recirculation pump flow or insulation to maintain >55°C throughout the loop','C) Temperature is too high — risk of scalding, install tempering valve','D) No action needed — 42°C complies with provincial energy codes for water heating'],
  answer:1,
  explanation:'<strong>Legionella proliferates at 25-50°C — a return temperature of 42°C indicates a colonization risk.</strong> The recirculation system must maintain above 55°C at all points in the loop to prevent Legionella growth. Causes of low return temp: undersized recirculation pump, undersized piping, excessive heat loss from uninsulated pipe, or demand exceeding system capacity. Insulate return pipe and verify pump sizing.',
  keyConcept:'Recirculation loop: minimum 55°C at all points including return. 42°C return = Legionella risk zone. Fix: improve pipe insulation, increase pump flow, or increase storage temperature.'}
"""

def main():
    f = ROOT / '447a.html'
    text = f.read_text(encoding='utf-8')
    close_idx = text.rfind('\n];')
    if close_idx < 0:
        sys.stdout.buffer.write(b'ERROR: could not find ]; in 447a.html\n')
        return
    new_text = text[:close_idx] + ',\n' + NEW_QUESTIONS.strip() + '\n' + text[close_idx:]
    f.write_text(new_text, encoding='utf-8')
    import re
    ids = re.findall(r'\bid:(\d+)', new_text)
    sys.stdout.buffer.write(f'447a.html: {len(ids)} questions total (was 110)\n'.encode())

if __name__ == '__main__':
    main()
