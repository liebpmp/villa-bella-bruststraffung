#!/usr/bin/env python3
"""Generate facelift illustrations (should pass safety filter)."""

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
        return True
    except Exception as e:
        print(f"❌ {filename}: {e}")
        return False

FACE_STYLE = "Professional digital medical illustration in Netter-atlas surgical textbook style for facial surgery education. Smooth digital painting with precise anatomical detail. Clean white background. No text, no labels, no annotations. Warm soft lighting. High resolution clinical illustration. NOT a photograph."

# ============================================================
# FACELIFT (3 Bilder)
# ============================================================

# Bild 7: Mini-Facelift
p7 = f"""{FACE_STYLE}

Lateral profile view of a mature face and neck showing mini-facelift surgical anatomy. The face shows early signs of aging with mild jowling and slight cheek laxity. 

A small anatomical cutaway window is located just behind and below the ear, revealing the layered facial tissue planes: warm peach skin layer, thin golden-yellow subcutaneous fat, and the superficial edge of the SMAS fascial sheet.

Two small brown dashed incision lines are marked in the skin behind the ear — short and minimal, emphasizing the minimally invasive nature of this procedure. The cutaway window is deliberately small. Only superficial layers near the ear are exposed.

Tissue colors: warm peach skin, golden-yellow fat lobules, SMAS as a thin orange-tinged fibromuscular layer, deeper facial muscles in brick-red. Educational anatomical atlas quality."""

# Bild 8: SMAS-Facelift
p8 = f"""{FACE_STYLE}

Lateral profile view of a mature face showing SMAS facelift (dual-plane rhytidectomy) surgical anatomy. The face shows moderate aging with visible jowls, nasolabial folds, and cheek descent.

A larger anatomical cutaway window extends from in front of the ear across the mid-cheek, revealing the key surgical tissue planes in clear layers:
1. Outermost: warm peach skin
2. Golden-yellow subcutaneous fat layer  
3. The SMAS layer (Superficial Musculo-Aponeurotic System) prominently highlighted as a distinct ORANGE-tinged fibromuscular sheet — clearly shown as a SEPARATE layer
4. Deeper brick-red facial muscles beneath

Subtle directional arrows on the SMAS layer indicate the superior-posterior (upward and backward) lifting vector. The two planes being independently tightened (skin and SMAS) are clearly visible.

Brown dashed incision lines extend from the temple area, around the ear, and behind it — more extensive than a mini procedure."""

# Bild 9: Deep Plane Facelift
p9 = f"""{FACE_STYLE}

Lateral profile view of a mature face showing deep plane facelift surgical anatomy. The face shows pronounced aging with significant jowling, deep nasolabial folds, and marked cheek and neck laxity.

The LARGEST anatomical cutaway window extends broadly across the cheek and jawline, revealing the deepest surgical dissection:
1. Outermost: warm peach skin
2. Golden-yellow subcutaneous fat
3. The SMAS layer shown as orange-tinged fibromuscular sheet
4. BELOW the SMAS: the deep plane of dissection is highlighted with a distinct deeper color emphasis — this is the plane between the SMAS and the deeper parotid-masseteric fascia
5. Deepest: brick-red facial muscles and pale beige bone

The key visual: tissue BENEATH the SMAS is being mobilized as a composite flap (SMAS + fat moving together). Large directional arrows show the deep tissue being lifted superiorly and posteriorly. This is the most extensive procedure — deepest dissection, largest cutaway exposure, maximum tissue mobilization visible."""

images = [
    (p7, "methode-fl-mini-NEW.png"),
    (p8, "methode-fl-smas-NEW.png"),
    (p9, "methode-fl-deep-NEW.png"),
]

for prompt, filename in images:
    gen(prompt, filename)
    time.sleep(3)

print("\n✅ Facelift images done!")
