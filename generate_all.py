#!/usr/bin/env python3
"""Generate 9 medical illustrations for Villa Bella landing pages."""

import os, base64, sys, time

# Load env
env_path = os.path.expanduser("~/.openclaw/workspace/.env")
with open(env_path) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ[k.strip()] = v.strip()

from openai import OpenAI
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

OUT_DIR = "/Users/nexus/.openclaw/workspace/projects/villa-bella-bruststraffung/images"

def generate_image(prompt, filename, size="1024x1024", retries=2):
    out_path = os.path.join(OUT_DIR, filename)
    for attempt in range(retries + 1):
        try:
            print(f"\n{'='*60}")
            print(f"🎨 Generating: {filename} (attempt {attempt+1})")
            print(f"{'='*60}")
            result = client.images.generate(
                model="gpt-image-2",
                prompt=prompt,
                n=1,
                size=size,
                quality="high",
            )
            img_data = base64.b64decode(result.data[0].b64_json)
            with open(out_path, "wb") as f:
                f.write(img_data)
            kb = os.path.getsize(out_path) // 1024
            print(f"✅ {filename} ({kb}KB)")
            return out_path
        except Exception as e:
            print(f"❌ Error on {filename} (attempt {attempt+1}): {e}")
            if attempt < retries:
                print("   Retrying in 5s...")
                time.sleep(5)
            else:
                print(f"   FAILED after {retries+1} attempts")
                return None

# ============================================================
# STYLE PREAMBLE (shared across all breast images)
# ============================================================
BREAST_STYLE = """Professional digital medical illustration in Netter-atlas surgical textbook style. Smooth digital painting with precise anatomical detail. Lateral sagittal cutaway view of female breast anatomy. Clean anatomical dissection window with smooth skin border revealing layered tissue planes. Educational anatomical drawing for clinical reference.

Internal anatomy color key: warm peach-toned smooth skin envelope, subcutaneous golden-yellow lobulated adipose tissue with individually rendered fat globules, rose-pink mammary glandular lobules with white branching ductal tree converging at nipple, deep brick-red pectoralis major muscle with visible fiber striations, pale lavender-white fascial membrane planes between layers, posterior pale beige oval rib cross-sections with cortical rim.

Clean white background (#FFFFFF), no text, no labels, no annotations, no arrows. Warm soft lighting from upper-left. High resolution clinical illustration."""

FACE_STYLE = """Professional digital medical illustration in Netter-atlas surgical textbook style. Smooth digital painting with precise anatomical detail. Lateral view of human face and head showing surgical anatomy. Educational anatomical drawing for clinical facial surgery reference.

Tissue color key: warm peach-toned smooth skin, golden-yellow subcutaneous fat lobules, the SMAS layer shown as a distinct orange-tinged fibromuscular sheet, deeper facial muscles in brick-red with fiber striations, pale beige bone structures, pale lavender-white fascial planes.

Clean white background (#FFFFFF), no text, no labels, no annotations. Warm soft lighting from upper-left. High resolution clinical illustration."""

# ============================================================
# BRUSTVERKLEINERUNG (3 Bilder)
# ============================================================

prompts = {}

# Bild 1: Vertikale Technik
prompts["methode-bv-vertikal-NEW.png"] = f"""{BREAST_STYLE}

SPECIFIC TECHNIQUE — Vertical breast reduction (Lejour technique):
The breast is moderately large. On the skin surface, a clearly visible brown dashed incision line runs vertically from the lower edge of the areola straight downward to the inframammary fold — this is the vertical incision marking. The cutaway window reveals the breast tissue beneath: abundant golden-yellow fat and rose-pink glandular tissue. A wedge-shaped zone of tissue along the vertical incision path is subtly highlighted with a slightly different tone (lighter or semi-transparent overlay) indicating the tissue to be removed. The breast shape suggests pre-operative state — full but with excess tissue inferiorly. Only ONE incision line — vertical only, no horizontal component."""

# Bild 2: T-Schnitt (Anker)
prompts["methode-bv-t-schnitt-NEW.png"] = f"""{BREAST_STYLE}

SPECIFIC TECHNIQUE — Inverted-T anchor incision breast reduction:
The breast is notably large (macromastia) with significant volume and ptosis. On the skin surface, TWO clearly visible brown dashed incision lines form an inverted T-shape (anchor pattern): one line runs vertically from the areola downward, and a second horizontal line runs along the inframammary fold crease — together forming an upside-down T or anchor shape. The cutaway window reveals very abundant breast tissue — large amounts of golden-yellow fat and rose-pink glandular tissue. A substantial portion of inferior and central tissue is subtly highlighted indicating the large volume of tissue to be removed. The breast is significantly larger than in the vertical technique illustration."""

# Bild 3: Fettabsaugung
prompts["methode-bv-fett-NEW.png"] = f"""{BREAST_STYLE}

SPECIFIC TECHNIQUE — Breast reduction with lateral liposuction:
The breast has a notably wide base extending far laterally along the chest wall. The cutaway emphasizes the fat layer: particularly thick golden-yellow adipose tissue concentrated at the lateral (side/axillary) aspect of the breast. A thin metallic liposuction cannula is shown inserted into the lateral fat deposit, with its trajectory path visible as a subtle tunnel through the yellow fat tissue. Small disrupted fat globules around the cannula tip show the suctioning action. The medial breast tissue (glandular and fat) appears normal, but the lateral extension of fat is prominent — this is what the liposuction targets for improved contour."""

# ============================================================
# BRUSTSTRAFFUNG (3 Bilder)
# ============================================================

