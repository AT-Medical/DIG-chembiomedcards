# Initiales Hosting auf ATMED-Core

## Ausgangssituation

Als praktischen ersten Schritt wird ChemBioMed Cards auf dem bestehenden ATMED-core-Server gehostet. Dieser Server betreibt bereits eine WordPress/WooCommerce-Infrastruktur, die für die initiale Verfügbarkeit des Projekts genutzt werden kann. Die Domain `chembiomed-cards.de` wird auf diesen Server zeigen; die statische Landingpage sowie erste digitale Karteninhalte werden dort bereitgestellt.

## Technischer Stack

Der ATMED-core-Server nutzt WordPress mit WooCommerce als Content-Management- und E-Commerce-Schicht. Die Landingpage (`index.html`) wird als statische Datei ausgeliefert und erfordert keine WordPress-Abhängigkeiten. Die dynamischen Plattformfunktionen (Kartenansicht, Nutzerkonten, QR-Redirect) werden als WordPress-Plugins oder separate PHP-Applikationen realisiert. Der QR-Redirect-Service („/c/<card-id>“) wird als eigenständiges Modul implementiert, das unabhängig vom CMS funktioniert.

## Wichtige Einschränkungen

Das Hosting auf ATMED-core ist ein pragmatischer Einstieg, keine dauerhafte Architekturentscheidung. Es besteht keine harte Kopplung zwischen dem Projekt und dem ATMED-core-Server – alle Komponenten werden so entwickelt, dass eine Migration zu einem dedizierten Server ohne Datenverlust und ohne Ausfallzeit möglich ist. Insbesondere der QR-Redirect-Service muss so ausgelegt sein, dass alle bestehenden QR-Codes nach einer Migration weiterhin funktionieren.

## Migrationspfad

Die Vorbereitung der Migration beginnt bereits beim initialen Setup: Datenbank-Exporte werden regelmäßig als Backup gespeichert, alle statischen Assets liegen in einem klar definierten Verzeichnisbaum, und die Konfiguration (Domain, Datenbankverbindung, API-Keys) wird über Umgebungsvariablen oder eine separate Konfigurationsdatei verwaltet. Details zur Migration sind im Dokument „future-dedicated-server.md“ beschrieben.
