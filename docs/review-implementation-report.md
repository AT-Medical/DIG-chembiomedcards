# Review & Implementation Report

**Projekt:** ChemBioMed Cards  
**Betreiber:** AT Medical GmbH  
**Stand:** 2026-01-01  
**Status:** Work in Progress

---

## 1. Zusammenfassung

Dieser Bericht dokumentiert den aktuellen Umsetzungsstand des Projekts „ChemBioMed Cards“, identifiziert offene Punkte und gibt Empfehlungen für die nächsten Schritte.

Das Projekt umfasst:

- **Kartenproduktion** (Druckdesign, HTML/SVG-Vorlagen, QR-Codes)
- **Online-Plattform** (Landingpage, LMS, Authentifizierung, Lizenzmodell)
- **Inhaltserstellung** (6 Module: AC, OC, BC, MB, APC, PH)
- **Repository-Infrastruktur** (GitHub, CI/CD, Metadaten-Registry)

---

## 2. Abgeschlossene Aufgaben

| Aufgabe | Status |
|---------|--------|
| Karten-Templates (HTML + SVG, Front/Rückseite) | ✅ Abgeschlossen |
| Landingpage (online-platform/landing-page/index.html) | ✅ Abgeschlossen |
| Architektur-Dokumentation (6 Dokumente) | ✅ Abgeschlossen |
| Frontend-Spezifikation (UX + 3 Layouts) | ✅ Abgeschlossen |
| Lizenzmodell-Dokumentation (3 Dokumente) | ✅ Abgeschlossen |
| Benutzerfeatures-Dokumentation (2 Dokumente) | ✅ Abgeschlossen |
| Druckproduktion-Spezifikation (3 Dokumente) | ✅ Abgeschlossen |
| Python-Skripte (3 Scaffold-Skripte) | ✅ Abgeschlossen |
| Paket-Registry YAML | ✅ Abgeschlossen |
| Karten-Metadaten-Beispiel (Felder ergänzt) | ✅ Abgeschlossen |
| Brand/Naming Guidelines | ✅ Abgeschlossen |

---

## 3. Offene Punkte

### 3.1 Inhaltliche Erstellung

- Alle Karteninhalte (Texte, Strukturformeln, Abbildungen) müssen noch erstellt werden.
- Derzeit existiert nur die Metadaten-Beispielkarte `oc_012` als Referenz.
- Ziel: Vollständige Kartensätze für AC, OC, BC, MB, APC je Kapitel.

### 3.2 Python-Skripte (Implementierung)

Die folgenden Skripte sind als Scaffold vorhanden und müssen implementiert werden:

- `scripts/generate_qr_codes.py` – QR-Code-Generierung (TODO: qrcode-Bibliothek einbinden)
- `scripts/generate_card_registry.py` – YAML→CSV (TODO: yaml.safe_load() implementieren)
- `scripts/export_print_batch.py` – PDF-Export (TODO: WeasyPrint oder Headless-Chrome)

### 3.3 Plattform-Entwicklung

- WordPress + WooCommerce Installation und Konfiguration ausständig
- LMS (Moodle oder LearnDash) Setup ausständig
- QR-Redirect-Dienst (`chembiomed-cards.de/c/<card_id>`) ausständig
- Authentifizierungsgateway (z. B. Keycloak) ausständig

### 3.4 Druckproduktion

- Druckfertigkeit der PDF-Dateien noch nicht erreicht
- Abstimmung mit Druckdienstleister ausständig
- Kartenbox-Produktion (Offsetdruck oder Digitaldruck) noch offen

### 3.5 Lizenzierung und Preise

- Preise für alle Pakete noch nicht festgelegt (in `package-registry.yaml` als `null` gesetzt)
- Lizenzschlüssel-Infrastruktur (Generierung, Validierung) noch nicht implementiert

---

## 4. Risiken und Hinweise

| Risiko | Bewertung | Maßnahme |
|--------|-----------|----------|
| Zeitplan Kartenproduktion | Hoch | Priorisierung der OC-Karten als erstes Teilset |
| WooCommerce-Integration Komplexität | Mittel | Plugin-Auswahl frühzeitig festlegen |
| Druckqualität (Farbprofil CMYK vs. RGB) | Mittel | Frühzeitig mit Druckdienstleister abstimmen |
| GitHub Actions Validator | Niedrig | Bereits implementiert, läuft auf `push` |

---

## 5. Empfohlene nächste Schritte

1. **Kartenproduktion starten** – Organische Chemie (OC) als Pilotmodul, 10–20 Karten
2. **QR-Redirect-Dienst aufsetzen** – einfachste Variante: Netlify Redirect oder Node.js-Microservice
3. **Landingpage live schalten** – nach DNS-Konfiguration für chembiomed-cards.de
4. **WooCommerce-Pilotshop** – mit einem Testpaket und Demo-Lizenzschlüssel
5. **LMS-Entscheidung treffen** – Moodle vs. LearnDash (abhängig von WP-Infrastruktur)

---

## 6. Technische Schulden

- Die Python-Skripte sind Scaffolds und benötigen echte Implementierungen.
- Die `cards.master.csv` und `cards.master.schema.json` sind geschützte Dateien – manuelle Pflege nötig bis der Generator funktioniert.
- Alle `price_eur: null`-Einträge in `package-registry.yaml` müssen aktualisiert werden.

---

*Zuletzt aktualisiert: AT Medical GmbH | 2026-01-01*
