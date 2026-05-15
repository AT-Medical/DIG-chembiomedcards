# UX-Anforderungen

## Design-Prinzip: Tablet-first

Die Plattform wird primär für die Nutzung auf 10-Zoll-Tablets im Querformat konzipiert. Dies entspricht dem typischen Lernkontext (auf dem Schreibtisch neben Buch und Notizen). Das Interface muss auf Tablets intuitiv bedienbar sein, ohne dass eine Einführung nötig ist. Desktop und Smartphone erhalten angepasste Layouts, sind aber sekundäre Zielplattformen. Alle interaktiven Elemente müssen eine Mindestgröße von 44×44 px haben (WCAG-Richtlinie für Touch-Ziele).

## Kern-Interaktionen

Die wichtigsten Nutzerinteraktionen sind: (1) **Karte umdrehen** – Antippen der Karte dreht sie um (3D-Flip-Animation, 300 ms); (2) **Lernstatus setzen** – drei Buttons unterhalb der Karte: „Bekannt“ (grün), „Wiederholen“ (orange), „Unbekannt“ (rot); (3) **Navigieren** – Wischen nach links/rechts geht zur nächsten/vorherigen Karte; (4) **Notiz anzeigen** – eigene Nutzernotizen werden unterhalb der Karte als ausklappbarer Bereich angezeigt; (5) **Medien-Upload** – Nutzer können eigene Bilder oder PDFs zu einer Karte hochladen.

## Benutzerdefinierte Sets und Filter

Nutzer können eigene Kartensets aus beliebigen Modulen zusammenstellen. Sets können nach Modul, Kapitel, Schwierigkeitsgrad und Lernstatus gefiltert werden. Die Filterkombination wird in der URL kodiert, sodass direkte Links zu Lernsitzungen möglich sind.

## Responsive Breakpoints

Die Plattform unterstützt vier Breakpoints: 320 px (kleines Smartphone), 768 px (großes Smartphone / kleines Tablet), 1024 px (Tablet / kleines Desktop) und 1440 px (Desktop). Unter 768 px wechselt das Layout auf die Smartphone-Ansicht (Einzelspalte, Bottom-Navigation).

## Barrierefreiheit

Alle interaktiven Elemente sind per Tastatur navigierbar. Karten haben ARIA-Labels; der Flip-Status wird als ARIA-Live-Region ausgegeben. Farbkodierungen werden nicht als alleiniges Unterscheidungsmerkmal verwendet (Lernstatus zusätzlich mit Icon und Text). Kontraste erfüllen WCAG 2.1 Level AA.
