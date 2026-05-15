# Smartphone-Layout

## Einspaltiges Layout

Das Smartphone-Layout zeigt Inhalte in einer einzigen Spalte. Die Karte nimmt den größten Teil des Bildschirms ein. Unterhalb der Karte befinden sich die Lernstatus-Buttons („Bekannt“, „Wiederholen“, „Unbekannt“) in voller Breite. Ein Antippen der Karte dreht diese um (Flip-Modus). Im Vollbild-Kartenmodus werden alle anderen UI-Elemente ausgeblendet, um eine ablenkungsfreie Lernerfahrung zu ermöglichen.

## Bottom-Navigation

Die Navigation am unteren Bildschirmrand enthält vier Symbole: **Home** (Startseite), **Karten** (Kartenauswahl und -browser), **Lernen** (aktive Lernsitzung), **Profil** (Nutzereinstellungen, Lernstatistiken, Lizenzverwaltung). Die Bottom-Navigation bleibt während einer Lernsitzung sichtbar, kann aber im Vollbildmodus ausgeblendet werden.

## Minimales Chrome und Vollbild

Im Lernmodus wird der Browser-Chrome (Adresszeile) so weit wie möglich ausgeblendet, um maximale Kartenfläche zu bieten. Die Vollbild-Option (via Web-Fullscreen-API) wird angeboten, ist aber optional. Die Navigation zwischen Karten erfolgt per Wischen oder über kleine Pfeiltasten-Buttons.

## Offline-Grundfunktionalität

Für Smartphones ist eine einfache Offline-Unterstützung geplant (Service Worker, Caching der zuletzt angesehenen Kartensets). Details der Offline-Implementierung werden in einer späteren Phase festgelegt; diese Anforderung ist als zukünftige Erweiterung markiert.
