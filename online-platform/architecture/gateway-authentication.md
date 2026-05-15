# Gateway-Authentifizierung

## Aktueller Stand

In der initialen Phase werden WooCommerce-Nutzerkonten als Authentifizierungsgrundlage verwendet. Jeder Nutzer, der ein Lizenzpaket erwirbt, erhält ein Konto auf der Plattform. Die Zugriffskontrolle auf einzelne Kartenpakete erfolgt über eine eigene Tabelle, die Nutzer-IDs mit freigeschalteten Paket-IDs verknüpft. Dieses Modell ist einfach zu implementieren, aber nicht beliebig skalierbar.

## Migrationsweg zu Gateway-Auth

Mittelfristig soll ein zentraler Authentifizierungs-Gateway eingeführt werden, der Single Sign-On (SSO) für alle Plattformkomponenten ermöglicht. Der Gateway validiert Nutzersitzungen und gibt JWT-Token aus, die von allen nachgelagerten Diensten (Kartenplattform, QR-Redirect, LMS) zur Zugriffskontrolle genutzt werden. Bestehende WooCommerce-Konten werden in das neue System migriert; Nutzer müssen sich einmalig neu authentifizieren.

## JWT- und Session-Management

JWT-Token werden mit einer kurzen Gültigkeit (z. B. 15 Minuten) ausgestellt und können über Refresh-Tokens erneuert werden. Die Token enthalten Nutzer-ID, E-Mail und eine Liste freigeschalteter Pakete. Refresh-Tokens werden serverseitig invalidiert, wenn eine Lizenz abläuft oder ein Konto gesperrt wird. Eine spezifische SSO-Implementierung (z. B. Keycloak, Auth0 oder ein selbst gehosteter OAuth2-Server) wird erst nach Abschluss der initialen Betriebsphase festgelegt.

## Rückwärtskompatibilität

Die Migration zur Gateway-Authentifizierung muss rückwärtskompatibel sein: Bestehende Sitzungen bleiben bis zu ihrem Ablauf gültig. Die API-Endpunkte unterstützen während des Übergangszeitraums sowohl das alte (Cookie-basierte WooCommerce-Session) als auch das neue (JWT-basierte) Authentifizierungsverfahren.
