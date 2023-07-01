# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import rasterio
import os
import numpy as np


def display_image(tif_path, map_save_location):
    """
   Zeigt ein Rasterbild anhand der angegebenen Datei.

   Args:
       input_file (str): Der Pfad zur Eingabedatei (Rasterbild), das angezeigt werden soll.
       map_save_location (str): Der Pfad zur Ausgabedatei, in dem die Karte gespeichert werden soll.
   """
    # Überprüfen, ob das Verzeichnis bereits existiert
    if not os.path.exists(map_save_location):

        # Verzeichnis erstellen
        os.makedirs(map_save_location)
        print("Verzeichnis wurde erstellt:", map_save_location)

    else:
        print("Verzeichnis ausgewählt:", map_save_location)

    # Erzeugung des zu erstellenden Dateinamen aus der Eingabedatei
    save_name = tif_path.replace("\\", "/")
    save_name = save_name.split("/")[-1]
    save_name = save_name.split(".")[-2] + "_map.png"
    print(save_name)
    save_name = os.path.join(map_save_location, save_name)
    print(save_name)

    # TIF-Bild öffnen
    with rasterio.open(tif_path) as src:

        # Georeferenzierungsinformationen abrufen
        transform = src.transform

        # Bild als Array einlesen
        data = src.read(1)

    # Berechnung der Prozentile für die Farbbegrenzung
    min_per = np.nanpercentile(data, 2)
    max_per = np.nanpercentile(data, 98)

    # Definiere die Größe der Abbildung
    dpi = 100

    # Setze die Auflösung auf 1080p
    fig = plt.figure(figsize=(1920/dpi, 1080/dpi), dpi=dpi)

    # Colormap definieren
    cmap = plt.cm.gray

    # Farbe für NaN-Werte festlegen
    cmap.set_bad('red', alpha=0.1)

    # Bild plotten
    plt.imshow(data, cmap=cmap, vmin=min_per, vmax=max_per,
               extent=[transform[2], transform[2] + transform[0] * src.width,
                       transform[5] + transform[4] * src.height, transform[5]])

    # Bildbeschriftungen einfügen
    plt.xlabel('Easting')
    plt.ylabel('Northing')
    plt.title('Radarbild')
    plt.colorbar(label='Rückstreuung in dB')

    # Achsenticklabels anpassen
    plt.ticklabel_format(axis='y', style='plain')

    # überprüfen ob die Karte bereits erzeugt wurde
    if not os.path.exists(save_name):

        # Speichere die Abbildung als PNG-Datei
        plt.savefig(save_name, dpi=dpi, bbox_inches='tight')
        print("Karte wurde erstellt")
    else:
        print("Eine Karte mit dem Namen existiert bereits")

    # anzeigen der Karte
    plt.show()


# Funktion mit Speicherort und Eingabedatei als Parameter ausführen
# Format des Parameters in Windows: C:\\path\\to\\file
# muss nur geändert werden, wenn man das Skript unabhängig von main.py ausführt
if __name__ == '__main__':
    display_image("C:\\path\\to\\file\\file.tif",
                  "C:\\path\\to\\another\\file")
