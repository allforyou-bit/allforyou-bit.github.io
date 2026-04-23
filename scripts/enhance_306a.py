"""Enhance explanations for 306A — 4 selected questions."""
from pathlib import Path
import re, sys

def safe_print(text):
    sys.stdout.buffer.write((str(text) + '\n').encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()

ENHANCEMENTS = {
    36: (
        "A hand seamer (seaming pliers) grips and folds the Pittsburgh lock pocket closed over the inserted panel edge, completing the longitudinal seam.",
        "A hand seamer (seaming pliers) is the correct tool for closing a Pittsburgh lock seam in the field: it grips the folded pocket (P-lock groove) and bends it flat onto the inserted panel edge, completing the longitudinal seam securely. Wrong answers: aviation snips cut sheet metal \u2014 they cannot form seams; a pop rivet gun creates mechanical fasteners (not a seam fold); an offset hammer is used to drive and set seams in tight locations but does not grip and fold the lock the way a hand seamer does. For field work, hand seamers are essential because a Pittsburgh machine (power roll former) is shop equipment. Red Seal point: the Pittsburgh machine forms the pocket on the panel edge in the shop; the hand seamer closes it during erection."
    ),
    40: (
        "Tack welds temporarily hold parts in alignment and at correct dimensions before full seam welding, preventing movement and distortion during welding.",
        "Tack welds temporarily hold parts in correct position and alignment before full seam welding, preventing movement and thermally induced distortion as the joint is welded. Wrong answers: tack welds are NOT the final structural welds \u2014 they provide only enough strength to hold position; they should not replace clamps for complex assemblies that require repositioning during fit-up (clamps are removed and repositioned, tacks are not). Tack weld quality matters: a tack that cracks during welding can become a defect in the root of the final weld. Good practice: tack at both ends first to hold square, then space intermediate tacks to control distortion. In sheet metal duct welding, tack spacing typically 150\u2013300mm for light gauge."
    ),
    46: (
        "The gas cylinder pictogram (silhouette of a cylinder) identifies gases under pressure \u2014 compressed, liquefied, or dissolved gases \u2014 per WHMIS 2015 / GHS.",
        "The gas cylinder pictogram (black cylinder silhouette on white background) identifies substances that are gases under pressure \u2014 compressed gases (argon, oxygen), liquefied gases (propane, CO\u2082), refrigerated liquefied gases (LNG), or dissolved gases (acetylene). Wrong answers: the flame-over-circle pictogram indicates an oxidizer (not a compressed gas); the exclamation mark indicates acute toxicity, skin/eye irritation, or other moderate hazards; the skull and crossbones indicates acute lethal toxicity. Red Seal sheet metal workers encounter this pictogram on argon shielding gas cylinders, compressed air cylinders, and refrigerant containers. WHMIS 2015 is aligned with the UN Globally Harmonized System (GHS) \u2014 the same pictograms are used internationally, which is why they differ from old WHMIS 1988 symbols."
    ),
    62: (
        "A minimum 6mm (1/4\") lap is required for soldered joints to develop adequate capillary solder flow and joint strength.",
        "A minimum 6mm (1/4\u201d) lap is required for soldered sheet metal joints to allow adequate capillary solder flow and develop sufficient joint strength. Capillary action draws molten solder into the joint gap (typically 0.05\u20130.15mm clearance) \u2014 too small a lap leaves insufficient bond area; too large a lap does not improve strength but wastes solder and time. Wrong answers: one sheet thickness is inadequate for most soldered joints; 25mm (1\u201d) is unnecessarily large for standard sheet metal seams. The correct joint clearance for capillary soldering is different from the lap length \u2014 a tight fit (clearance 0.05\u20130.15mm) promotes capillary flow while a loose fit (>0.5mm) results in a cold, porous joint. Solder must be applied to the base metal (not the iron tip) once the seam reaches soldering temperature."
    ),
}

filepath = Path('306a.html')
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
safe_print(f'Total questions: {len(ids)} (should be 100)')
