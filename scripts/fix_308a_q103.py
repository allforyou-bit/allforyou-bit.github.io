"""Replace 308A Q103 (duplicate) with new Controls question."""
from pathlib import Path
import re, sys

def safe_print(text):
    sys.stdout.buffer.write((str(text) + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()

OLD_Q103 = """  {id:103,topic:'components',topicLabel:'System Components',diff:'medium',
   text:'What is the purpose of a crankcase heater on a refrigeration or AC compressor?',
   options:['A) To heat the compressor oil before startup to reduce viscosity and improve lubrication during initial operation','B) To prevent refrigerant migration into the compressor crankcase during the off cycle \\u2014 refrigerant dissolves in oil when the compressor is cold, and vaporizes on startup causing oil foaming and loss of lubrication','C) To maintain minimum operating temperature for cold-weather operation of the compressor','D) To heat the refrigerant vapour before compression to prevent liquid slugging on startup'],
   answer:1,
   explanation:'<strong>Crankcase heater prevents refrigerant migration \\u2014 refrigerant dissolves in cold oil during off cycle and causes oil foaming on startup.</strong> During the off cycle, the compressor crankcase is the coldest point in the system (heat migrates toward cold). Refrigerant vapour migrates and condenses/dissolves in the compressor oil. On startup, pressure drop causes the refrigerant to flash out of the oil \\u2014 creating foam, which provides no lubrication. The heater keeps the oil warm enough to prevent excessive refrigerant absorption.',
   keyConcept:'Crankcase heater: essential for copeland scroll, semi-hermetic, and open-type compressors. Watt density: typically 50-150W. Always energized during off cycle (not during operation \\u2014 remove power on startup, or use PTCR type that reduces power when running). Refrigerant migration symptoms: oil foaming on startup, liquid slugging (liquid refrigerant entering cylinders), compressor noise/damage. Belly band heater vs immersion heater (POE compatible). Always check crankcase heater operation during PM.'},"""

NEW_Q103 = """  {id:103,topic:'controls',topicLabel:'Controls & Electrical',diff:'medium',
   text:'A walk-in cooler compressor trips repeatedly on the low-pressure cutout (LPC) during normal winter operation, yet the cooler is maintaining setpoint temperature. What is the MOST LIKELY cause and the correct remedy?',
   options:['A) Refrigerant overcharge is flooding the evaporator and lowering suction pressure — recover excess refrigerant','B) Low ambient temperature around the condenser is causing condensing pressure to drop; the low condensing pressure starves refrigerant flow through the TXV and suction pressure falls below the LPC setpoint — install a head pressure control (HPC) to maintain minimum condensing pressure in cold weather','C) The LPC setpoint is factory-set too high and should be adjusted upward in the field to stop nuisance trips','D) A restricted liquid line filter drier is reducing refrigerant flow and causing low suction pressure — replace the drier'],
   answer:1,
   explanation:'In cold weather, low ambient temperature reduces condenser heat rejection, causing condensing pressure (head pressure) to fall. A thermostatic expansion valve (TXV) requires a minimum pressure differential across it to meter refrigerant properly; when head pressure drops too low, refrigerant flow through the TXV decreases, suction pressure falls, and the LPC trips the compressor. The correct remedy is a head pressure control (HPC) — typically condenser fan cycling or a fan speed controller — that maintains minimum condensing pressure (commonly 100-120 psig / 690-830 kPa for R-404A) regardless of outdoor temperature. Adjusting the LPC setpoint downward would mask the real problem and risk compressor damage from loss of lubrication; a restricted drier would cause high superheat, not an LPC trip under normal load conditions.',
   keyConcept:'Head pressure control: required in cold-climate commercial refrigeration. Methods: condenser fan cycling (pressure or temperature controlled), fan speed drive (VFD), or flooding the condenser with refrigerant (flooding valve). Minimum condensing pressure prevents: TXV starvation, LPC trips, and compressor lubrication loss. LPC nuisance trips in winter = first suspect head pressure control failure or absence.'},"""

filepath = Path('308a.html')
content = filepath.read_text(encoding='utf-8')

# Find the old Q103 block by its unique start signature
old_sig = "  {id:103,topic:'components',topicLabel:'System Components',diff:'medium',"
if old_sig not in content:
    safe_print('ERROR: Old Q103 signature not found in 308a.html')
    safe_print('Trying line-by-line search...')
    # Find the line
    for i, line in enumerate(content.split('\n'), 1):
        if 'id:103' in line:
            safe_print(f'Line {i}: {line[:120]}')
    sys.exit(1)

# Find start and end of Q103 block
start_idx = content.index(old_sig)
# End is where Q104 starts: ,\n  {id:104,
end_sig = "\n  {id:104,"
end_idx = content.index(end_sig, start_idx)

old_block = content[start_idx:end_idx]
safe_print(f'Old Q103 block found ({len(old_block)} chars)')
safe_print(f'Old block starts: {old_block[:80]}')

new_content = content[:start_idx] + NEW_Q103 + content[end_idx:]

# Verify
if "id:103,topic:'controls'" not in new_content:
    safe_print('ERROR: New Q103 not inserted correctly')
    sys.exit(1)

if "id:103,topic:'components'" in new_content:
    safe_print('ERROR: Old Q103 still present')
    sys.exit(1)

# Count questions
ids = re.findall(r'\bid:\s*(\d+)', new_content)
safe_print(f'Total questions after edit: {len(ids)}')

filepath.write_text(new_content, encoding='utf-8')
safe_print('308a.html updated successfully.')
safe_print('Old Q103: components/crankcase heater (duplicate of Q78)')
safe_print('New Q103: controls/head pressure control (LPC nuisance trips in winter)')
