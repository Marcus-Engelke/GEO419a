# -*- coding: utf-8 -*-
import rasterio
import numpy as np
import os


def raster_log_db(input_file, output_file):
    """
    Führt eine logarithmische Skalierung der Rückstreuintensität eines Rasterbildes durch und speichert das Ergebnis in einer neuen Datei.

    Args:
        input_file (str): Der Pfad zur Eingabedatei (Rasterbild), für das die logarithmische Skalierung durchgeführt werden soll.
        output_file (str): Der Pfad zur Ausgabedatei, in dem das Ergebnis der logarithmischen Skalierung gespeichert werden soll.
    """

    # Überprüfen, ob das Verzeichnis bereits existiert
    if not os.path.exists(output_file):

        # Verzeichnis erstellen
        os.makedirs(output_file)
        print("Verzeichnis wurde erstellt:", output_file)

    else:
        print("Verzeichnis ausgewählt:", output_file)

    # Erzeugung des zu erstellenden Dateinamen aus der Eingabedatei
    save_name = input_file.replace("\\", "/")
    save_name = save_name.split("/")[-1]
    save_name = save_name.split(
        ".")[-2] + "_modified." + save_name.split(".")[-1]
    output_file = os.path.join(output_file, save_name)

    # Überprüfen ob die Datei bereits vorhanden ist
    while True:
        if input_file.endswith(".tif"):
            if not os.path.exists(output_file):
                print("Start der logarithmischen Skalierung der Rückstreuintensität")

                # Rasterdatei öffnen
                dataset = rasterio.open(input_file)

                # Lese den Rasterdaten-Array des ersten Bands
                band_number = 1
                band_data = dataset.read(band_number)

                # Maske die TRUE für alle Werte die nicht 0 sind einnimmt
                valid_mask = band_data != 0

                # Werte die Null sind werden durch NaN ersetzt
                band_data_valid = np.where(valid_mask, band_data, np.nan)

                # Berechne den Logarithmus der Pixelwerte und multipliziere mit 10
                result = 10 * np.log10(band_data_valid)

                # Schreibe das Ergebnis in eine neue Datei
                with rasterio.open(output_file, 'w', **dataset.meta) as dst:

                    # Schreibe das Ergebnis in das erste Band
                    dst.write(result, indexes=1)

                # Datei schließen
                dataset.close()
                print("Logarithmischen Skalierung abgeschlossen.")

                # Rückgabe des Speicherortes der skalierten Datei
                return (output_file)
                break

            else:
                print("Eine Datei mit dem gleichen Namen ist bereits vorhanden.")
                print("Logarithmische Skalierung wird nicht durchgeführt.")

                # Rückgabe des Speicherortes der skalierten Datei
                return (output_file)
                break
        else:

            # Anfordern einer neuen Datei, wenn die initiale Datei den Anforderungen nicht entspricht
            input_file = input(
                "Die Inputdatei ist keine tif-Datei. Wählen Sie eine neue Datei: ")

    print("Logarithmische Skalierungs-Funktion beendet.")


# Funktion mit Speicherort und Eingabedatei als Parameter ausführen
# Format des Parameters in Windows: C:\\path\\to\\file
# muss nur geändert werden, wenn man das Skript unabhängig von main.py ausführt
if __name__ == '__main__':
    raster_log_db("C:\\path\\to\\file\\file.tif",
                  "C:\\path\\to\\another\\file")
