# Technischer Review- und Implementierungsbericht (auditierbar)

**Projekt:** ChemBioMed Cards  
**Repository:** `AT-Medical/DIG-chembiomedcards`  
**Stand:** 2026-05-16  
**Berichtstyp:** Technischer Review-Bericht (Audit-fähig)  
**Status:** Aktualisiert

---

## 1. Audit-Rahmen und Quellenbasis

Dieser Bericht dokumentiert den aktuellen technischen Projektstand mit nachvollziehbaren Nachweisen aus Repository-Struktur, Commit-Historie und reproduzierbaren Validierungsläufen.

**Nachweisquellen:**
- Repository-Stand: Branch `copilot/update-review-implementation-report`
- Implementierungs-Basisstand: Commit `5f3ccb4` (`feat: full repository build-out (Tasks 1–16)`)
- Laufzeit-Validierungen: lokal ausgeführte Shell-Kommandos (siehe Abschnitt 3)

---

## 2. Konkrete Liste neu erstellter/geänderter Dateien

### 2.1 Implementierungs-Basisstand (Commit `5f3ccb4`)

```text
A	.github/ISSUE_TEMPLATE/bug-report.yml
A	.github/ISSUE_TEMPLATE/card-production.yml
A	.github/ISSUE_TEMPLATE/content-review.yml
A	.github/ISSUE_TEMPLATE/platform-feature.yml
A	.github/pull_request_template.md
A	.github/workflows/validate-metadata.yml
A	.gitignore
A	CHANGELOG.md
A	LICENSE.md
A	README.md
A	brand/colors/color-system.md
A	brand/design-tokens/README.md
A	brand/design-tokens/chembiomed.tokens.json
A	brand/logo/README.md
A	brand/logo/source/.gitkeep
A	brand/naming-guidelines.md
A	brand/typography/typography-system.md
A	card-system/card-types/case-card.md
A	card-system/card-types/clinical-card.md
A	card-system/card-types/comparison-card.md
A	card-system/card-types/overview-card.md
A	card-system/card-types/reaction-card.md
A	card-system/card-types/structure-card.md
A	card-system/examples/oc_012_primaerer_alkohol_back.example.md
A	card-system/examples/oc_012_primaerer_alkohol_front.example.md
A	card-system/layout-standard/back-layout.md
A	card-system/layout-standard/din-a6-landscape-standard.md
A	card-system/layout-standard/footer-and-copyright.md
A	card-system/layout-standard/front-layout.md
A	card-system/layout-standard/inward-tabs-system.md
A	card-system/layout-standard/print-safety.md
A	card-system/layout-standard/qr-code-placement.md
A	card-system/templates/README.md
A	card-system/templates/card-template-back.html
A	card-system/templates/card-template-back.svg
A	card-system/templates/card-template-front.html
A	card-system/templates/card-template-front.svg
A	cards/AC/README.md
A	cards/AC/ac_cards_index.md
A	cards/AC/back/.gitkeep
A	cards/AC/front/.gitkeep
A	cards/AC/metadata/.gitkeep
A	cards/AC/print/.gitkeep
A	cards/APC/README.md
A	cards/APC/apc_cards_index.md
A	cards/APC/back/.gitkeep
A	cards/APC/front/.gitkeep
A	cards/APC/metadata/.gitkeep
A	cards/APC/print/.gitkeep
A	cards/BC/README.md
A	cards/BC/back/.gitkeep
A	cards/BC/bc_cards_index.md
A	cards/BC/front/.gitkeep
A	cards/BC/metadata/.gitkeep
A	cards/BC/print/.gitkeep
A	cards/MB/README.md
A	cards/MB/back/.gitkeep
A	cards/MB/front/.gitkeep
A	cards/MB/mb_cards_index.md
A	cards/MB/metadata/.gitkeep
A	cards/MB/print/.gitkeep
A	cards/OC/README.md
A	cards/OC/back/.gitkeep
A	cards/OC/front/.gitkeep
A	cards/OC/metadata/.gitkeep
A	cards/OC/oc_cards_index.md
A	cards/OC/print/.gitkeep
A	cards/PH/README.md
A	cards/PH/back/.gitkeep
A	cards/PH/front/.gitkeep
A	cards/PH/metadata/.gitkeep
A	cards/PH/ph_cards_index.md
A	cards/PH/print/.gitkeep
A	cards/README.md
A	cards/registry/card-metadata-example.yaml
A	cards/registry/cards.master.csv
A	cards/registry/cards.master.schema.json
A	cards/registry/package-registry.yaml
A	deploy/ATMED-core-deployment-notes.md
A	docs/cooperation-notes.md
A	docs/domain-and-hosting.md
A	docs/legal-rights-notes.md
A	docs/product-vision.md
A	docs/project-overview.md
A	docs/publishing-strategy.md
A	docs/review-implementation-report.md
A	docs/roadmap.md
A	exports/README.md
A	exports/anki/.gitkeep
A	exports/pdf/.gitkeep
A	exports/publisher/.gitkeep
A	exports/web/.gitkeep
A	imports/README.md
A	imports/csv/.gitkeep
A	imports/source-material/.gitkeep
A	imports/yaml/.gitkeep
A	lms-content/README.md
A	lms-content/chapter-links/.gitkeep
A	lms-content/extended-chapters/.gitkeep
A	lms-content/moodle-integration.md
A	lms-content/qr-targets/.gitkeep
A	online-platform/README.md
A	online-platform/architecture/atmed-core-initial-hosting.md
A	online-platform/architecture/future-dedicated-server.md
A	online-platform/architecture/gateway-authentication.md
A	online-platform/architecture/lms-integration.md
A	online-platform/architecture/platform-architecture.md
A	online-platform/architecture/qr-redirect-service.md
A	online-platform/architecture/wordpress-woocommerce-integration.md
A	online-platform/backend/README.md
A	online-platform/backend/api-requirements.md
A	online-platform/backend/card-api.md
A	online-platform/backend/license-api.md
A	online-platform/backend/media-api.md
A	online-platform/backend/notes-api.md
A	online-platform/database/README.md
A	online-platform/database/data-model.md
A	online-platform/database/schema-draft.sql
A	online-platform/frontend/README.md
A	online-platform/frontend/desktop-layout.md
A	online-platform/frontend/smartphone-layout.md
A	online-platform/frontend/tablet-layout.md
A	online-platform/frontend/ux-requirements.md
A	online-platform/landing-page/README.md
A	online-platform/landing-page/index.html
A	online-platform/licensing/campus-licenses.md
A	online-platform/licensing/license-key-flow.md
A	online-platform/licensing/license-model.md
A	online-platform/licensing/package-access.md
A	online-platform/licensing/publisher-integration.md
A	online-platform/user-features/custom-card-sets.md
A	online-platform/user-features/learning-status.md
A	online-platform/user-features/spaced-repetition.md
A	online-platform/user-features/storage-quotas.md
A	online-platform/user-features/user-media-uploads.md
A	online-platform/user-features/user-notes.md
A	print-production/README.md
A	print-production/exports/pdf/.gitkeep
A	print-production/exports/png/.gitkeep
A	print-production/exports/prepress/.gitkeep
A	print-production/packaging/box-concepts.md
A	print-production/packaging/package-inserts.md
A	print-production/packaging/product-line-structure.md
A	print-production/specs/bleed-and-safe-zone.md
A	print-production/specs/card-box-production-notes.md
A	print-production/specs/din-a6-landscape-print-spec.md
A	print-production/specs/qr-print-spec.md
A	scripts/README.md
A	scripts/export_print_batch.py
A	scripts/generate_card_registry.py
A	scripts/generate_qr_codes.py
A	scripts/validate_card_metadata.py
```

