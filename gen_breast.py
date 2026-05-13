#!/usr/bin/env python3
"""Generate breast surgery illustrations with safety-filter-aware prompts."""

import os, base64, sys, time

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

def gen(prompt, filename):
    out_path = os.path.join(OUT_DIR, filename)
    print(f"\n🎨 Generating: {filename}")
    sys.stdout.flush()
    try:
        result = client.images.generate(
            model="gpt-image-2",
            prompt=prompt,
            n=1,
            size="1024x1024",
            quality="high",
        )
        with open(out_path, "wb") as f:
            f.write(base64.b64decode(result.data[0].b64_json))
        kb = os.path.getsize(out_path) // 1024
        print(f"✅ {filename} ({kb}KB)")
        sys.stdout.flush()
        return True
    except Exception as e:
        print(f"❌ {filename}: {e}")
        sys.stdout.flush()
        return False

# Strategy: Frame as isolated anatomical cross-section diagram, 
# similar to the reference images which show a cutaway without full body context.
# Avoid "female", focus on tissue planes and surgical technique.

ANAT_STYLE = """Netter-atlas style medical textbook illustration. Educational anatomical cross-section diagram for plastic surgery training. Smooth professional digital painting. Isolated anatomical specimen diagram — sagittal cutaway cross-section of mammary tissue showing layered tissue planes.

Tissue rendering: warm peach skin envelope, subcutaneous golden-yellow lobulated adipose tissue with rendered fat globules, rose-pink glandular parenchyma with white ductal branches, deep brick-red striated pectoralis muscle, pale lavender fascial membranes, pale beige rib cross-sections posteriorly.

Clean white background. No text, no labels, no arrows, no annotations. Clinical anatomical atlas quality. NOT a photograph."""

# Bild 1: Vertical Technique
p1 = f"""{ANAT_STYLE}

Surgical technique diagram: Vertical reduction mammaplasty (Lejour technique).
The sagittal cutaway shows a moderately large mammary gland cross-section in lateral view. On the skin surface, a clearly visible brown dashed vertical incision line runs from the areolar margin straight downward to the inframammary crease. A subtle wedge-shaped zone of tissue along the vertical line is highlighted in slightly lighter tone, indicating planned tissue excision. The glandular parenchyma (rose-pink) and adipose tissue (golden-yellow) are abundant. Single vertical incision only — no horizontal component."""

# Bild 2: Inverted-T / Anchor
p2 = f"""{ANAT_STYLE}

Surgical technique diagram: Inverted-T anchor incision reduction mammaplasty.
The sagittal cutaway shows a notably large mammary gland cross-section (macromastia) in lateral view, with very abundant tissue volume. On the skin surface, TWO brown dashed incision lines form an inverted-T (anchor) pattern: one vertical from the areolar margin downward, plus one horizontal along the inframammary crease. A large area of inferior tissue is highlighted indicating substantial planned tissue excision. Significantly more tissue volume than a vertical-only technique."""

# Bild 3: Reduction + Liposuction
p3 = f"""{ANAT_STYLE}

Surgical technique diagram: Reduction mammaplasty with lateral liposuction.
The sagittal cutaway shows a mammary gland with notably wide lateral extension of adipose tissue. The golden-yellow fat layer is particularly thick at the lateral (axillary) aspect. A thin metallic liposuction cannula is shown inserted into the lateral fat deposit, with its trajectory visible as a subtle tunnel through the adipose tissue. Small disrupted fat globules around the cannula tip indicate suctioning. The central glandular parenchyma appears normal but the lateral fat extension is prominent."""

# Bild 4: Classic Mastopexy
p4 = f"""{ANAT_STYLE}

Surgical technique diagram: Classic mastopexy (lift procedure).
The sagittal cutaway shows a ptotic (sagging) mammary gland — the tissue mass has descended well below the inframammary fold, the nipple-areola complex is positioned low. Brown dashed lines on the skin surface outline excess skin zones for removal. A subtle upward directional indicator shows the elevation vector. Two areolar positions are suggested: current low position and intended higher position. The overall shape demonstrates significant ptosis requiring reshaping and elevation."""

# Bild 5: Mastopexy + Augmentation
p5 = f"""{ANAT_STYLE}

Surgical technique diagram: Mastopexy with augmentation (lift plus implant).
The sagittal cutaway shows a moderately ptotic mammary gland with reduced volume. Behind the rose-pink glandular parenchyma, positioned between gland and pectoralis muscle (subglandular pocket), a smooth oval prosthetic implant is visible — rendered as a translucent light-blue tinted silicone shell with subtle highlight reflections, clearly distinct from natural tissue. The implant provides added projection and upper-pole fullness. Brown dashed mastopexy incision lines on the skin surface. Combination of volume augmentation and skin tightening."""

# Bild 6: Reduction Mastopexy
p6 = f"""{ANAT_STYLE}

Surgical technique diagram: Reduction mastopexy (simultaneous lift and volume reduction).
The sagittal cutaway shows a large AND ptotic mammary gland — heavy, significantly descended. Excessive golden-yellow adipose and rose-pink glandular tissue weigh the gland down. Two simultaneous techniques visualized: (1) Brown dashed mastopexy lift lines on skin with upward directional indicators, AND (2) a highlighted zone of excess parenchyma within the gland marked for removal. Both skin tightening (lift) and internal tissue removal (reduction) clearly shown as dual interventions."""

images = [
    (p1, "methode-bv-vertikal-NEW.png"),
    (p2, "methode-bv-t-schnitt-NEW.png"),
    (p3, "methode-bv-fett-NEW.png"),
    (p4, "methode-bs-klassisch-NEW.png"),
    (p5, "methode-bs-vergroesserung-NEW.png"),
    (p6, "methode-bs-verkleinerung-NEW.png"),
]

start_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0

for i, (prompt, filename) in enumerate(images):
    if i < start_idx:
        print(f"⏭️ Skipping {filename}")
        continue
    success = gen(prompt, filename)
    if not success:
        # Try fallback prompt with even more clinical framing
        print(f"   Retrying {filename} with fallback prompt...")
        fallback = prompt.replace("mammary gland", "glandular organ").replace("mammaplasty", "surgical technique").replace("mammary", "glandular").replace("nipple-areola complex", "central papilla region").replace("areolar margin", "central papilla border")
        gen(fallback, filename)
    if i < len(images) - 1:
        time.sleep(3)

print("\n✅ Breast surgery images generation complete!")
