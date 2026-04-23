"""Enhance explanations for 276A — 8 selected questions."""
from pathlib import Path
import re, sys

def safe_print(text):
    sys.stdout.buffer.write((str(text) + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()

ENHANCEMENTS = {
    4: (
        "SMAW at 150\u2013200 A requires shade 10\u201311 to protect against the intense UV/IR radiation of the arc.",
        "SMAW at 150\u2013200 A requires a shade 10\u201311 lens to protect against the intense UV and infrared radiation of the welding arc. Using a lower shade (e.g., shade 8) would allow damaging UV/IR through and cause arc eye (photokeratitis) and retinal damage \u2014 symptoms appear hours after exposure. A shade 14 is unnecessarily dark (typically used for plasma cutting) and would make it difficult to see the weld pool. Shade selection increases with amperage: low-amperage SMAW (\u226475A) may use shade 8\u20139; 150\u2013200A uses 10\u201311; above 300A typically requires shade 12+. Always check CSA Z94.3 or the lens manufacturer's table for the correct shade by process and amperage."
    ),
    8: (
        "AWS D1.1 and CSA standards recommend a minimum of 2,000 cfm (cubic feet per minute) of fresh air per welder for mild steel.",
        "AWS D1.1 and CSA standards recommend a minimum of 2,000 cfm (approximately 57 m\u00b3/min) of fresh air per welder for mild steel welding to dilute and remove welding fumes. This is a general ventilation threshold \u2014 local exhaust ventilation (LEV/fume extraction gun) is preferred as it captures fumes at source and requires less total airflow. Wrong answers: 500 cfm is far too low for safe dilution; 10,000 cfm is appropriate for confined spaces or heavy-fume processes, not typical workshop SMAW. When welding coated, galvanized, or stainless steel, local exhaust is mandatory regardless of general ventilation levels because toxic fumes (zinc oxide, hexavalent chromium) exceed threshold limit values even with 2,000 cfm dilution."
    ),
    28: (
        "E=electrode, 70=70,000 psi tensile, 1=all-position, 8=low-hydrogen potassium flux, DCEP or AC capable.",
        "E7018 classification: E=electrode; 70=minimum 70,000 psi (480 MPa) tensile strength; 1=usable in all positions (flat, horizontal, vertical-up, overhead); 8=low-hydrogen potassium flux coating, usable on DCEP or AC. The \u20188\u2019 suffix (low-hydrogen) is the critical Red Seal exam point: E7018 requires electrodes to be stored in a rod oven at 120\u2013150\u00b0C and used within 4 hours of removal to prevent moisture absorption \u2014 hydrogen in the weld causes hydrogen-induced cracking. Wrong answers confuse E6010 (DCEP only, deep penetration, no oven needed) with E7018, or misread \u20181\u2019 (all-position) as \u20181G\u2019 flat-only. E7018 is the go-to code for structural steel where hydrogen cracking is a risk."
    ),
    30: (
        "E6013 (rutile) produces a soft, steady arc with easy slag removal and minimal penetration, reducing burn-through risk on thin materials.",
        "E6013 (rutile-coated) produces a soft arc, light spatter, easy slag removal, and shallow penetration \u2014 making it ideal for thin sheet metal where burn-through is the primary risk. Wrong answers: E6010 and E6011 have deep penetration and forceful arc (designed for root passes and pipe), which would easily burn through thin material. E7018 (low-hydrogen) is excellent for structural work but requires an oven and produces a broader bead; it is not the preferred choice for light gauge sheet. E6013\u2019s easy restriking and smooth bead also make it a good learning electrode, but its low penetration means it\u2019s NOT suitable for code-quality root passes or high-strength joints where full fusion is required."
    ),
    52: (
        "GMAW transfer modes: Short circuit (low voltage, short arc \u2014 thin metal), globular (large drops, spatter), spray (fine droplets, high quality), pulsed spray (controlled spray at lo",
        "The four GMAW transfer modes: (1) Short-circuit transfer \u2014 lowest voltage (14\u201319V), wire periodically touches the puddle, suitable for thin gauge and out-of-position, but risk of cold lap/incomplete fusion at heavy thickness; (2) Globular transfer \u2014 large irregular drops transfer erratically, high spatter, generally not a preferred mode in production; (3) Spray transfer \u2014 above the spray transition current, metal transfers as fine axial droplets, high quality and deposition rate, but restricted to flat/horizontal positions only and requires minimum material thickness; (4) Pulsed spray \u2014 background current below spray transition + peak pulse current above it, achieves spray transfer quality at lower average heat input, allowing out-of-position use. Red Seal key point: spray transfer cannot be used out-of-position (gravity causes puddle to sag); pulsed spray solves this."
    ),
    57: (
        "Spray transfer requires high voltage (typically 26\u201340V) and high current above the spray transition current to atomize the wire into fine droplets that project axially into the wel",
        "Spray transfer requires voltage typically in the range of 26\u201340V combined with current above the spray transition threshold (which varies by wire diameter and shielding gas \u2014 for 0.9mm wire with Ar/CO\u2082 75/25, roughly 200\u2013250A). Below this transition, metal transfers in globular mode regardless of voltage. The spray transition is lowered (easier to achieve) with higher argon content in the shielding gas \u2014 which is why 100% CO\u2082 cannot achieve true spray transfer (CO\u2082 elevates the transition to beyond practical current levels). Wrong answers: low voltage (14\u201319V) produces short-circuit transfer, not spray; medium voltage (19\u201322V) is the globular range. For Red Seal: if a question shows 100% CO\u2082 + high voltage, the answer is globular \u2014 not spray."
    ),
    104: (
        "In E71T-1: E=electrode, 7=70ksi tensile, 1=all-position, T=tubular (flux-cored), -1=shielding gas and usability designator (CO\u2082 or Ar/CO\u2082, DCEP, fluid slag).",
        "E71T-1 classification: E=electrode; 7=70,000 psi (480 MPa) minimum tensile strength; 1=all-position (the \u20181\u2019 after the T confirms flat/horizontal/vertical-up/overhead capability); T=tubular wire (flux-cored); -1=usability designator specifying CO\u2082 or Ar/CO\u2082 shielding gas, DCEP polarity, and fluid fast-freezing slag. Common exam trap: E71T-11 (no external shielding gas \u2014 self-shielded FCAW) vs E71T-1 (requires external gas \u2014 FCAW-G). Self-shielded FCAW-S cannot be used for most structural work per CSA W59/AWS D1.1 without engineering approval. Wrong answers often confuse the \u20181\u2019 position digit with the flux type, or confuse T (tubular) with S (solid wire in GMAW nomenclature). Always check -G (gas-shielded) vs -S (self-shielded) designator on the wire classification."
    ),
    110: (
        "AWS A2.4 welding symbols communicate the weld type (fillet, groove, etc.), size, length, location (arrow side or other side), and any finishing requirements on engineering drawings",
        "AWS A2.4 welding symbols communicate weld type, size, length, location, and finishing requirements on engineering drawings without written notes. Key elements: the reference line is horizontal \u2014 symbol below the line = arrow side weld; symbol above = other side weld; both sides = weld both sides. The tail contains welding process or specification reference. Common Red Seal exam traps: a flag on the reference line = field weld; a filled circle at the arrow-reference line junction = weld all around; finish symbols (G=grind flush, C=chipping, M=machining) follow the weld size. Wrong answers confuse \u2018arrow side\u2019 with \u2018front of the part\u2019 \u2014 arrow side means the side the arrow touches, regardless of orientation. Symbols are read left-to-right along the reference line; length and pitch follow size."
    ),
}

filepath = Path('276a.html')
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

    old_expl = block[exp_val_start:exp_val_end]

    # Replace explanation value
    abs_start = idx + exp_val_start
    abs_end = idx + exp_val_end
    content = content[:abs_start] + new_expl + content[abs_end:]
    safe_print(f'Q{qid}: enhanced')
    changed += 1

safe_print(f'\nTotal enhanced: {changed}/8')
safe_print(f'File size change: {len(content) - original_len:+d} chars')

filepath.write_text(content, encoding='utf-8')

ids = re.findall(r'\bid:\s*(\d+)', content)
safe_print(f'Total questions: {len(ids)} (should be 120)')
