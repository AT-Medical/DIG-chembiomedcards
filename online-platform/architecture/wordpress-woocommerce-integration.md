# WordPress/WooCommerce-Integration

## WooCommerce als initialer E-Commerce-Layer

In der ersten Betriebsphase übernimmt WooCommerce die Funktion der E-Commerce-Schicht: Produkte entsprechen Kartenpaket-Lizenzen, der Checkout-Prozess nutzt den Standard-WooCommerce-Zahlungsfluss. Jedes Paket (z. B. „OC Grundlagenpaket 1“) ist als WooCommerce-Produkt angelegt. Nach dem Kauf wird automatisch ein Lizenzschlüssel generiert und per E-Mail zugestellt.

## Bestellabwicklungs-Flow

Der vollständige Ablauf lautet: (1) Nutzer wählt ein Paket und schließt den Checkout ab. (2) WooCommerce löst nach erfolgreicher Zahlung einen Webhook („order\_completed“) aus. (3) Das Lizenzschlüssel-Plugin generiert einen eindeutigen Schlüssel und speichert ihn in der Datenbank. (4) Der Schlüssel wird per E-Mail an den Käufer gesendet. (5) Der Käufer aktiviert den Schlüssel in seinem Plattform-Konto. (6) Das Paket wird freigeschaltet und der Nutzer hat Zugriff auf die enthaltenen Karten.

## Migrations- und Entkopplungsstrategie

WooCommerce ist ein Einstieg, keine langfristige Lösung. Die Entkopplung beginnt mit der Abstraktion der Lizenzlogik hinter einer eigenen API, sodass WooCommerce nur noch als „Trigger“ fungiert. Mittelfristig kann WooCommerce durch ein anderes Zahlungssystem (z. B. Stripe Checkout, LemonSqueezy) ersetzt werden, ohne dass bestehende Lizenzen oder Nutzerdaten verloren gehen. Alle Lizenz- und Nutzerdaten werden in einer eigenen Tabelle (nicht in der WooCommerce-Datenbankstruktur) gespeichert, um die Migration zu erleichtern.
