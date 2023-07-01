# -*- coding: utf-8 -*-
import sys


def get_user_input():
    """
   Diese Funktion überprüft, ob das Skript über das Terminal mit extra Argument oder über eine IDE gestartet wurde.

   Returns:
       str: Der vom Benutzer eingegebene Pfad, wo die Datei gespeichert werden soll.
   """
    if len(sys.argv) > 1:

        # Das Skript wurde über das Terminal mit Argument gestartet
        user_save = sys.argv[1]
        print(user_save)
        return user_save
    else:

        # Das Skript wurde in einer IDE gestartet oder ohne Argument im Terminal
        user_save = input(
            "Bitte geben Sie den Pfad ein wo die Datei gespeichert werden soll: ")
        print(user_save)

        # Rückgabe des eingegebenen Speicherortes
        return user_save


# Funktion ausführen
# muss nur geändert werden, wenn man das Skript unabhängig von main.py ausführt
if __name__ == '__main__':
    get_user_input()
