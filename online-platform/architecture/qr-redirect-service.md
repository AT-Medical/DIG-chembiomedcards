# QR-Redirect-Service

## Konzept und Zweck

Der QR-Redirect-Service stellt sicher, dass jeder gedruckte QR-Code dauerhaft auf die korrekte digitale Kartenansicht zeigt – unabhängig von technischen Migrationen, URL-Änderungen oder Inhaltsaktualisierungen. Das Muster lautet: `https://chembiomed-cards.de/c/<card-id>`, z. B. `https://chembiomed-cards.de/c/oc-012`. Diese URL ist dauerhaft und darf sich nie ändern, da gedruckte Karten nicht nachträglich angepasst werden können.

## Redirect-Tabellen-Architektur

Die Redirect-Tabelle ist eine einfache Schlüssel-Wert-Zuordnung: `card_id → target_url`. Die Ziel-URL kann auf die aktuelle Plattformseite, eine LMS-Seite oder eine externe Ressource zeigen und kann bei Bedarf geändert werden. Die Karten-ID selbst ist unverfänderlich. Der Service ist ein leichtgewichtiger Dienst (z. B. ein einfaches PHP-Skript oder eine Node.js-Anwendung), der ohne Datenbank-Joins auskommt und extrem schnell antworten muss (Ziel: &lt;50 ms).

## Versionsfähige URLs

Falls sich Karteninhalte grundlegend ändern (neue Version einer Karte), kann die Ziel-URL auf eine versionierte Kartenansicht zeigen (z. B. `/oc/primaerer-alkohol/v2`). Die Redirect-Tabelle enthält ein optionales `version`-Feld, das manuell gepflegt wird. Standardmäßig zeigt der Redirect immer auf die neueste Version.

## Monitoring und Fallback

Scan-Ereignisse werden optionalprotokolliert (anonymisiert, ohne personenbezogene Daten): Zeitstempel, Karten-ID, Nutzeragent (Browser/Scanner), geografische Region (nur Land). Bei unbekannten Karten-IDs gibt der Redirect-Service einen HTTP-404 zurück und zeigt eine freundliche Fehlerseite mit Hinweis auf die Plattform. Das Monitoring überwacht die Verfügbarkeit des Redirect-Service und alarmiert bei Ausfall.
