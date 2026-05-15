# DIG-chembiomedcards

ChemBioMed Cards: skalierbares Lernkarten-Referenzsystem für Chemie, Biochemie, Molekularbiologie, Ernährung, Medizin und Pharmakologie mit DIN-A6-Druckkarten, Online-Lernplattform, Lizenzlogik, Notizen, QR-/LMS-Anbindung und AT-Medical-Workflow.

## Projektstruktur (Initialisierung)

```text
DIG-chembiomedcards/
├── data/                 # Strukturierte Kartendaten, Import/Export, Redirect-Mapping, Pakete
├── docs/                 # Verbindliche Spezifikationen (Layout, Architektur, Workflows)
├── platform/             # Onlineplattform (frontend/backend/auth/storage/integrations)
└── print/                # Druckproduktion (Templates, Pakete, drucknahe Assets)
```

Die Struktur ist bewusst framework-neutral gehalten, um spätere technische Entscheidungen (z. B. Next.js/FastAPI/Laravel) nicht vorwegzunehmen.
