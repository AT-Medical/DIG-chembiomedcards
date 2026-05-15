# Migration zu einem dedizierten Server

## Ziel der Migration

Mit wachsender Nutzerzahl und zunehmendem Kartenbestand wird die Migration von ATMED-core zu einem dedizierten Server notwendig. Ziel ist eine vollständige Entkopplung von der ATMED-core-Infrastruktur, bessere Ressourcenkontrolle (CPU, RAM, Storage) und die Möglichkeit, eine eigene CI/CD-Pipeline einzurichten.

## Entkopplungsanforderungen

Vor der Migration müssen folgende Entkopplungen abgeschlossen sein: (1) Der QR-Redirect-Service muss als eigenständiger Dienst laufen, der keine WordPress-Abhängigkeiten hat. (2) Die Nutzerdatenbank muss exportierbar und in ein schema-kompatibles Format überführbar sein. (3) Alle Mediendateien (Kartenbilder, PDF-Exporte) müssen in einem strukturierten Verzeichnis liegen, das als Ganzes migriert werden kann.

## Migrations-Checkliste

- [ ] Datenbank-Dump (MySQL/MariaDB) erstellen und validieren
- [ ] Mediendateien sichern und Integrität prüfen
- [ ] Lizenzschlüssel-Tabelle exportieren und importieren
- [ ] QR-Redirect-Tabelle („card_id → URL“) migrieren und testen
- [ ] DNS-Übergang planen (TTL im Voraus absenken, z. B. auf 300 s)
- [ ] SSL-Zertifikat auf neuem Server einrichten
- [ ] Smoke-Tests auf neuem Server vor DNS-Umschaltung durchführen
- [ ] Monitoring und Alerting aktivieren

## Zero-Downtime-Strategie

Die Migration erfolgt nach dem Blue/Green-Prinzip: Der neue Server wird parallel aufgebaut und vollständig getestet, bevor der DNS-Eintrag umgestellt wird. Während des Übergangs werden beide Server gleichzeitig betrieben; Schreiboperationen werden temporär auf den alten Server geleitet und nach DNS-Umstellung repliziert. Die DNS-TTL wird mindestens 48 Stunden vor der Migration auf einen niedrigen Wert abgesenkt, um die Propagationszeit zu minimieren.

## QR-URL-Stabilität

Die Stabilität der QR-Redirect-URLs („chembiomed-cards.de/c/<card-id>“) hat höchste Priorität, da gedruckte Karten nicht neu produziert werden können. Der Redirect-Service muss als erste Komponente auf dem neuen Server getestet und freigegeben werden, bevor der DNS-Übergang stattfindet.