### 2.2 Aktuelle Berichtsanpassung

```text
M	docs/review-implementation-report.md
```

---

## 3. Validierungsausgaben (reproduzierbar)

### 3.1 `python3 -m py_compile scripts/*.py`

- Exit-Code: `0`

```text
(keine stdout-Ausgabe)

```

### 3.2 `python3 scripts/validate-card-metadata.py` (angeforderter Befehl, fehlschlagend)

- Exit-Code: `2`

```text
(keine stdout-Ausgabe)
python3: can't open file '/home/runner/work/DIG-chembiomedcards/DIG-chembiomedcards/scripts/validate-card-metadata.py': [Errno 2] No such file or directory
```

**Bewertung:** Der im Auftrag angegebene Dateiname mit Bindestrich existiert nicht im Repository.

### 3.3 Operativ tatsächlich vorhandener Validator (für Soll-Ist-Abgleich)

Korrigierter und im Repository vorhandener Aufruf:

`python3 scripts/validate_card_metadata.py --csv cards/registry/cards.master.csv`

- Exit-Code: `0`

```text
Validation passed: cards/registry/cards.master.csv

```

### 3.4 `find . -maxdepth 4 -type f | sort`

- Exit-Code: `0`

```text
./.git/FETCH_HEAD
./.git/HEAD
./.git/config
./.git/copilot-hooks/prepare-commit-msg
./.git/description
./.git/hooks/applypatch-msg.sample
./.git/hooks/commit-msg.sample
./.git/hooks/fsmonitor-watchman.sample
./.git/hooks/post-update.sample
./.git/hooks/pre-applypatch.sample
./.git/hooks/pre-commit.sample
./.git/hooks/pre-merge-commit.sample
./.git/hooks/pre-push.sample
./.git/hooks/pre-rebase.sample
./.git/hooks/pre-receive.sample
./.git/hooks/prepare-commit-msg.sample
./.git/hooks/push-to-checkout.sample
./.git/hooks/sendemail-validate.sample
./.git/hooks/update.sample
./.git/index
./.git/info/exclude
./.git/logs/HEAD
./.git/objects/pack/pack-bb80acfd0809513ba3ca416a2904495597f150de.idx
./.git/objects/pack/pack-bb80acfd0809513ba3ca416a2904495597f150de.pack
./.git/objects/pack/pack-bb80acfd0809513ba3ca416a2904495597f150de.rev
./.git/packed-refs
./.git/shallow
./.github/ISSUE_TEMPLATE/bug-report.yml
./.github/ISSUE_TEMPLATE/card-production.yml
./.github/ISSUE_TEMPLATE/content-review.yml
./.github/ISSUE_TEMPLATE/platform-feature.yml
./.github/pull_request_template.md
./.github/workflows/validate-metadata.yml
./.gitignore
./CHANGELOG.md
./LICENSE.md
./README.md
./brand/colors/color-system.md
./brand/design-tokens/README.md
./brand/design-tokens/chembiomed.tokens.json
./brand/logo/README.md
./brand/logo/source/.gitkeep
./brand/naming-guidelines.md
./brand/typography/typography-system.md
./card-system/card-types/case-card.md
./card-system/card-types/clinical-card.md
./card-system/card-types/comparison-card.md
./card-system/card-types/overview-card.md
./card-system/card-types/reaction-card.md
./card-system/card-types/structure-card.md
./card-system/examples/oc_012_primaerer_alkohol_back.example.md
./card-system/examples/oc_012_primaerer_alkohol_front.example.md
./card-system/layout-standard/back-layout.md
./card-system/layout-standard/din-a6-landscape-standard.md
./card-system/layout-standard/footer-and-copyright.md
./card-system/layout-standard/front-layout.md
./card-system/layout-standard/inward-tabs-system.md
./card-system/layout-standard/print-safety.md
./card-system/layout-standard/qr-code-placement.md
./card-system/templates/README.md
./card-system/templates/card-template-back.html
./card-system/templates/card-template-back.svg
./card-system/templates/card-template-front.html
./card-system/templates/card-template-front.svg
./cards/AC/README.md
./cards/AC/ac_cards_index.md
./cards/AC/back/.gitkeep
./cards/AC/front/.gitkeep
./cards/AC/metadata/.gitkeep
./cards/AC/print/.gitkeep
./cards/APC/README.md
./cards/APC/apc_cards_index.md
./cards/APC/back/.gitkeep
./cards/APC/front/.gitkeep
./cards/APC/metadata/.gitkeep
./cards/APC/print/.gitkeep
./cards/BC/README.md
./cards/BC/back/.gitkeep
./cards/BC/bc_cards_index.md
./cards/BC/front/.gitkeep
./cards/BC/metadata/.gitkeep
./cards/BC/print/.gitkeep
./cards/MB/README.md
./cards/MB/back/.gitkeep
./cards/MB/front/.gitkeep
./cards/MB/mb_cards_index.md
./cards/MB/metadata/.gitkeep
./cards/MB/print/.gitkeep
./cards/OC/README.md
./cards/OC/back/.gitkeep
./cards/OC/front/.gitkeep
./cards/OC/metadata/.gitkeep
./cards/OC/oc_cards_index.md
./cards/OC/print/.gitkeep
./cards/PH/README.md
./cards/PH/back/.gitkeep
./cards/PH/front/.gitkeep
./cards/PH/metadata/.gitkeep
./cards/PH/ph_cards_index.md
./cards/PH/print/.gitkeep
./cards/README.md
./cards/registry/card-metadata-example.yaml
./cards/registry/cards.master.csv
./cards/registry/cards.master.schema.json
./cards/registry/package-registry.yaml
./deploy/ATMED-core-deployment-notes.md
./docs/cooperation-notes.md
./docs/domain-and-hosting.md
./docs/legal-rights-notes.md
./docs/product-vision.md
./docs/project-overview.md
./docs/publishing-strategy.md
./docs/review-implementation-report.md
./docs/roadmap.md
./exports/README.md
./exports/anki/.gitkeep
./exports/pdf/.gitkeep
./exports/publisher/.gitkeep
./exports/web/.gitkeep
./imports/README.md
./imports/csv/.gitkeep
./imports/source-material/.gitkeep
./imports/yaml/.gitkeep
./lms-content/README.md
./lms-content/chapter-links/.gitkeep
./lms-content/extended-chapters/.gitkeep
./lms-content/moodle-integration.md
./lms-content/qr-targets/.gitkeep
./online-platform/README.md
./online-platform/architecture/atmed-core-initial-hosting.md
./online-platform/architecture/future-dedicated-server.md
./online-platform/architecture/gateway-authentication.md
./online-platform/architecture/lms-integration.md
./online-platform/architecture/platform-architecture.md
./online-platform/architecture/qr-redirect-service.md
./online-platform/architecture/wordpress-woocommerce-integration.md
./online-platform/backend/README.md
./online-platform/backend/api-requirements.md
./online-platform/backend/card-api.md
./online-platform/backend/license-api.md
./online-platform/backend/media-api.md
./online-platform/backend/notes-api.md
./online-platform/database/README.md
./online-platform/database/data-model.md
./online-platform/database/schema-draft.sql
./online-platform/frontend/README.md
./online-platform/frontend/desktop-layout.md
./online-platform/frontend/smartphone-layout.md
./online-platform/frontend/tablet-layout.md
./online-platform/frontend/ux-requirements.md
./online-platform/landing-page/README.md
./online-platform/landing-page/index.html
./online-platform/licensing/campus-licenses.md
./online-platform/licensing/license-key-flow.md
./online-platform/licensing/license-model.md
./online-platform/licensing/package-access.md
./online-platform/licensing/publisher-integration.md
./online-platform/user-features/custom-card-sets.md
./online-platform/user-features/learning-status.md
./online-platform/user-features/spaced-repetition.md
./online-platform/user-features/storage-quotas.md
./online-platform/user-features/user-media-uploads.md
./online-platform/user-features/user-notes.md
./print-production/README.md
./print-production/exports/pdf/.gitkeep
./print-production/exports/png/.gitkeep
./print-production/exports/prepress/.gitkeep
./print-production/packaging/box-concepts.md
./print-production/packaging/package-inserts.md
./print-production/packaging/product-line-structure.md
./print-production/specs/bleed-and-safe-zone.md
./print-production/specs/card-box-production-notes.md
./print-production/specs/din-a6-landscape-print-spec.md
./print-production/specs/qr-print-spec.md
./scripts/README.md
./scripts/__pycache__/export_print_batch.cpython-312.pyc
./scripts/__pycache__/generate_card_registry.cpython-312.pyc
./scripts/__pycache__/generate_qr_codes.cpython-312.pyc
./scripts/__pycache__/validate_card_metadata.cpython-312.pyc
./scripts/export_print_batch.py
./scripts/generate_card_registry.py
./scripts/generate_qr_codes.py
./scripts/validate_card_metadata.py

```

