# Villa Bella — Methoden-Karten Bildgenerierung Brief

## Tool & Settings
- **Model:** `gpt-image-2` via OpenAI Images API
- **Size:** `1024x1024`
- **Quality:** `high`
- **Output:** Base64 PNG

## Referenz-Stil (Gynäkomastie — 3 existierende Bilder)
Die 3 Gynäkomastie-Bilder (`methode-fett.png`, `methode-druese.png`, `methode-kombi.png`) definieren den Stil:
- **Art:** Professionelle digitale medizinische Illustration, Netter-Atlas Stil
- **Ansicht:** Lateral sagittal cutaway (Seitenansicht mit Anatomie-Fenster)
- **Rendering:** Smooth digital painting mit präzisem anatomischem Detail
- **KEINE Fotos, kein 3D-Render, kein Cartoon, keine Skizze**

## Farbpalette (EXAKT einhalten!)
| Gewebe | Farbbeschreibung für Prompt |
|--------|----------------------------|
| Haut | warm peach-toned smooth skin |
| Fettgewebe | golden-yellow lobulated adipose tissue with individually rendered fat globules |
| Drüsengewebe | rose-pink mammary glandular lobules with white branching ductal tree |
| Muskel | brick-red pectoralis major muscle with visible fiber striations |
| Knochen/Rippen | pale beige oval rib cross-sections with cortical rim |
| Faszien | translucent pale lavender-white fascial membrane layers |
| Duktales System | white arborizing ductal branches converging at nipple |

