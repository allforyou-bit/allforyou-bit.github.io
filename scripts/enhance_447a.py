"""Enhance explanations for 447A — 6 selected questions."""
from pathlib import Path
import re, sys

def safe_print(text):
    sys.stdout.buffer.write((str(text) + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()

ENHANCEMENTS = {
    3: (
        "Threading oil (cutting oil) lubricates and cools the die head during threading, preventing die wear and producing clean, accurate threads.",
        "Threading oil (cutting oil) lubricates and cools the die head during the threading operation, preventing die wear, reducing friction, and producing clean, accurate threads with proper form. Wrong answers: water or general lubricant (WD-40, grease) are not acceptable \u2014 water causes corrosion and does not provide adequate lubrication for cutting; WD-40 is a penetrant/light lubricant not formulated for metal cutting. Pipe dope or Teflon tape are used for sealing threaded joints after assembly, not during cutting. If threading oil is not used, the result is torn, ragged threads (not to NPT standard), accelerated die wear, and fittings that will leak. Black pipe threading oil is typically dark coloured; some jobs use white threading oil for stainless pipe."
    ),
    8: (
        "A flaring tool creates a conical (bell-shaped) flare on the end of soft copper or aluminum tubing, used for compression flare fittings in refrigeration and gas lines.",
        "A flaring tool creates a 45\u00b0 conical flare on the end of soft copper or aluminum tubing by expanding the tube end into a bell shape that seats against the flare fitting body, creating a metal-to-metal seal. Wrong answers: a flaring tool is not used for soldering (that requires flux, solder, and heat), not for cutting tube (that\u2019s a tube cutter or hacksaw), and not for bending (that\u2019s a tube bender or spring bender). The flare must seat fully and evenly \u2014 a cracked, oval, or partial flare will leak. CSA B149.1 permits flare fittings for gas service on copper tubing. Common exam point: SAE 45\u00b0 flare vs 37\u00b0 flare (AN/JIC) \u2014 45\u00b0 is standard for plumbing/HVAC, while 37\u00b0 is used in hydraulic/fuel systems."
    ),
    72: (
        "Gas piping must maintain a minimum 25 mm (1 in) clearance from electrical conduit, wiring, and other services to prevent damage and provide access for inspection.",
        "CSA B149.1 requires a minimum 25 mm (1 in) clearance between gas piping and electrical conduit, wiring, or other services. This clearance prevents: mechanical damage if the electrical conduit or gas pipe moves or vibrates; heat transfer from electrical equipment to gas fittings; and electrolytic corrosion where gas pipe contacts dissimilar metal in conduit. Clearance also allows visual inspection for leaks along the gas pipe run. Wrong answers: zero clearance (touching) violates B149.1 and is a failed inspection; 100 mm is a clearance requirement for other scenarios (e.g., gas meters to electrical meters), not pipe-to-conduit. During rough-in inspection, inspectors specifically check gas-to-electrical separation \u2014 flag it early rather than moving pipe after drywalling."
    ),
    82: (
        "The fill valve (ballcock) senses the low water level in the tank after a flush and opens to refill the tank to the proper level, then closes automatically.",
        "The fill valve (ballcock or float valve) senses the low water level in the tank after a flush \u2014 via a float ball or pressure-sensing diaphragm \u2014 and opens the water supply to refill the tank to the correct water level, then closes automatically when the float rises to the set point. Wrong answers: the fill valve does not control flushing (that is the flush valve or flapper, which opens when the trip lever is pressed and closes when the tank empties); it does not regulate supply pressure (that is a pressure-reducing valve upstream). Common failure: fill valve that does not fully close \u2014 water runs continuously into the overflow tube (\u201cphantom flushing\u201d). Fix: adjust float arm height or replace fill valve assembly. Red Seal exam often asks to distinguish fill valve vs flush valve function."
    ),
    88: (
        "Angle stop valves (quarter-turn angle valves or supply stop valves) are used at fixture supply connections (toilet, lavatory, sink) to allow shutoff of water to individual fixtures",
        "Angle stop valves (also called supply stop valves or fixture shutoffs) are installed at each toilet, lavatory, and sink to allow individual fixture shutoff for service or replacement without shutting off the whole building. Wrong answers: gate valves are used for main shutoffs (not at fixtures \u2014 they are too large and slow to operate); ball valves are also used for shutoffs but not typically at the small-diameter fixture supply; check valves prevent backflow and do not allow shutoff. Angle stops come in 1/4-turn and multi-turn types; 1/4-turn ball-type stops have replaced traditional multi-turn packing valves in most applications because they are less likely to fail or seize in the open position. Important: always install angle stops accessible for inspection and operation \u2014 under sinks, behind toilets, not behind walls."
    ),
    89: (
        "Dual-flush toilets offer a reduced flush (approximately 3 L) for liquid waste and a full flush (up to 6 L) for solid waste, reducing average water consumption compared to single-fl",
        "Dual-flush toilets provide two flush volumes: approximately 3 L (half-flush) for liquid waste and up to 6 L (full flush) for solid waste \u2014 compared to older single-flush toilets that used 13\u201320 L per flush. This meets the National Energy Code and provincial water efficiency requirements. Wrong answers: dual-flush toilets do not use higher pressure than standard toilets (pressure-assist is a different technology); they do not require a different trap arm size; the 3L/6L volumes are the maximum, not guaranteed usage (actual consumption depends on water pressure). Under the Canadian Model National Energy Code and many provincial codes, dual-flush or low-consumption toilets (\u22646 L) are now required in new construction. Red Seal point: know that 6 L is the maximum flush volume allowed for new toilets in Canada \u2014 not 13 L."
    ),
}

filepath = Path('447a.html')
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

safe_print(f'\nTotal enhanced: {changed}/6')
safe_print(f'File size change: {len(content) - original_len:+d} chars')

filepath.write_text(content, encoding='utf-8')

ids = re.findall(r'\bid:\s*(\d+)', content)
safe_print(f'Total questions: {len(ids)} (should be 135)')
