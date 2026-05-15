# QR-Code Druckspezifikation

## Mindestgröße und Platzierung

Der QR-Code auf jeder Karte hat eine Mindestgröße von **15×15 mm** im Fertigformat. Die empfohlene Größe beträgt 18×18 mm. Der QR-Code wird in der unteren rechten Ecke der Karte platziert, innerhalb der Sicherheitszone (mindestens 5 mm Abstand zur Schnittlinie). Ein Quiet-Zone-Abstand von mindestens **4 Modulen** (das entspricht 4 hellen Zellen am Rand des QR-Codes) muss eingehalten werden.

## Auflösung und Farbe

QR-Codes werden in **Schwarz auf Weiß** gedruckt. Eine Farbumkehr (weißer QR-Code auf dunklem Hintergrund) ist nicht erlaubt, da viele Scanner damit Probleme haben. Die Mindestauflösung für den QR-Code beträgt **300 dpi**; **600 dpi** wird empfohlen. Der QR-Code wird als Vektorgrafik (SVG oder eingebetteter Vektorpfad in PDF) geliefert, um Unschärfen durch Pixelierung zu vermeiden.

## Fehlerkorrektur und Testpflicht

Das Mindest-Fehlerkorrekturlevel ist **Level M** (15 % Wiederherstellungskapazität); **Level Q** (25 %) wird empfohlen, um die Lesbarkeit auch bei leichter Beschädigung der Karte sicherzustellen. Vor jedem Druckauftrag muss ein Testscan mit mindestens drei verschiedenen Scanner-Apps (z. B. iOS-Kamera, Android-Kamera, separater QR-Scanner) durchgeführt werden. Der Test muss bei unterschiedlichen Lichtsitu­ationen und mit einem Abstand von mindestens 20 cm erfolgen.

## QR-Redirect-URL

Die im QR-Code kodierte URL lautet: `https://chembiomed-cards.de/c/<card-id>`, z. B. `https://chembiomed-cards.de/c/oc-012`. Diese URL ist dauerhaft und darf nie geändert werden. Der QR-Code-Inhalt wird vor Produktionsstart anhand der finalen Karten-IDs aus dem Kartenregister (cards.master.csv) generiert.