## Komposition
- Laterale Sagittal-Ansicht (Seitenansicht)
- Clean anatomical cutaway window mit sauberer Hautkante
- Schichten in korrekter Tiefenreihenfolge: Haut → Fett → Drüsen → Muskel → Rippen
- Reiner weißer Hintergrund (#FFFFFF)
- KEIN Text, keine Labels, keine Annotationen, keine Pfeile
- Weiche Beleuchtung von oben-links

## Master-Prompt-Template
```
Professional digital medical illustration, lateral sagittal cutaway view of female chest showing breast anatomy cross-section. Anatomical dissection window with clean skin border revealing layered tissue planes in sequential depth.

[TECHNIQUE-SPECIFIC DESCRIPTION HERE]

Internal anatomy visible: warm peach skin envelope, subcutaneous golden-yellow lobulated adipose tissue with individually rendered fat globules, [technique-specific tissue details], deep brick-red pectoralis major muscle with visible fiber striations, pale lavender-white fascial planes between layers, posterior beige oval rib cross-sections with cortical rim.

Clean white background, no text, no labels, no annotations. Netter-atlas style, surgical textbook-quality medical illustration, smooth digital painting with precise anatomical detail, warm anatomical color palette, clearly delineated tissue planes, high resolution.
```

## ⚠️ Safety Filter Hinweise
- "female chest" + "breast" als medizinische Illustration/Zeichnung funktioniert (V4 ging durch)
- Falls Safety-Filter blockt: "educational anatomical drawing" betonen, "clinical", "textbook"
- NICHT "photograph" oder "photo" verwenden

---

## AUFGABE: 9 Bilder generieren (3 Seiten × 3 Methoden)

### Seite 1: BRUSTVERKLEINERUNG (3 Bilder)

**Bild 1: `methode-bv-vertikal-NEW.png` — Vertikale Technik**
Kontext aus LP: "Schnitt von der Brustwarze senkrecht nach unten. Für moderate Verkleinerungen mit minimaler Narbenbildung. Die Brust wird gleichzeitig angehoben und neu geformt."
→ Zeigen: Weibliche Brust von der Seite, cutaway zeigt innere Anatomie. Eine sichtbare vertikale gestrichelte Schnittlinie von der Areola/Brustwarze senkrecht nach unten auf der Hautoberfläche. Das zu entfernende Gewebe sollte subtil markiert/hervorgehoben sein. Die Brust erscheint moderat groß (vor der Reduktion).

**Bild 2: `methode-bv-t-schnitt-NEW.png` — Invertiertes T (Anker-Schnitt)**
Kontext aus LP: "Vertikaler Schnitt plus Schnitt in der Unterbrustfalte. Für deutlich übergroße Brüste (Makromastie) mit maximaler Gewebereduktion."
→ Zeigen: Weibliche Brust, deutlich größer als beim vertikalen Bild. Cutaway zeigt viel Gewebe. ZWEI gestrichelte Schnittlinien: eine vertikal von der Brustwarze nach unten UND eine horizontal in der Unterbrustfalte (zusammen = umgekehrtes T / Anker-Form). Größerer markierter Bereich für Gewebeentfernung.

**Bild 3: `methode-bv-fett-NEW.png` — Verkleinerung + Fettabsaugung**
Kontext aus LP: "Bei breitem Brustansatz kann eine seitliche Fettabsaugung das Ergebnis perfektionieren. Besonders geeignet für eine natürliche Kontur und optimale Proportionen."
→ Zeigen: Weibliche Brust mit breiterem Ansatz. Cutaway betont das Fettgewebe (golden-yellow) besonders an den Seiten/lateral. Eine feine Kanüle oder deren Pfad durch das seitliche Fettgewebe angedeutet. Fokus auf die seitliche/laterale Fettverteilung.

### Seite 2: BRUSTSTRAFFUNG (3 Bilder)

**Bild 4: `methode-bs-klassisch-NEW.png` — Klassische Bruststraffung**
Kontext aus LP: "Bewährte Mastopexie: Überschüssige Haut wird entfernt, das Brustgewebe angehoben, die Brustwarze in die ideale Position gebracht. Für deutlich erschlaffte Brüste."
→ Zeigen: Weibliche Brust die deutlich erschlafft/hängend dargestellt ist (Ptosis). Cutaway zeigt das Brustgewebe das nach unten gesunken ist. Gestrichelte Linien zeigen wo Haut entfernt wird (oben und unten). Ein Pfeil oder Andeutung der Anhebungsrichtung nach oben. Die Brustwarze-Position ist markiert (alte Position tief, neue Position höher).

**Bild 5: `methode-bs-vergroesserung-NEW.png` — Straffung + Vergrößerung**
Kontext aus LP: "Bruststraffung kombiniert mit einem Implantat oder Eigenfett-Transfer. Für Frauen, die neben der Straffung auch mehr Volumen wünschen."
→ Zeigen: Weibliche Brust im cutaway. Hinter dem Brustgewebe (zwischen Drüse und Muskel oder unter dem Muskel) ist ein Implantat als glatte ovale Form angedeutet (leicht hellblau/transparent oder silhouettenhaft). Das Implantat fügt Volumen hinzu. Straffungslinien auf der Haut wie bei klassischer Straffung.

**Bild 6: `methode-bs-verkleinerung-NEW.png` — Straffung + Verkleinerung**
Kontext aus LP: "Reduktionsmastopexie: Gleichzeitige Verkleinerung und Straffung. Besonders entlastend bei Rücken- und Nackenbeschwerden durch zu große Brüste."
→ Zeigen: Weibliche Brust, groß und hängend. Cutaway zeigt viel Gewebe. Kombination aus: Straffungslinien (Anhebung) UND markierter Bereich für Gewebeentfernung (Reduktion). Doppelte Technik in einem Bild visualisiert.

### Seite 3: FACELIFT (3 Bilder)

**Bild 7: `methode-fl-mini-NEW.png` — Mini-Facelift**
Kontext aus LP: "Zwei kleine Schnitte hinter den Ohren. Ideal bei ersten Alterserscheinungen: leichte Hängebäckchen, beginnende Wangenerschlaffung. Weniger invasiv, schnellere Heilung."
→ Zeigen: Seitliche Ansicht eines Gesichts/Kopfes als medizinische Illustration. Cutaway hinter dem Ohr zeigt die Gewebeschichten: Haut, subkutanes Fett, SMAS-Schicht, tiefere Muskulatur. Zwei kleine gestrichelte Schnittlinien hinter dem Ohr markiert. Dezent — weniger invasiv als die anderen Methoden.

**Bild 8: `methode-fl-smas-NEW.png` — SMAS-Facelift**
Kontext aus LP: "Zwei-Schichten-Technik: Haut und darunterliegendes Muskel-Bindegewebe (SMAS) werden gestrafft. Das natürlichste und langanhaltendste Ergebnis."
→ Zeigen: Seitliche Gesichtsansicht mit größerem Cutaway. Die SMAS-Schicht (Superficial Musculo Aponeurotic System) ist klar als separate Schicht zwischen Fett und tieferer Muskulatur hervorgehoben (in einer eigenen Farbe, z.B. orange oder tieferes rosa). Pfeile oder Spannungslinien zeigen die Straffungsrichtung der SMAS-Schicht nach oben/posterior. Größerer Schnittbereich als Mini.

**Bild 9: `methode-fl-deep-NEW.png` — Deep Plane Facelift**
Kontext aus LP: "Noch tiefere Gewebeschichten werden mobilisiert als beim SMAS. Für besonders ausgeprägte Erschlaffung. Maximale Verjüngung bei natürlichem Ergebnis."
→ Zeigen: Seitliche Gesichtsansicht mit dem tiefsten/größten Cutaway. Wie SMAS, aber die Präparationsebene geht UNTER die SMAS-Schicht — die tiefere Ebene (deep plane) ist hervorgehoben. Mehr Gewebemobilisation sichtbar. Die Illustration zeigt dass hier tiefer gearbeitet wird als beim SMAS.

## Output
- Alle 9 Bilder als PNG in `/Users/nexus/.openclaw/workspace/projects/villa-bella-bruststraffung/images/`
- Dateinamen wie oben angegeben (`methode-XX-NEW.png`)
- Nach Fertigstellung: kurze Zusammenfassung welche Bilder erstellt wurden + welche Prompts funktioniert haben (für Style Guide)
