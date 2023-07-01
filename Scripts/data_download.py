# -*- coding: utf-8 -*-
import urllib.request
import os
import requests


def data_download(save_location):
    """
    Lädt eine Datei von einer URL herunter und speichert sie an dem angegebenen Speicherort.

    Args:
        save_location (str): Der Speicherort, an dem die heruntergeladene Datei gespeichert werden soll.
            Der Speicherort sollte als absoluter Pfad angegeben werden.
            Beispiel für Windows: 'C:\\path\\to\\file'

    Returns:
        str: Der vollständige Pfad zur heruntergeladenen Datei.

    Raises:
        requests.exceptions.RequestException: Eine Ausnahme wird ausgelöst, wenn ein Fehler beim Aufrufen der URL auftritt.
    """
    # Überprüfen, ob das Verzeichnis bereits existiert
    if not os.path.exists(save_location):

        # Verzeichnis erstellen
        os.makedirs(save_location)
        print("Verzeichnis wurde erstellt:", save_location)

    else:
        print("Verzeichnis ausgewählt:", save_location)

    # Schleife die den URL input solange erfragt bis passende Daten vorhanden sind
    while True:

        # Eingabe der URL wird vom Nutzer erwartet
        url = input(
            "Geben Sie die URL der zip-Datei ein (leer lassen wenn die Standard Datei gedownloaded werden soll): ")

        # wenn der Nutzer keine URL eingiebt wird die Standard-URL gedownloaded
        if url == "":

            # Standard-URL --> kann geändert werden wenn eine andere Datei als Standard-URL gebraucht wird
            url = "https://upload.uni-jena.de/data/649ad4879284a9.22886089/GEO419A_Testdatensatz.zip"
            print("Es wird die Standard Datei gedownloaded.", url)
            break
        else:

            # überprüfen ob eingegebene URL die richtigen Anforderungen besitzt
            if url.endswith(".zip"):
                if url.startswith("https://"):
                    try:
                        response = requests.head(url, timeout=5)

                        # Wirft eine Exception, wenn ein Fehlercode zurückgegeben wird
                        response.raise_for_status()
                        if response.status_code != 200:
                            print(
                                "Ungültiger Pfad. Der Pfad ist nicht online verfügbar")
                        else:
                            print("Der Download der zip-Datei wird durchgeführt")
                            break
                    except requests.exceptions.RequestException as e:
                        print("Fehler beim Aufrufen der URL:", e)
                else:
                    print("Ungültiger Pfad. Der Pfad muss mit 'https://' beginnen.")
            else:
                print("Ungültiger Pfad. Der Pfad muss mit '.zip' enden.")

    # Dateiname wird aus der URL entnommen
    name = url.rsplit("/", 1)[-1]

    # Speicherort wird aus Endung der URL und dem angegebenen Ordner erstellt
    out_save = os.path.join(save_location, name)

    # Überprüfen ob Datei bereits vorhanden ist
    if not os.path.exists(out_save):

        # Datei downloaden
        urllib.request.urlretrieve(url, out_save)
        print("Datei wurde erfolgreich gedownloaded nach:", out_save)

    else:
        print("Die Datei oder eine Datei mit dem Namen: '" +
              out_save + "' exisitiert bereits. Download nicht durchgeführt.")

    print("Download-Funktion beendet.")

    # Rückgabe des Speicherortes der heruntergeladenen Datei
    return out_save


# Funktion mit Speicherort als Parameter ausführen
# Format des Parameters in Windows: C:\\path\\to\\file
# muss nur geändert werden, wenn man das Skript unabhängig von main.py ausführt
if __name__ == '__main__':
    data_download("C:\\path\\to\\file")
