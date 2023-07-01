# -*- coding: utf-8 -*-
import os
from log_tif import raster_log_db
from extract_file import extract_file
from image_creation import display_image
from data_download import data_download
from env_test import get_user_input


print("##############################")
print("1. Speicherort festlegen")
print("##############################")

# Speicherort wird ermittelt
user_save = get_user_input()


print("##############################")
print("2. Start des Daten Downloads")
print("##############################")

# Download der Daten
out_save = data_download(user_save)


print("##############################")
print("3. Start der Daten Extraktion")
print("##############################")

# extrahieren der Dateien
extracted_file = extract_file(out_save, user_save)


print("##############################")
print("4. Berechnung der dB-Rückstreuung")
print("##############################")

# Berechnung der dB-Rückstreuung
i = 0
db_converted_list = []
# Berechnung mehrer potentieller tif-Dateien in der Eingabedatei
for entry in extracted_file:
    if extracted_file[i].endswith(".tif") and not extracted_file[i].startswith("__"):
        db_input = os.path.join(user_save, entry)
        print("Datei zum Umwandeln gefunden", db_input)
        i = i + 1
        db_output = raster_log_db(db_input, user_save)
        db_converted_list.append(db_output)
        print("Liste der erstellten Dateien:", db_converted_list)
    else:
        print("Nicht umwandelbare Datei: ", entry)
        i = i + 1


print("##############################")
print("5. Darstellung des Untersuchungsgebietes")
print("##############################")

# Erstellung der Plots und Karten für alle tif-Dateien, die in dB umgewandelt wurden
for entry in db_converted_list:
    display_image(entry, user_save)


print("##############################")
print("Programm beendet")
print("##############################")
