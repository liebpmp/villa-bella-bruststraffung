# CLAUDE.md — Villa Bella Gynäkomastie LP V3

## Projekt
Single-file HTML Landing Page für Gynäkomastie-Korrektur bei Villa Bella München.
- **Datei:** `gynaekomastie.html` (928 LOC, single-file mit eingebettetem CSS/JS)
- **Backup V2.1:** `versions/gynaekomastie-v2.1-pre-v3.html`
- **Bilder:** `images/` Ordner (lokale Assets)
- **Feedback-Dokument:** `luis-v3-feedback.txt` (VOLLSTÄNDIG lesen!)

## ⚠️ KRITISCHE REGELN
1. **NUR die im Feedback genannten Änderungen umsetzen!** Rest der Seite EXAKT so lassen.
2. **Kein Layout-Redesign** — Farben, Schriften, Button-Stil, Premium-Design beibehalten
3. **Medizinisch vorsichtig formulieren** — "in vielen Fällen", "je nach Befund", "im Regelfall", keine Heilversprechen
4. **Responsive MUSS stark sein** — Desktop UND Mobile testen
5. **Single-file bleiben** — alles in einer HTML-Datei (CSS + JS embedded)

## Aufgabe: V3 Feedback einarbeiten

Lies `luis-v3-feedback.txt` VOLLSTÄNDIG. Starte ab dem Abschnitt **"Ab hier neues Feedback für V3 Desktop"** (ca. Mitte des Dokuments). Alles DAVOR wurde bereits in V2/V2.1 eingearbeitet.

### Die V3-Änderungen im Überblick:

#### 1. Hero/Header komplett überarbeiten
- **Eyebrow:** "GYNÄKOMASTIE-KORREKTUR IN MÜNCHEN" → "DISKRET. MÄNNLICH. INDIVIDUELL."
- **H1 bleibt:** "Gynäkomastie-Korrektur in München: Für einen flachen, maskulinen Oberkörper"
- **Neuer Introtext:** "Schluss mit dem Verstecken der eigenen Brust..."
- **Neue 3 Bullet Points** (Hunderte zufriedene Männer, 30+ Jahre, wieder selbstbewusst)
- **Neue Trust-Zeile:** "Termin online in 2 Minuten buchen · Rückmeldung innerhalb von 24h · 100% vertraulich"
- **Trust-Badges** (Jameda/Google/Doctify) von links unten → RECHTS unter das Video verschieben
- **Video höher platzieren** — besser mit H1/Intro harmonieren
- **Testimonial-Zitat-Kasten unter Hero ENTFERNEN** ("Ich kann endlich wieder ins Schwimmbad...")

#### 2. "Kennen Sie dieses Gefühl?" Sektion
- **Neuer Text links** (komplett ersetzen, 4 Absätze, steht im Feedback)
- **Zitatkasten "Typischer Patient" ENTFERNEN**
- **CTA-Button beibehalten:** "Mein persönliches Beratungsgespräch sichern"
- **Zeile unter Button ENTFERNEN** ("100% unverbindlich. Absolut diskret. Kein Druck.")
- **Neues Bild rechts:** `images/kennen-sie-v3.jpg` (sportlicher Mann, graues T-Shirt)

#### 3. Testimonial-Sektion "Was andere Männer berichten"
- **Reihenfolge:** "ZURÜCK ZU SELBSTACHTUNG" als ERSTES Testimonial (holt Zielgruppe am stärksten ab)
- **Bewertungs-Karten aktualisieren:**
  - Google: 5,0 Sterne, 80+ Bewertungen, Link (siehe Feedback)
  - Jameda: 5,0 Sterne, 150+ Bewertungen, Link (siehe Feedback)
  - Doctify: 4,94/5 Sterne, 50+ Bewertungen, Link (siehe Feedback)
- **Karten KLICKBAR machen** (neuer Tab) + "Bewertungen ansehen →" CTA-Zeile pro Karte

#### 4. Dunkle CTA-Übergangssektion
- Headline bleibt: "Bereit für einen flachen, maskulinen Oberkörper?"
- Button bleibt: "Beratungstermin anfragen →"
- **Neue Subheadline:** "Diskret geplant, narbenarm umgesetzt — für ein Ergebnis, das natürlich männlich wirkt."
- **Neue graue Zeile:** "✓ Narbenarm geplant · ✓ Oft ambulant möglich · ✓ Langfristiges Ergebnis"

#### 5. "So funktioniert die Gynäkomastie-Korrektur" — MAJOR UPDATE
- **Neues Bild rechts:** `images/beratung-dr-meyer.jpg` (Dr. Meyer mit männlichem Patient)
- **Neuer Introtext** (2 Absätze, steht im Feedback)
- **5 neue Ablaufkarten** (statt bisherige 3-4):
  1. Ursachenklärung & Zielbild
  2. Individuelle Planung mit Vorher-Nachher
  3. Narbenarme Korrektur mit moderner Technik
  4. Sicherer Ablauf & kurze Ausfallzeit
  5. Langfristiges Ergebnis durch Ursachenbehandlung
  → Vollständige Texte stehen im Feedback-Dokument!

- **Stacked-Card-Scroll-Animation (Desktop):**
  - Karten beim Scrollen nacheinander in Fokus
  - Leicht versetzt/gestapelt aufbauen
  - Kurz sticky, dann nächste Karte nachrückt
  - NUR subtile Animationen: opacity, translateY, minimaler scale
  - Keine Rotationen, keine hektischen Moves
  - Texte IMMER vollständig lesbar

- **Mobile:**
  - KEINE komplexe Sticky-Stack-Animation
  - Sauber untereinander
  - Optional dezentes Fade-in/Slide-up
  - Genug Abstand

- **Accessibility:** `prefers-reduced-motion` respektieren!

## Bilder (lokal verfügbar)
- `images/kennen-sie-v3.jpg` — Sportlicher Mann, graues T-Shirt (für "Kennen Sie dieses Gefühl?")
- `images/beratung-dr-meyer.jpg` — Dr. Meyer Beratungssituation (für "So funktioniert")
- `images/hero-male-web.jpg` — Hero (bleibt)
- `images/gefuehl-male-web.jpg` — Alt (wird ersetzt durch kennen-sie-v3.jpg)
- `images/methode-fett.png`, `methode-druese.png`, `methode-kombi.png` — Methoden-Cards (bleiben)
- `images/arzt-kontakt-web.jpg` — Kontaktformular (bleibt)

## Ergebnis
- `gynaekomastie.html` mit allen V3-Änderungen
- Version in `versions/gynaekomastie-v3-luis-feedback.html` sichern
- Git commit mit beschreibender Message
