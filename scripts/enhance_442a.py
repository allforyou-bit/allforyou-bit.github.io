"""Enhance explanations for 442A Q37, Q54, Q55, Q61, Q62, Q40, Q52, Q28."""
from pathlib import Path
import re, sys

def safe_print(text):
    sys.stdout.buffer.write((str(text) + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()

# Each entry: (question_id, old_expl_substring_unique, new_full_explanation)
# We match by finding 'id:N,' then searching for the explanation field in that block.

ENHANCEMENTS = {
    28: (
        "Screw-pin shackles can be easily assembled and disassembled, making them suitable for temporary or frequently changed rigging setups.",
        "Screw-pin shackles can be assembled and disassembled quickly without tools, making them the correct choice for temporary or frequently changed rigging configurations. The other options are incorrect: screw-pin shackles should NOT be used in applications where the pin can rotate or unscrew under load (such as running rigging or slings that rotate) — bolt-type (cotter-pin) shackles are required there. Screw-pin shackles are not rated higher than bolt-type shackles of the same size; they are simply easier to open and close. For permanent installations or overhead lifts with load movement, always use bolt-type shackles with cotter pins."
    ),
    37: (
        "WLL = Breaking Strength \u00f7 Safety Factor = 50,000 \u00f7 5 = 10,000 kg.",
        "WLL = Breaking Strength \u00f7 Safety Factor = 50,000 \u00f7 5 = 10,000 kg. The 5:1 safety factor (design factor) is the minimum required by Canadian OH&S regulations and ASME B30 standards for rigging hardware, and it accounts for dynamic loading, shock loading, fatigue, wear, and inspection intervals. Common wrong answers: using 4:1 (which is the factor for some overhead hoisting equipment under specific standards, not general rigging) or 3:1 (which is far too low and not acceptable for any rigging hardware under Canadian codes). Always verify WLL on the component\u2019s tag \u2014 never calculate from breaking strength alone without confirming the applicable standard."
    ),
    40: (
        "CSA W47.1 governs the certification of fusion welding companies (fabricators and contractors) to ensure they have qualified personnel, procedures, and quality control systems for s",
        "CSA W47.1 (Certification of Companies for Fusion Welding of Steel) governs the certification of welding companies \u2014 it certifies the company, not individual welders. Certified companies must have qualified welding supervisors, approved welding procedures (WPSs), and a documented quality control system. This is different from: CSA W59 (which governs the design and fabrication requirements for welded steel structures), CSA W178.2 (which certifies individual welding inspectors), and AWS D1.1 (the American Structural Welding Code used as a reference). On a Canadian structural steel project, the fabricator or erector must hold a current CSA W47.1 certification \u2014 this is a mandatory contract requirement."
    ),
    52: (
        "CSA W59 (Welded Steel Construction) specifies the design, fabrication, and erection requirements for welded structural steel, including joint design, workmanship, and inspection cr",
        "CSA W59 (Welded Steel Construction \u2014 Metal Arc Welding) specifies design, fabrication, and erection requirements for welded steel structures in Canada, including joint design, acceptable workmanship, and inspection criteria. It is often confused with: CSA W47.1 (which certifies welding companies \u2014 not design requirements), CSA W59 is the structural welding CODE (what must be built and to what standard), while W47.1 is the company CERTIFICATION standard (who is allowed to build it). AWS D1.1 is the equivalent American standard; many Canadian projects reference both. For Red Seal ironworker exam: know that W59 = fabrication and design standard; W47.1 = company certification; W178.2 = inspector certification."
    ),
    54: (
        "Column grid lines are a system of reference lines (typically numbered in one direction, lettered in the other) that establish the layout of the structural framing plan.",
        "Column grid lines are intersecting reference lines (typically numbered 1, 2, 3\u2026 in one direction and lettered A, B, C\u2026 in the other) that establish the planned column locations on a structural drawing. They are NOT column centre-lines in the sense of indicating column size or section \u2014 they are location references only. Grid line intersections identify each column by coordinates (e.g., Column B-3). This is different from dimension lines (which show actual measurements between members) and elevation marks (which show height). All trades on a project use the same grid reference to coordinate work \u2014 so an ironworker, concrete crew, and mechanical contractor all reference Column B-3 the same way."
    ),
    55: (
        "EL. (elevation) followed by a number indicates the height of a point above the project datum (typically the finished first floor elevation at 0.000).",
        "EL. (Elevation) followed by a number (e.g., EL. 12500) indicates the height in millimetres above the project datum \u2014 typically the finished first floor (FF) established at EL. 0.000. Elevations above datum are positive; below datum are negative. This is different from: a grid coordinate (which locates a point in plan, not in height), a dimension (which measures distance between two specific points), or a TOS/BOS notation (which is a specific elevation of the top or bottom of a steel member). When setting anchor bolts or erecting columns, always verify the elevation against the structural drawings \u2014 not the architectural drawings, which may use a different datum."
    ),
    61: (
        "TOS (Top of Steel) is a common elevation notation on structural drawings indicating the elevation of the top surface of the steel beam, used to coordinate with concrete deck elevat",
        "TOS (Top of Steel) is an elevation reference on structural drawings indicating the height of the top flange of a beam, measured from the project datum. It is used to coordinate with the concrete deck, mechanical, and architectural drawings. Common related notations: BOS (Bottom of Steel \u2014 soffit elevation, important for clearance), TOS is NOT the same as finished floor elevation (which is TOS + deck slab thickness + topping if any). Wrong answers often confuse TOS with the beam depth or with the centreline elevation. For steel erection: when setting beam elevation, you level to the TOS \u2014 not to the bottom flange or web centreline."
    ),
    62: (
        "FSBW (Full Strength Butt Weld) or FPBW (Full Penetration Butt Weld) indicates a complete joint penetration (CJP) groove weld that develops the full strength of the connected member",
        "FSBW (Full Strength Butt Weld) or CJP (Complete Joint Penetration) groove weld indicates that the weld must develop the full tensile strength of the connected base metal \u2014 the weld is not the weak link. This requires 100% penetration through the joint thickness, usually verified by visual inspection plus UT (ultrasonic testing) or radiography. It is different from: a partial joint penetration (PJP) weld, which does not penetrate the full thickness and has reduced capacity; a fillet weld, which joins members at a surface (no groove); and a plug or slot weld. FSBW/CJP welds are required at moment connections (beam-column moment joints) and splice plates carrying tension \u2014 they cost more (more prep, more passes, more inspection) than fillet welds."
    ),
}

filepath = Path('442a.html')
content = filepath.read_text(encoding='utf-8')
original_len = len(content)

changed = 0
for qid, (old_snippet, new_expl) in ENHANCEMENTS.items():
    # Find the block for this question id
    id_pattern = f'id:{qid},'
    idx = content.find(id_pattern)
    if idx == -1:
        safe_print(f'Q{qid}: id pattern not found, skipping')
        continue

    # Find the explanation field in this block
    # Search from idx to next question boundary
    next_q = content.find(',{id:', idx + 1)
    if next_q == -1:
        next_q = idx + 5000
    block = content[idx:next_q]

    # Find explanation value in block
    exp_start = block.find("explanation:'")
    if exp_start == -1:
        safe_print(f'Q{qid}: explanation field not found, skipping')
        continue

    exp_val_start = exp_start + len("explanation:'")
    # Find closing quote (handle escaped quotes)
    exp_val_end = exp_val_start
    while exp_val_end < len(block):
        ch = block[exp_val_end]
        if ch == "'" and block[exp_val_end-1] != '\\':
            break
        exp_val_end += 1

    old_expl = block[exp_val_start:exp_val_end]

    # Verify old snippet is in old_expl
    if old_snippet[:50] not in old_expl and old_snippet[:50].replace('\u2014', '--') not in old_expl:
        # Try plain ASCII
        safe_print(f'Q{qid}: old snippet not matched (first 50: {repr(old_snippet[:50])})')
        safe_print(f'       found: {repr(old_expl[:80])}')
        continue

    # Replace in content
    old_full = f"explanation:'{old_expl}'"
    new_full = f"explanation:'{new_expl}'"
    if old_full not in content[idx:next_q]:
        # Try to replace using idx-relative positions
        abs_exp_start = idx + exp_start
        abs_exp_val_start = idx + exp_val_start
        abs_exp_val_end = idx + exp_val_end
        content = content[:abs_exp_val_start] + new_expl + content[abs_exp_val_end:]
        safe_print(f'Q{qid}: enhanced (positional replace)')
    else:
        content = content[:idx] + content[idx:next_q].replace(old_full, new_full, 1) + content[next_q:]
        safe_print(f'Q{qid}: enhanced (string replace)')
    changed += 1

safe_print(f'\nTotal enhanced: {changed}/8')
safe_print(f'File size change: {len(content) - original_len:+d} chars')

filepath.write_text(content, encoding='utf-8')

# Verify question count unchanged
ids = re.findall(r'\bid:\s*(\d+)', content)
safe_print(f'Total questions: {len(ids)} (should be 120)')
