"""Enhance explanations for 313A — 4 selected questions."""
from pathlib import Path
import re, sys

def safe_print(text):
    sys.stdout.buffer.write((str(text) + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()

ENHANCEMENTS = {
    13: (
        "CEC Section 2 contains general rules, definitions, approval requirements, and administrative provisions that apply throughout the code.",
        "CEC Section 2 (General Rules) contains foundational requirements \u2014 definitions, approval of equipment and materials, marking and identification, and administrative rules \u2014 that apply to all other sections of the code unless specifically modified. Wrong answers confuse it with: Section 10 (Grounding and bonding), Section 12 (Wiring methods), or Section 26 (Installation of electrical equipment). Section 2 is important for industrial electricians because it defines \u2018approved\u2019 equipment (CSA/UL listed or acceptable equivalent), sets the authority having jurisdiction (AHJ) as the final arbiter, and establishes that the CEC is a minimum standard \u2014 AHJ can and often does add local requirements. On Red Seal exams, Section 2 questions often test whether candidates know what \u2018approved\u2019 means (certified by an accredited testing organization, not just brand-name)."
    ),
    32: (
        "Reversing any two of the three phase connections to an induction motor reverses the rotating magnetic field direction, causing the rotor to rotate in the opposite direction.",
        "Reversing any two of the three phase connections (e.g., swap T1 and T2, leaving T3 in place) reverses the phase sequence of the rotating magnetic field in the stator, which causes the rotor to follow in the opposite direction. Wrong answers: reversing all three connections does NOT reverse direction \u2014 A-B-C to C-B-A is the same as reversing two (it changes the phase sequence from ABC to CBA = reverse); reversing only one connection does not produce a valid three-phase sequence and would result in single-phasing. The motor starter reversing contactor physically swaps two leads (typically T1 and T3) when the reverse coil is energized. Red Seal key point: only swapping TWO leads reverses rotation; swapping one results in a fault; swapping all three = same as swapping two (still reversal)."
    ),
    72: (
        "A P&ID (also called a P&ID diagram) uses ISA 5.1 standard symbols to show all process piping, vessels, equipment, instruments, valves, and control loops in a schematic form \u2014 the b",
        "A P&ID (Piping and Instrumentation Diagram) uses ISA 5.1 / ISA-5.1 standard symbols to schematically show all process piping, vessels, pumps, valves, instruments, and control loops \u2014 it is the primary reference document for industrial electricians during instrumentation installation, commissioning, and troubleshooting. Wrong answers: a P&ID is NOT a physical layout drawing (that is a general arrangement or plot plan); it is NOT a ladder logic diagram (that is the PLC program); it is NOT an electrical single-line diagram (that shows power distribution). Key distinction: P&ID shows WHAT instruments exist and HOW they connect to control loops; it does not show physical location or dimensions. Industrial electricians use P&IDs to identify instrument tag numbers (e.g., FT-101 = Flow Transmitter 101), understand signal types (4\u201320 mA, digital), and trace loop documentation."
    ),
    82: (
        "Delta-wye transformers provide a ground reference (neutral) on the secondary side, allowing 3-phase 4-wire systems with both 3-phase (line-to-line, e.g., 600V) and single-phase (line-to-",
        "A delta-wye (\u0394-Y) transformer has the primary wound in delta (no neutral) and the secondary wound in wye (star) with a grounded neutral point. This provides a 4-wire system on the secondary, delivering both 3-phase line-to-line voltage (e.g., 600V L-L) and single-phase line-to-neutral voltage (e.g., 347V L-N = 600/\u221a3). Wrong answers: wye-delta has the neutral on the primary side only and is typically used for motor loads or power factor correction; delta-delta has no neutral on either side (used for motor loads where no single-phase branch circuits are needed). The delta-wye configuration also blocks certain harmonic currents (triplen harmonics) from passing between primary and secondary. Red Seal point: 600V/347V systems in Canada use delta-wye transformers so that 347V single-phase branch circuits (lighting) can be supplied from the same transformer as 600V 3-phase motor loads."
    ),
}

filepath = Path('313a.html')
content = filepath.read_text(encoding='utf-8')
original_len = len(content)

changed = 0
for qid, (old_snippet, new_expl) in ENHANCEMENTS.items():
    id_pattern = f'id:{qid},'
    idx = content.find(id_pattern)
    if idx == -1:
        safe_print(f'Q{qid}: id pattern not found')
        continue

    next_q = content.find(',{id:', idx + 1)
    if next_q == -1:
        next_q = idx + 6000

    block = content[idx:next_q]
    exp_start = block.find("explanation:'")
    if exp_start == -1:
        safe_print(f'Q{qid}: explanation field not found')
        continue

    exp_val_start = exp_start + len("explanation:'")
    exp_val_end = exp_val_start
    while exp_val_end < len(block):
        if block[exp_val_end] == "'" and block[exp_val_end-1] != '\\':
            break
        exp_val_end += 1

    abs_start = idx + exp_val_start
    abs_end = idx + exp_val_end
    content = content[:abs_start] + new_expl + content[abs_end:]
    safe_print(f'Q{qid}: enhanced')
    changed += 1

safe_print(f'\nTotal enhanced: {changed}/4')
safe_print(f'File size change: {len(content) - original_len:+d} chars')

filepath.write_text(content, encoding='utf-8')

ids = re.findall(r'\bid:\s*(\d+)', content)
safe_print(f'Total questions: {len(ids)} (should be 135)')
