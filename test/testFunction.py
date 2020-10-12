import os
import shutil
# Implementación de Tkinter
from tkinter import Tk
from tkinter.filedialog import askdirectory

Tk().withdraw()
basepath = askdirectory( )

print(basepath)
# basepath = r"C:\Users\Bastian\Desktop\testMp3"

# pass raw artist_dir and file names
artist_directory = os.path.join(basepath, "Muse")
tracks_path = [os.path.join(basepath, "Muse - Micro Cuts.mp3"),
               os.path.join(basepath, "Muse - Megalomania.mp3"),
               os.path.join(basepath, "Muse - Futurism.mp3"),
               os.path.join(basepath, "Muse - Screenager.mp3"),
               ]


def moveMp3Files(artist_directory, tracks_path):
    if os.path.exists(artist_directory):
        for track in tracks_path:
            try:
                shutil.move(track, artist_directory)
                print(
                    "directorio ya existe, he pasado por aca para mover archivo " + track)
            except shutil.Error as e:
                print(e)
    else:
        print(
            "No he encontrado un directorio, intentare crear uno y terminar mi trabajo...")
        os.mkdir(artist_directory)
        return moveMp3Files(artist_directory, tracks_path)


moveMp3Files(artist_directory, tracks_path)
