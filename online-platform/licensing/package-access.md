# Paketzugang und Zugriffskontrolle

## Zugangstabellen-Struktur

Die Paketzugriffskontrolle basiert auf einer einfachen Nutzertabelle: `user_package_access (user_id, package_id, license_key_id, granted_at, expires_at, status)`. Bei jeder API-Anfrage auf eine gesperrte Ressource wird diese Tabelle geprüft. Die Prüfung findet serverseitig statt; gecachte Zugangsentscheidungen sind nur für die Dauer der aktuellen Sitzung gültig.

## Grace-Period für Abonnements

Um eine harte Zugriffssperrung nach Ablauf eines Abonnements zu vermeiden, gilt eine Grace-Period von 7 Tagen. Während dieser Periode kann der Nutzer weiterhin auf die freigeschalteten Karten zugreifen, erhält aber täglich eine Erinnerung, das Abonnement zu verlängern. Nach Ablauf der Grace-Period wird der Zugang gesperrt, die Lerndaten (Lernstatus, Notizen) bleiben jedoch erhalten. Bei Verlängerung des Abonnements wird der Zugang sofort wiederhergestellt.

## Offline-Zugang und heruntergeladene Inhalte

Heruntergeladene Inhalte (z. B. PDF-Druckvorlagen) bleiben nach Ablauf des Abonnements lokal verfügbar. Der Online-Zugang auf die Plattform und auf neue Inhalte erfordert eine gültige Lizenz. Eine vollständige Offline-Kartenansicht ist als zukünftige Funktion geplant; in der initialen Version ist nur Online-Zugang vorgesehen.
