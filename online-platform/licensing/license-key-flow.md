# Lizenzschlüssel-Flow

## Normaler Ablauf (Happy Path)

Der vollständige Aktivierungsfluss verläuft in sechs Schritten: (1) **Kauf**: Nutzer wählt ein Paket in WooCommerce und schließt den Checkout mit Zahlung ab. (2) **Schlüsselgenerierung**: Nach Zahlungsbestätigung generiert das System automatisch einen eindeutigen, kryptografisch sicheren Lizenzschlüssel (Format: `XXXX-XXXX-XXXX-XXXX`, Base-32). (3) **E-Mail-Zustellung**: Der Schlüssel wird zusammen mit Aktivierungsanleitung und Nutzungsbedingungen an die Kauf-E-Mail-Adresse gesendet. (4) **Kontoerstellung oder Anmeldung**: Der Nutzer erstellt ein Plattform-Konto oder meldet sich bei einem bestehenden Konto an. (5) **Schlüsselaktivierung**: Der Schlüssel wird im Account-Bereich („Lizenz aktivieren“) eingegeben und validiert. (6) **Paketzugang**: Das Paket wird freigeschaltet; der Nutzer hat sofortigen Zugriff auf alle enthaltenen Karten.

## Fehlerfälle

Folgende Fehlerzustände werden behandelt: **Ungültiger Schlüssel** – Fehlermeldung mit Hinweis auf Support-Kontakt. **Bereits aktiviert** – Anzeige des Kontos, auf dem der Schlüssel aktiviert ist; Support-Option für Gerätewechsel. **Abgelaufener Schlüssel** (nur Zeitlimitierte Schlüssel, z. B. Demo-Schlüssel) – Hinweis auf Ablaufdatum und Kaufmöglichkeit. **Doppelte Aktivierung** – System verweigert zweite Aktivierung auf anderem Konto; ein Admin-Override ist möglich.

## Schlüsselmanagement

Generierte Schlüssel werden in der Datenbank mit folgenden Feldern gespeichert: `key_id`, `key_hash` (SHA-256, nicht Klartext), `package_id`, `created_at`, `activated_at`, `user_id` (nach Aktivierung), `status` (active, expired, revoked). Der Klartext-Schlüssel wird nur einmalig bei der Generierung angezeigt und nicht dauerhaft gespeichert.