---

## 4. Architekturentscheidungen (korrigiert)

### 4.1 Authentifizierungsrichtung (korrigiert)

Primäre Richtung ist **ATMED-Gateway mit SSO auf Basis authentik/OIDC**.  
Keycloak ist **nicht** als Primärlösung gesetzt und wird aus der Primärposition entfernt.

**Zielbild:**
- Zentrale Authentifizierung über ATMED-Gateway
- SSO für Kartenplattform, QR-Redirect und LMS
- OIDC-konforme Token-/Session-Strategie
- WooCommerce-Accountmodell nur als initiales Übergangskonstrukt

### 4.2 QR-Redirect-Default (korrigiert)

**Netlify Redirect ist nicht Default.**  
Default ist ein **eigener Redirect-Service auf ATMED-core**, mit geplanter späterer Migration auf einen dedizierten Server.

**Konsequenz für Stabilität:**
- Öffentliche QR-URLs bleiben dauerhaft stabil (`/c/<card-id>`)
- Backend-Hosting kann migriert werden, ohne QR-Codes im Druck zu brechen

---

## 5. Plattformpriorisierung und Feature-Status

### 5.1 LMS-Priorität

- **Primäre Vertiefungsplattform:** Moodle/LMS
- **Optionale Alternative:** LearnDash (WordPress-nahe Option)