# Bild 4: Klassische Straffung
prompts["methode-bs-klassisch-NEW.png"] = f"""{BREAST_STYLE}

SPECIFIC TECHNIQUE — Classic mastopexy (breast lift):
The breast shows significant ptosis (sagging) — the nipple-areola complex has descended well below the inframammary fold, and the breast tissue hangs low. The cutaway reveals that the glandular tissue mass has slumped downward within the skin envelope. On the skin surface, brown dashed lines indicate the surgical plan: excess skin zones above and below the areola are outlined for removal. A subtle upward-pointing arrow or directional indicator shows the lifting vector — tissue will be elevated superiorly. Two positions of the areola are suggested: current low position and intended higher position. The overall impression is of a breast that needs significant reshaping and elevation."""

# Bild 5: Straffung + Vergrößerung
prompts["methode-bs-vergroesserung-NEW.png"] = f"""{BREAST_STYLE}

SPECIFIC TECHNIQUE — Mastopexy with augmentation (breast lift + implant):
The breast shows moderate ptosis with deflated volume. The cutaway reveals normal but somewhat sparse breast tissue. BEHIND the rose-pink glandular tissue, positioned between the gland and the brick-red pectoralis muscle (subglandular pocket), a smooth oval breast implant is visible — rendered as a translucent light blue-tinted silicone shell with subtle highlight reflections, clearly distinguishable from natural tissue. The implant adds projection and upper-pole fullness. On the skin surface, brown dashed mastopexy incision lines are visible (periareolar and vertical). The combination of implant volume plus skin tightening creates the augmentation-lift result."""

# Bild 6: Straffung + Verkleinerung
prompts["methode-bs-verkleinerung-NEW.png"] = f"""{BREAST_STYLE}

SPECIFIC TECHNIQUE — Reduction mastopexy (simultaneous lift and reduction):
The breast is large AND ptotic (heavy, sagging significantly). The cutaway reveals excessive amounts of both golden-yellow fat and rose-pink glandular tissue weighing the breast down. This illustration combines TWO techniques visible simultaneously: (1) Brown dashed mastopexy lift lines on the skin with upward directional indicators showing elevation, AND (2) a highlighted zone of excess tissue within the breast interior marked for removal/reduction. The breast appears heavy enough to cause back and neck strain. Both the skin tightening (lift) and internal tissue removal (reduction) are clearly shown as dual interventions in one procedure."""

# ============================================================
# FACELIFT (3 Bilder)
# ============================================================

# Bild 7: Mini-Facelift
prompts["methode-fl-mini-NEW.png"] = f"""{FACE_STYLE}

SPECIFIC TECHNIQUE — Mini-facelift:
Lateral view of a mature face (showing early signs of aging: mild jowling, slight cheek laxity). A small anatomical cutaway window is located just behind and below the ear, revealing the layered facial tissue planes: skin, thin subcutaneous fat, and the edge of the SMAS layer. TWO small brown dashed incision lines are marked behind the ear — short and minimal. The cutaway is deliberately SMALL to emphasize the minimally invasive nature. Only the superficial layers near the ear are exposed. The face is shown from ear to chin, with natural skin tone. The overall impression is a subtle, limited procedure with small incisions."""

# Bild 8: SMAS-Facelift
prompts["methode-fl-smas-NEW.png"] = f"""{FACE_STYLE}

SPECIFIC TECHNIQUE — SMAS facelift (dual-plane technique):
Lateral view of a mature face showing moderate aging (visible jowls, nasolabial folds, cheek descent). A LARGER anatomical cutaway window extends from in front of the ear across the cheek, revealing the key surgical planes. The SMAS layer (Superficial Musculo-Aponeurotic System) is prominently highlighted as a distinct orange-tinged fibromuscular sheet — clearly shown as a SEPARATE layer between the subcutaneous fat above and the deeper facial muscles below. Subtle directional tension lines or vectors on the SMAS layer indicate the superior-posterior lifting direction. The two distinct planes being tightened are clearly visible: skin layer and SMAS layer moving independently. Brown dashed incision lines extend from the temple, around the ear, and behind. More extensive than mini-facelift."""

# Bild 9: Deep Plane Facelift
prompts["methode-fl-deep-NEW.png"] = f"""{FACE_STYLE}

SPECIFIC TECHNIQUE — Deep plane facelift:
Lateral view of a mature face showing pronounced aging (significant jowling, deep nasolabial folds, marked cheek and neck laxity). The LARGEST anatomical cutaway window extends broadly across the cheek and jawline. The dissection plane goes BENEATH the SMAS layer — the deep plane is highlighted as the surgical level of tissue mobilization. The illustration clearly shows: skin and fat above, then the SMAS layer, then BELOW the SMAS the deep plane of dissection is marked with a distinct color or emphasis (the plane between SMAS and deeper parotid-masseteric fascia). More tissue is being mobilized en-bloc compared to the SMAS facelift. The SMAS + overlying fat move as one composite flap. Directional vectors show the deep tissue being lifted superiorly and posteriorly. This is the most extensive procedure — the deepest dissection, largest exposure, maximum rejuvenation."""

# ============================================================
# GENERATE ALL
# ============================================================

if __name__ == "__main__":
    start_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    items = list(prompts.items())
    
    results = {}
    for i, (filename, prompt) in enumerate(items):
        if i < start_idx:
            print(f"⏭️  Skipping {filename} (index {i})")
            continue
        path = generate_image(prompt, filename)
        results[filename] = "✅" if path else "❌"
        if i < len(items) - 1:
            time.sleep(2)  # Small delay between calls
    
    print(f"\n{'='*60}")
    print("📊 RESULTS SUMMARY")
    print(f"{'='*60}")
    for fn, status in results.items():
        print(f"  {status} {fn}")
    print(f"\nTotal: {sum(1 for s in results.values() if s == '✅')}/{len(results)} successful")
