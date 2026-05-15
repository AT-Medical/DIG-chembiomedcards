# Spaced Repetition

## Leitner-Box-Modell (5 Fächer)

Das Spaced-Repetition-System basiert auf dem Leitner-Box-Modell mit 5 Fächern. Neue Karten beginnen in Fach 1. Beantwortet der Nutzer eine Karte korrekt (Lernstatus „Bekannt“), wandert sie in das nächste Fach. Beantwortet er sie falsch (Lernstatus „Unbekannt“), wandert sie in Fach 1 zurück. Lernstatus „Wiederholen“ behält die Karte im aktuellen Fach.

## Wiederholungsintervalle

Die Wiederholungsintervalle für die fünf Fächer sind: Fach 1 (täglich), Fach 2 (alle 2 Tage), Fach 3 (alle 4 Tage), Fach 4 (alle 8 Tage), Fach 5 (alle 16 Tage). Diese Intervalle sind vorläufig und können später durch einen SM-2-Algorithmus ersetzt werden. Karten in Fach 5, die erneut korrekt beantwortet werden, gelten als „gelernt“ und erscheinen nur noch bei manueller Wiederholung.

## Integration mit dem Lernstatus

Die drei Lernstatus-Optionen („Bekannt“, „Unbekannt“, „Wiederholen“) sind direkt mit der Box-Bewegung verknüpft: „Bekannt“ → Karte steigt in nächstes Fach; „Unbekannt“ → Karte fällt in Fach 1 zurück; „Wiederholen“ → Karte bleibt im aktuellen Fach, Termin wird in 24 h neu geplant.

## Tägliche Review-Queue

Täglich generiert das System eine Review-Queue aus allen Karten, deren nächster Wiederholungstermin heute oder in der Vergangenheit liegt. Die Queue ist nach Fach priorisiert (Fächer 1 und 2 zuerst). Der SM-2-Algorithmus ist als zukünftige Erweiterung vorbereitet; die aktuelle Implementierung nutzt feste Intervalle.