### 5.2 Onlineplattform-Features (klarer Funktionsrahmen)

Die Plattform ist auf folgende Kernfunktionen auszurichten:

1. Eigene Kartensammlungen pro Nutzer
2. Lernstatus pro Nutzer und Karte
3. Nutzernotizen pro Karte
4. Nutzer-Medienuploads pro Karte
5. Speicherquoten pro Nutzerkonto
6. Tablet-first UX als primäre Bedienlogik
7. Smartphone-Ansicht als verpflichtendes Responsive-Zielbild
8. Strikte Trennung offizieller Inhalte und privater Nutzerinhalte

---

## 6. Produktlinie PH / Pharmakologie

PH (Pharmakologie) ist strukturell angelegt und wird als **spätere Produktlinie** verstärkt dokumentiert:

- Separate inhaltliche Ausbauphase nach Kernmodulen AC/OC/BC/MB/APC
- Eigene Positionierung als Erweiterungsmodul innerhalb der Produktfamilie
- Berücksichtigung in LMS-Struktur, Kartenregister und Paket-/Lizenzlogik

---

## 7. Rechtliche offene Punkte (erweitert)

Die folgenden Punkte sind offen und für den Go-Live kritisch:

1. Urheberrechte an Karteninhalten, Grafiken, Formeln und didaktischen Aufbereitungen
2. Vertrags- und Freigabemodell für externe Fachherausgeber
3. Rechtekette und Vergütungsmodell für studentische Beiträge
4. Rollen- und Rechteabgrenzung mit Verlagspartnern
5. Print-/Digitalrechte je Inhaltspaket und Vertriebskanal
6. Datenschutz (insb. Nutzerprofile, Lernstatus, Uploads, LMS-Integrationen)

