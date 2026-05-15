# ChemBioMed Cards – Landingpage

## Übersicht

Diese Landingpage ist die öffentliche Eingangsseite des ChemBioMed-Cards-Projekts. Sie stellt das Lernkarten-System, die sechs Fachmodule und die Kernfunktionen der Plattform vor.

## Technologie

Die Seite ist als vollständige HTML5-Datei ohne externe Abhängigkeiten realisiert. Alle CSS-Stile sind direkt eingebettet (`<style>`-Block im `<head>`). Es werden keine externen Stylesheets, JavaScript-Frameworks, Fonts oder CDN-Ressourcen geladen. Die Seite ist damit vollständig offline-fähig und benötigt keine Build-Pipeline.

## Deployment

Die Datei `index.html` kann direkt auf jedem Webserver oder Static-Hosting-Dienst bereitgestellt werden. Für die initiale Bereitstellung auf dem ATMED-core-Server genügt das Kopieren der Datei in das Webroot-Verzeichnis. Eine spätere Migration zu einem dedizierten Server oder einem CDN ist ohne Änderungen an der Datei möglich.

## Anpassung

- Farben und CSS-Variablen sind am Dateianfang im `:root`-Block definiert.
- Modul-Informationen befinden sich im Abschnitt `Sechs Module – ein System`.
- Der CTA-Button `Zur Plattform` sollte auf die echte Plattform-URL verlinkt werden, sobald diese verfügbar ist.
- Kein DHBW-Branding, keine Partnerschaftshinweise ohne explizite schriftliche Vereinbarung.
