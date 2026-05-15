# LMS-Integration

## Konzept

Die LMS-Integration ermöglicht die Einbindung von ChemBioMed Cards in Learning-Management-Systeme. Als Referenz-LMS dient Moodle, da es weit verbreitet, Open Source und gut dokumentiert ist. Die Karten-URL-Struktur für das LMS lautet: `lms.at-medical.example/<modul>/<kartenname>`, z. B. `lms.at-medical.example/oc/primaerer-alkohol`. Diese URLs werden im Karten-Metadatensatz als `lms_url`-Feld geführt.

## URL-Struktur und Kapitelverknüpfung

Jede Karte ist einem Lernkapitel zugeordnet, das in der LMS-Struktur als Kurs-Abschnitt abgebildet wird. Die Kapitelstruktur spiegelt die Modul-/Kapitel-Hierarchie des Kartenregisters wider. Eine Karte kann in mehrere LMS-Kurse eingebunden werden; die kanonische URL bleibt unverfändert. Lernziele pro Karte („learning\_objectives“ im Metadatensatz) werden als LMS-Lernziele übernommen.

## Datenmodell und Schnittstellen

Das Karten-Metadatenmodell ist so gestaltet, dass es für eine spätere SCORM-Paketierung oder xAPI-Integration genutzt werden kann. SCORM- und xAPI-Unterstützung sind für eine spätere Phase geplant und noch nicht implementiert. Für die initiale Integration genügt das Einbetten der Karten-URLs als externe Links in Moodle-Kursen.

## Implementierungshinweise für Moodle

In Moodle wird jedes Modul (AC, OC, BC, MB, APC, PH) als eigener Kurs angelegt. Karten werden als „URL-Aktivität“ eingebunden. Für eine tiefere Integration kann ein Moodle-Plugin entwickelt werden, das den Lernstatus (Bekannt/Unbekannt/Wiederholen) zwischen ChemBioMed-Plattform und Moodle synchronisiert. Diese Synchronisation setzt eine API auf der ChemBioMed-Plattform voraus, die OAuth2-authentifizierte Anfragen von Moodle akzeptiert.
