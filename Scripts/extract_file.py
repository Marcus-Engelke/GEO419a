# -*- coding: utf-8 -*-
import zipfile
import os


def extract_file(file, extract_save_location):
    """
    Extrahiert Dateien aus einer Zip-Datei und speichert sie an einem angegebenen Speicherort.

    Args:
        file (str): Der Pfad zur Zip-Datei, aus der extrahiert werden soll.
        extract_save_location (str): Der Speicherort, an dem die extrahierten Dateien gespeichert werden sollen.
            Der Speicherort sollte als absoluter Pfad angegeben werden.
            Beispiel für Windows: 'C:\\path\\to\\extract'

    Returns:
        list: Eine Liste der extrahierten Dateien.
    """
    # Überprüfen, ob das Verzeichnis bereits existiert
    if not os.path.exists(extract_save_location):

        # Verzeichnis erstellen
        os.makedirs(extract_save_location)
        print("Verzeichnis wurde erstellt:", extract_save_location)

    else:
        print("Verzeichnis ausgewählt:", extract_save_location)
    while True:
        if file.endswith(".zip"):

            # Zip-Datei öffnen
            zip_file = zipfile.ZipFile(file, 'r')

            # Liste aller Dateien die in der Datei sind
            file_list = zip_file.namelist()

            # iterieren über jeden Eintrag in der Liste
            for entry in file_list:

                # Pfad zu der jeweiligen potentiell extrahierten Datei wird erstellt
                missing_file = os.path.join(extract_save_location, entry)

                # Überprüfen ob die Datei bereits extrahiert wurde
                if not os.path.exists(missing_file):
                    print("Fehlende Datei", missing_file)

                    # extrahieren der Datei
                    zip_file.extract(entry, extract_save_location)

                else:
                    print(entry, "wurde bereits extrahiert")

            zip_file.close()
            print("Extraktions-Funktion beendet.")

            # Rückgabe aller potentiell extrahierbaren Dateien
            return file_list
            break

        else:
            print("Die Datei endet nicht in .zip und kann somit nicht extrahiert werden.")
            file = input("Bitte eine gültige zip-Datei angeben: ")


# Funktion mit Speicherort und Eingabedatei als Parameter ausführen
# Format des Parameters in Windows: C:\\path\\to\\file
# muss nur geändert werden, wenn man das Skript unabhängig von main.py ausführt
if __name__ == '__main__':
    extract_file("C:\\path\\to\\file\\file.zip", "C:\\path\\to\\another\\file")
