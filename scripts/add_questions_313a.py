#!/usr/bin/env python3
"""Add 25 application-type Hard/Medium questions to 313a.html (Industrial Electrician)"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NEW_QUESTIONS = r"""
  // ── APPLICATION-TYPE ADDITIONS (2026-04-18) ──
  {id:111,topic:'motors',topicLabel:'Motors & Drives',diff:'hard',
  text:"A 313A electrician finds a 3-phase induction motor drawing Phase A=28A, Phase B=31A, Phase C=24A while running unloaded at rated voltage. What is the MOST likely cause?",
  options:['A) Worn motor bearings causing mechanical drag','B) Single-phasing from a blown control fuse','C) Voltage unbalance at the supply terminals','D) Motor is overloaded beyond nameplate rating'],
  answer:2,
  explanation:'<strong>Even small voltage unbalance causes significant current unbalance.</strong> A 2% voltage unbalance can cause 6–10× current unbalance between phases. Bearings cause noise but not phase-unbalanced current. Single-phasing would show one phase near zero. Overload raises all phases proportionally.',
  keyConcept:'Rule: 1% voltage unbalance → ~6% current unbalance. Check line voltages before suspecting motor windings.'},

  {id:112,topic:'motors',topicLabel:'Motors & Drives',diff:'hard',
  text:"A VFD-driven conveyor motor trips on overcurrent fault consistently after 45 minutes at 60 Hz. At 45 Hz it runs indefinitely. The technician confirms the motor FLA and VFD current limit match. What should be checked NEXT?",
  options:['A) Replace VFD output transistors','B) Check motor cooling — internal fan may be inadequate at full speed under load','C) Reduce the VFD carrier frequency','D) Verify motor insulation with a megohmmeter'],
  answer:1,
  explanation:'<strong>Motor cooling is speed-dependent.</strong> Internal cooling fans move less air at reduced speed. At 60 Hz full load, heat generated exceeds what the fan removes, triggering thermal protection. This is a common issue with TEFC motors on VFDs — a separately powered cooling fan or derating may be required.',
  keyConcept:'VFD-driven motors running below nameplate speed lose cooling capacity. Derating or external cooling is required for continuous low-speed operation.'},

  {id:113,topic:'motors',topicLabel:'Motors & Drives',diff:'hard',
  text:"A wound-rotor induction motor is connected with external resistance in the rotor circuit. After the resistance is short-circuited, motor RPM increases from 1,680 to 1,740 under the same load. What does this confirm?",
  options:['A) The motor had a shorted stator winding','B) External rotor resistance was increasing slip and reducing speed — now removed for normal operation','C) Synchronous speed of this motor is 1,740 RPM','D) The motor was single-phasing before the resistance change'],
  answer:1,
  explanation:'<strong>External rotor resistance increases slip, reducing speed.</strong> Wound-rotor motors use external resistance to limit starting current and control speed. When resistance is removed (short-circuited), slip decreases and speed approaches synchronous speed. 1,800 RPM synchronous at 60 Hz for a 4-pole motor; 1,740 RPM represents normal running slip.',
  keyConcept:'Wound-rotor speed control: more external resistance = more slip = lower speed. Zero resistance = minimum slip = maximum speed.'},

  {id:114,topic:'motors',topicLabel:'Motors & Drives',diff:'medium',
  text:"A 460V, 3-phase motor nameplate shows FLA=42A and service factor (SF)=1.15. The motor is running at 46A continuously. What action is MOST appropriate?",
  options:['A) Immediately shut down — current exceeds FLA','B) No action needed — 46A is within the SF rating of 48.3A','C) Replace overload relay set to 42A','D) Add capacitor bank to reduce current draw'],
  answer:1,
  explanation:'<strong>Service factor allows continuous operation above FLA.</strong> 42A × 1.15 SF = 48.3A maximum continuous rating. Running at 46A is within the service factor. However, if ambient temperature exceeds nameplate rating or altitude is above 3,300 ft, SF may be derated.',
  keyConcept:'Motor SF: nameplate FLA × SF = maximum continuous current. Operation within SF is acceptable but reduces motor life.'},

  {id:115,topic:'motors',topicLabel:'Motors & Drives',diff:'hard',
  text:"A megohmmeter test on a 600V motor shows 10 MΩ insulation resistance at 20°C. Industry standards (IEEE 43) require a minimum of 1 MΩ per kV plus 1 MΩ. The motor is rated 50 HP. Is the insulation acceptable?",
  options:['A) No — 10 MΩ is below the 50 MΩ minimum for a 50 HP motor','B) Yes — 10 MΩ far exceeds the 1 MΩ minimum for 600V equipment','C) No — temperature correction required before assessment','D) Yes — only the polarization index matters, not spot resistance'],
  answer:1,
  explanation:'<strong>IEEE 43 minimum: 1 MΩ/kV of rated voltage + 1 MΩ.</strong> For a 600V (0.6 kV) motor: 0.6 + 1 = 1.6 MΩ minimum. The measured 10 MΩ far exceeds this. Temperature correction is recommended for trending but not required for a pass/fail assessment at this margin. Note: values below 100 MΩ warrant investigation for new motors.',
  keyConcept:'Megohm test minimum: 1 MΩ/kV + 1 MΩ. Below 1 MΩ = fail. Temperature correction (PI) = R10min / R1min ≥ 1.5 is ideal.'},

  {id:116,topic:'plc',topicLabel:'PLCs & Controls',diff:'hard',
  text:"A PLC output (O:0/1) should energize a motor starter when pushbutton I:0/0 and proximity sensor I:0/2 are both active. Both input LEDs are lit, but the motor does not start. The output LED is also lit. What is the MOST likely fault?",
  options:['A) The output module is failed internally','B) The control wiring from the PLC output to the motor starter coil is open or the coil has failed','C) The PLC program is missing the input rungs','D) PLC power supply is low'],
  answer:1,
  explanation:'<strong>If the output LED is lit, the PLC logic is working correctly.</strong> The output image bit is set. The fault lies in the field wiring from the output terminal to the motor starter coil — an open circuit (broken wire, loose terminal, blown fuse) or a failed starter coil. Trace with a voltmeter from the output terminal.',
  keyConcept:'Troubleshoot PLC outputs in order: PLC logic (LEDs/program) → output module terminal voltage → field wiring → load device.'},

  {id:117,topic:'plc',topicLabel:'PLCs & Controls',diff:'hard',
  text:"A PLC program controls a pump with a timed auto-shutoff. The timer (TON) has a preset of 300 seconds. The pump starts correctly but never shuts off automatically. The timer accumulated value shows 0 even while the pump runs. What is the MOST likely cause?",
  options:['A) Timer coil is wired in parallel with the pump output — incorrect logic','B) The enable rung for the timer (EN bit) is not latched — the timer resets every scan','C) Timer base is set to 1.0 second instead of 0.01','D) Output coil is addressed incorrectly'],
  answer:1,
  explanation:'<strong>TON timers require the enable rung to stay TRUE continuously to accumulate.</strong> If the rung goes FALSE for even one scan (due to a momentary condition), the timer resets to zero. The accumulated value staying at 0 means the enable rung is not holding TRUE. Check for momentary contacts or latch the enable condition.',
  keyConcept:'TON timer: EN rung must stay TRUE continuously. If EN goes FALSE, accumulated value resets to 0. Use a seal-in contact if needed.'},

  {id:118,topic:'plc',topicLabel:'PLCs & Controls',diff:'medium',
  text:"During commissioning, a conveyor starts immediately when PLC power is applied without any operator input. All field wiring is confirmed correct. What programming error is MOST likely?",
  options:['A) The output is wired to the wrong physical terminal','B) An output coil exists on an unconditional rung (no input conditions)','C) A normally closed contact is used where normally open is needed','D) The scan time is set too short for the input to register'],
  answer:1,
  explanation:'<strong>An unconditional rung energizes the output every scan.</strong> If an output coil is placed on a rung with no input contacts (or all conditions are always TRUE), it energizes at power-up. This is a common programming error when copying rungs without clearing input conditions. Add a start button contact to the rung.',
  keyConcept:'Every output coil should have at least one input condition. Unconditional output rungs = immediate energization at power-up.'},

  {id:119,topic:'power',topicLabel:'Power Systems',diff:'hard',
  text:"A technician measures 480V phase-to-phase on all phases of a 480Y/277V system but only 160V phase-to-neutral on all three phases. What is the MOST likely cause?",
  options:['A) Single phase failure on Phase A','B) Open neutral conductor on the secondary of the supply transformer','C) High-resistance ground fault on Phase B','D) Transformer tap set incorrectly'],
  answer:1,
  explanation:'<strong>A lost neutral causes all phase-to-neutral voltages to equalize incorrectly.</strong> With no neutral reference, phase-to-neutral voltage is determined by load balance. With balanced loads, all three phases still show correct phase-to-phase (480V), but phase-to-neutral may show unequal or unexpected values. 160V on all phases indicates neutral is open and loads are shifting the neutral point.',
  keyConcept:'Open neutral symptoms: correct phase-to-phase voltage + abnormal phase-to-neutral voltages. Can damage equipment connected phase-to-neutral.'},

  {id:120,topic:'power',topicLabel:'Power Systems',diff:'hard',
  text:"A delta-wye transformer bank is operating with one transformer failed open on the delta primary side. What type of operation results and what is the capacity change?",
  options:['A) System shuts down completely — three phases cannot be produced','B) Open-delta (V-connection) continues three-phase output at 57.7% of original kVA capacity','C) Output becomes single-phase only at full voltage','D) Remaining two transformers increase output to 75% to compensate'],
  answer:1,
  explanation:'<strong>Open-delta still produces balanced three-phase voltage.</strong> Two transformers in a V-connection provide three-phase output with correct phase angle relationships, but at only 57.7% (1/√3) of original three-transformer kVA. This is an emergency operating mode — both remaining transformers must carry increased current. They should be derated to prevent overheating.',
  keyConcept:'Open-delta: 3-phase voltage maintained, capacity = 57.7% of full delta bank. Used as emergency measure only.'},

  {id:121,topic:'power',topicLabel:'Power Systems',diff:'hard',
  text:"A 313A electrician is performing a power factor test on a plant distribution system. The power meter shows 500 kW real power and 600 kVA apparent power. What is the power factor and what corrective measure is needed?",
  options:['A) PF=0.60 — add capacitor bank sized for 80 kVAR','B) PF=0.83 — no correction needed above 0.80','C) PF=0.83 — add capacitor bank to correct to 0.95 or above for utility billing','D) PF=1.20 — system is overcorrected, remove capacitors'],
  answer:2,
  explanation:'<strong>PF = kW / kVA = 500/600 = 0.833.</strong> Most utilities penalize below 0.90 or 0.95 PF. To correct from 0.833 to 0.95: required kVAR = kW(tan θ₁ - tan θ₂) = 500(tan 33.6° - tan 18.2°) = 500(0.664 - 0.329) = 167 kVAR of capacitors needed. This eliminates utility PF penalty charges.',
  keyConcept:'PF = kW/kVA. PF correction: add capacitors sized for the kVAR difference between current and target angle.'},

  {id:122,topic:'instrumentation',topicLabel:'Instrumentation',diff:'hard',
  text:"A 4-20mA loop-powered transmitter reads 3.6mA with the process at 0% (minimum range). What does this indicate and what should the technician do FIRST?",
  options:['A) Normal — some transmitters operate below 4mA at process zero','B) Broken signal wire — replace immediately','C) Transmitter fault or calibration drift — verify loop supply voltage and check transmitter zero trim','D) PLC analog input card has failed'],
  answer:2,
  explanation:'<strong>4mA is the minimum live-zero standard — 3.6mA indicates a transmitter fault.</strong> In a 4-20mA system, 4mA = 0% process. Below 4mA is outside the valid range and indicates transmitter fault, severely low loop supply voltage (< 12V at transmitter), or calibration drift. Check supply voltage first (should be 24VDC minus line drops), then recalibrate or replace the transmitter.',
  keyConcept:'4-20mA live zero: 4mA=0%, 20mA=100%, <4mA=fault/wire break alarm. Loop supply must maintain minimum 12V at transmitter terminals.'},

  {id:123,topic:'instrumentation',topicLabel:'Instrumentation',diff:'hard',
  text:"A Type J thermocouple is installed in a furnace. The DCS reads 280°C while a calibrated RTD reference shows 230°C. What is the MOST likely cause of the 50°C offset?",
  options:['A) The thermocouple extension wire has a junction break','B) The controller is configured for Type K instead of Type J thermocouple','C) Ambient temperature at the terminal block exceeds 50°C','D) The thermocouple is installed backwards (reversed polarity)'],
  answer:1,
  explanation:'<strong>Wrong thermocouple type in the controller causes a systematic temperature offset.</strong> Type J and Type K have different millivolt-per-degree output curves. A Type J thermocouple at 230°C outputs ~12.4 mV. If the controller reads this using Type K tables (which expect ~9.4 mV for 230°C), it will calculate a higher temperature. This is a configuration error, not a hardware failure.',
  keyConcept:'Type J thermocouple: Fe/constantan, range -40 to 750°C. Type K: Ni-Cr/Ni-Al. Using wrong table causes systematic offset. Always verify controller TC type setting during commissioning.'},

  {id:124,topic:'instrumentation',topicLabel:'Instrumentation',diff:'medium',
  text:"A differential pressure flow transmitter shows zero flow even though the pump is running and valves are open. The impulse lines are checked and found to be open. What should the technician suspect FIRST?",
  options:['A) Flow element (orifice plate) installed backwards','B) Transmitter low-side equalizing valve left open (bypassing differential pressure)','C) Pump cavitation causing flow fluctuation','D) PLC analog input scaled incorrectly'],
  answer:1,
  explanation:'<strong>An open equalizing valve bypasses both high and low pressure to the same value, resulting in zero differential.</strong> Differential pressure transmitters have a 3-valve manifold: two block valves and one equalizer. If the equalizer is open, HP and LP sides equalize — zero ΔP, zero indicated flow. Close the equalizer, open both block valves in the correct sequence.',
  keyConcept:'DP transmitter 3-valve manifold operation: 1) Close equalizer. 2) Open HP block valve. 3) Open LP block valve. Reverse to isolate.'},

  {id:125,topic:'safety',topicLabel:'Safety & Code',diff:'hard',
  text:"A 313A electrician is performing work on a 600V motor control center (MCC). CSA Z462 requires establishment of an electrically safe work condition. In the correct sequence, what is the THIRD step?",
  options:['A) Verify absence of voltage with a properly rated test instrument','B) Apply lockout/tagout devices to all energy isolation points','C) Visually verify all circuits are de-energized','D) Release or restrain stored energy (capacitors, springs)'],
  answer:0,
  explanation:'<strong>CSA Z462 Electrically Safe Work Condition sequence: 1) Identify all sources. 2) Notify affected employees. 3) De-energize equipment. 4) Operate disconnects. 5) Release stored energy. 6) Apply LOTO. 7) Verify absence of voltage.</strong> The third step is to de-energize (operate the disconnecting means), then release stored energy, then LOTO, then verify. Verification is the LAST step.',
  keyConcept:'LOTO sequence: Identify sources → Notify → De-energize → Release stored energy → LOTO → Verify absence of voltage.'},

  {id:126,topic:'safety',topicLabel:'Safety & Code',diff:'hard',
  text:"An arc flash hazard analysis determines the incident energy at a panel is 12 cal/cm². What PPE category is required per NFPA 70E / CSA Z462 and what is the minimum arc rating?",
  options:['A) PPE Category 1 — 4 cal/cm² rated suit','B) PPE Category 2 — 8 cal/cm² rated suit','C) PPE Category 3 — 25 cal/cm² rated suit','D) No PPE required — below 1.2 cal/cm² threshold'],
  answer:2,
  explanation:'<strong>PPE Category selection is based on incident energy level.</strong> Category 1: <4 cal/cm². Category 2: 4-8 cal/cm². Category 3: 8-25 cal/cm². Category 4: 25-40 cal/cm². At 12 cal/cm², Category 3 PPE with minimum 25 cal/cm² arc-rated suit, face shield, insulating gloves, and hearing protection is required. The PPE rating must EXCEED the incident energy.',
  keyConcept:'Arc flash PPE: always select the category ABOVE the incident energy level. 12 cal/cm² → Category 3 (25 cal/cm² minimum).'},

  {id:127,topic:'theory',topicLabel:'Theory',diff:'hard',
  text:"A 313A electrician measures a single-phase 120V AC circuit drawing 15A with a power factor of 0.75 lagging. What is the true (real) power consumed?",
  options:['A) 1,350 W','B) 1,800 W (apparent power)','C) 1,800 VA','D) 2,400 W'],
  answer:0,
  explanation:'<strong>Real power = V × I × PF = 120 × 15 × 0.75 = 1,350 W.</strong> Apparent power = V × I = 120 × 15 = 1,800 VA. Real power (watts) does actual work. The remaining 1,800 - 1,350 = 450 VAR is reactive power (stored/returned by inductance or capacitance). Power factor = cos θ = real/apparent = 0.75.',
  keyConcept:'P (watts) = V × I × PF. S (VA) = V × I. Q (VAR) = V × I × sin θ. PF = P/S = cos θ.'},

  {id:128,topic:'theory',topicLabel:'Theory',diff:'hard',
  text:"A technician performs a voltage drop test on a 120V, 20A branch circuit supplying a load 50m from the panel. The voltage drop measured is 8V (6.7%). What corrective action should be taken per CEC requirements?",
  options:['A) No action needed — CEC allows up to 10% voltage drop','B) Replace the load with a lower-power model','C) Increase conductor size to reduce resistance and voltage drop below CEC recommended 3% (branch) or 5% (total)','D) Add a voltage regulator at the load end'],
  answer:2,
  explanation:'<strong>CEC recommends maximum 3% voltage drop on branch circuits and 5% total (feeder + branch).</strong> At 6.7% drop, the conductor is undersized for the run. Voltage drop = I × R; reduce R by increasing conductor cross-section. Use the voltage drop formula to select the correct conductor: larger AWG = lower resistance = less voltage drop.',
  keyConcept:'CEC voltage drop limits: 3% branch circuit, 2% feeder, 5% total. Formula: VD = (2 × L × I × R/1000) for single-phase.'},

  {id:129,topic:'motors',topicLabel:'Motors & Drives',diff:'medium',
  text:"A technician uses a clamp meter to measure current on a 3-phase motor with star (Y) connection. Each phase measures 18A. What is the line current feeding this motor?",
  options:['A) 31.2A (18 × √3)','B) 18A — line and phase currents are equal in Y connection','C) 10.4A (18 / √3)','D) 54A (18 × 3)'],
  answer:1,
  explanation:'<strong>In a star (Y) connected motor, line current equals phase current.</strong> In Y connection: I_line = I_phase = 18A. Only voltage differs: V_line = V_phase × √3. This is opposite to delta: in delta, I_line = I_phase × √3, but V_line = V_phase. The clamp meter on each supply line will read 18A.',
  keyConcept:'Y connection: I_L = I_phase, V_L = V_phase × √3. Delta: I_L = I_phase × √3, V_L = V_phase.'},

  {id:130,topic:'plc',topicLabel:'PLCs & Controls',diff:'hard',
  text:"A technician is troubleshooting a PLC-controlled system. The physical motor runs but the PLC output LED is OFF. The motor starter coil is confirmed energized from an external source. What does this indicate?",
  options:['A) Output module has failed — replace immediately','B) The motor is bypassed around the PLC — the PLC output is not the source of control','C) PLC is in run mode but program scan is suspended','D) The output module LED is defective'],
  answer:1,
  explanation:'<strong>If the motor is running but the PLC output LED is off, the motor is being energized by something other than the PLC output.</strong> A bypass switch, parallel wiring, or a manual override may be energizing the starter coil directly. This is a safety concern — if the PLC output is supposed to control the motor, the bypass must be identified and documented. Trace the starter coil wiring.',
  keyConcept:'Rule: If output LED=OFF but load is energized, the load has an alternate power source. Always trace full circuit during troubleshooting.'},

  {id:131,topic:'power',topicLabel:'Power Systems',diff:'medium',
  text:"A 313A electrician is sizing a feeder for a 75 HP, 460V, 3-phase motor (FLA=92A). Per CEC Rule 28-106, the feeder conductor minimum ampacity must be at least what percentage of the motor FLA?",
  options:['A) 100% of FLA = 92A','B) 115% of FLA = 105.8A','C) 125% of FLA = 115A','D) 150% of FLA = 138A'],
  answer:2,
  explanation:'<strong>CEC Rule 28-106 requires motor branch circuit conductors rated at minimum 125% of motor FLA.</strong> 92A × 1.25 = 115A minimum ampacity. This accounts for motor starting conditions and continuous duty heat. The overcurrent protection (breaker/fuse) is sized separately per Rule 28-200 and can be higher (up to 250% for inverse time breakers).',
  keyConcept:'CEC motor conductor sizing: minimum 125% of FLA. Protection device sizing: up to 150–250% of FLA depending on type (per CEC Rule 28-200).'},

  {id:132,topic:'instrumentation',topicLabel:'Instrumentation',diff:'medium',
  text:"An RTD (Pt100) temperature sensor reads -40°C in an oven that is clearly at room temperature (~22°C). A technician measures 50 Ω resistance at the RTD terminals at the DCS. What is the MOST likely fault?",
  options:['A) RTD element has failed open','B) RTD extension wires are short-circuited together at some point','C) The DCS analog card has failed','D) RTD calibration drift from overheating'],
  answer:1,
  explanation:'<strong>A shorted RTD lead appears as lower resistance than actual temperature.</strong> Pt100 resistance at 22°C ≈ 108.5 Ω. A short circuit somewhere in the 3-wire RTD leads reduces measured resistance below actual, making the DCS calculate a lower (incorrect) temperature. At 50 Ω, the indicated temperature would be around -130°C on a Pt100 curve, but -40°C indicates a partial short or the short is at a different point.',
  keyConcept:'Pt100 RTD: R = 100 Ω at 0°C, increases ~0.385 Ω/°C. Open circuit → reading too high (∞). Short circuit → reading too low.'},

  {id:133,topic:'theory',topicLabel:'Theory',diff:'medium',
  text:"A 313A electrician installs a 100 kVAR capacitor bank to correct power factor from 0.75 to above 0.95 on a 460V plant distribution. During testing, the technician notices the downstream bus voltage has risen by 3%. What is the MOST likely explanation?",
  options:['A) Capacitors are drawing more current than expected','B) Capacitive reactive power is counteracting inductive voltage drop in the feeder — this is normal and desirable','C) The capacitor bank is oversized and causing leading power factor','D) Transformer tap must be adjusted to compensate'],
  answer:1,
  explanation:'<strong>Capacitor banks raise bus voltage by reducing reactive current in the feeder.</strong> Reactive current causes voltage drop (I × X_L). Adding capacitive reactive power reduces net reactive current, which reduces voltage drop in the feeder impedance, resulting in higher terminal voltage. A 2-4% voltage rise from PF correction is normal and typically beneficial for motors.',
  keyConcept:'Capacitor banks: 1) Correct PF. 2) Reduce reactive current. 3) Raise local bus voltage. 4) Reduce distribution losses. All are desirable effects.'},

  {id:134,topic:'safety',topicLabel:'Safety & Code',diff:'medium',
  text:"A 313A electrician is working in a Class I, Division 1 hazardous location. Which of the following luminaires is acceptable for this area?",
  options:['A) Standard fluorescent strip light in a conduit system','B) CSA-certified explosion-proof (Ex d) luminaire rated for Class I, Division 1','C) Vapour-tight IP66 luminaire with standard ballast','D) LED panel light with glass lens'],
  answer:1,
  explanation:'<strong>Class I, Division 1 locations contain flammable gases or vapours under normal operating conditions.</strong> Only CSA-certified explosion-proof (Ex d) or intrinsically safe equipment is permitted. Vapour-tight fixtures are for Division 2 (abnormal conditions only). The containment rating (explosion-proof enclosure) prevents internal arcs from igniting the external atmosphere.',
  keyConcept:'Class I Div 1: flammable gas present under normal conditions → explosion-proof (Ex d) equipment required. Div 2: only present under abnormal → vapour-tight acceptable.'},

  {id:135,topic:'motors',topicLabel:'Motors & Drives',diff:'hard',
  text:"A 313A electrician performs a polarization index (PI) test on a large 4.16kV motor. The 1-minute resistance is 80 MΩ and the 10-minute resistance is 120 MΩ. What is the PI and is the insulation acceptable?",
  options:['A) PI=1.5 — borderline, monitor closely','B) PI=0.67 — unacceptable, insulation has moisture or contamination','C) PI=1.5 — acceptable, insulation is dry and healthy','D) PI=1.5 — unacceptable, PI must be ≥ 2.0 for motors above 1 kV'],
  answer:2,
  explanation:'<strong>PI = R₁₀ min / R₁ min = 120/80 = 1.5.</strong> IEEE 43 states: PI <1.0 = unacceptable (shorted/wet); PI 1.0-2.0 = questionable for machines rated above 1 kV; PI > 2.0 = acceptable for motors above 1 kV. At 1.5, this motor is questionable and should be cleaned/dried before energizing. For motors below 1 kV, PI > 1.5 may be acceptable.',
  keyConcept:'PI = R10min / R1min. For motors >1 kV: PI <1.0=danger, 1.0-2.0=questionable, >2.0=good. Test voltage: 500V for <1 kV, 1000V for 1-5 kV.'}
"""

def main():
    f = ROOT / '313a.html'
    text = f.read_text(encoding='utf-8')

    # Find the closing ]; of the questions array
    close_idx = text.rfind('\n];')
    if close_idx < 0:
        sys.stdout.buffer.write(b'ERROR: could not find ]; in 313a.html\n')
        return

    # Insert before the closing ];
    new_text = text[:close_idx] + ',\n' + NEW_QUESTIONS.strip() + '\n' + text[close_idx:]
    f.write_text(new_text, encoding='utf-8')

    # Verify
    import re
    ids = re.findall(r'\bid:(\d+)', new_text)
    sys.stdout.buffer.write(f'313a.html: {len(ids)} questions total (was 110)\n'.encode())

if __name__ == '__main__':
    main()
