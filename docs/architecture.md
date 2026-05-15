# Zielarchitektur (Initial)

## Hauptachsen
1. Druckversion (Assets, Templates, Kartenpakete)
2. Onlineplattform (Lernkartenbox, Lizenzlogik, Status, Notizen, Uploads)

## Technische Leitlinien
- Startbetrieb: chembiomed-cards.de auf ATMED-core
- WordPress/WooCommerce vorhanden für initiale Kauf-/Lizenzflüsse
- Perspektivisch: eigene App + eigener Server + Gateway/SSO
- Karten als strukturierte Datensätze (nicht nur Bilder)

## Plattform-Bausteine (geplant)
- Frontend: z. B. Next.js
- Backend/API: z. B. FastAPI oder Laravel
- Datenbank: PostgreSQL
- Objektstorage: S3/R2-kompatibel
- QR-/Redirect-Service für stabile Printlinks
- Import/Export: CSV/YAML/JSON (+ später PDF/Anki)
