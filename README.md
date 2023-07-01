# GEO419A - Prozessierung von Sentinel-1 Daten
Dieses Programm basiert auf einem Projekt des Moduls "GEO 419A - Modulare Programmierung in der Fernerkundung: Dateninterpretation" im M.Sc Geonformatik an der Friedrich-Schiller-Universität und wurde entwickelt von Johannes Senf und Marcus Engelke.
Es beinhaltet Funktionen / Algorithmen zum Download, Entpacken und zur Prozessierung (logarithmische Skalierung der Rückstreuintensität) von Sentinel-1 Bildern (weitere Radardaten sollten auch funktionieren). Nachfolgend ist eine detailliertere Übersicht:

- Benutzerabfrage zum Speicherort und Downloadlink der zip-Datei
- Download und Entpacken der zip in das gewählte Verzeichnis
- Prozessierung der entpackten Radardaten (logarithmische Skalierung)
- Speichern und Darstellung des Ergebnis (ohne Ausreißer und Extremwerte)
- Überprüfung, ob die Dateien schon vorhanden sind (Überspringen der jeweiligen Schritte)
- Programm über IDE und Kommandozeile ausführbar

# Environment
Über Anaconda kann das Environment für dieses Projekt erstellt werden. Dort werden alle Pakete und Abhängigkeiten automatisch installiert (Anacononda Prompt). 

```conda env create -f environment.yml```