---

## 8. Technischer Review-Befund (nicht nur Management-Zusammenfassung)

### 8.1 Positiver Ist-Stand

- Repository-Struktur und Modulaufteilung sind konsistent angelegt.
- Architektur-, Plattform- und Produktionsdokumente sind breit vorbereitet.
- Metadaten-Validierung ist als CI-Workflow und Skriptgrundlage vorhanden.

### 8.2 Technische Lücken

- Mehrere Python-Skripte sind weiterhin Scaffold/TODO-nah.
- Das im Problemstatement genannte Validator-Skript mit Bindestrich ist nicht vorhanden (Namensabweichung).
- Rechte- und Datenschutzfragen sind dokumentiert, aber noch nicht entscheidungsreif operationalisiert.

### 8.3 Verbindliche nächste technische Schritte

1. Script-Namenskonvention harmonisieren (Bindestrich vs. Unterstrich) oder Alias bereitstellen.
2. Redirect-Service auf ATMED-core als produktionsnahen Minimaldienst umsetzen.
3. ATMED-Gateway/SSO/authentik/OIDC-Entscheidung als verbindliche Referenzarchitektur fixieren.
4. Moodle-zentrierten Integrationspfad inkl. Lernstatus-/Rechtesynchronisation konkretisieren.
5. Rechts- und Governance-Backlog in umsetzbare Arbeitspakete mit Verantwortlichkeiten überführen.

---

*Zuletzt aktualisiert: AT Medical GmbH | 2026-05-16*
