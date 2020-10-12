import os
import shutil
import string
from tinytag import TinyTag, TinyTagException
from tkinter import Tk
from tkinter.filedialog import askdirectory
import msvcrt as m

# Directorio Base
default_basepath = r"C:\Users\Bastian\Music"
basepath = default_basepath


def mainManageFiles(basepath):
    artista = string.capwords(input('Ingrese Nombre de Artista: '))
    print("----------------------------------\n Buscando...\n----------------------------------\n")
    tracks_path = []
    count = 0

    for fname in os.listdir(basepath):

        path = os.path.join(basepath, fname)
        # si es un directorio, skip, sin antes verificar si ya existe un directorio sobre arista
        if os.path.isdir(path):
            continue

        if fname.endswith(".mp3"):
            try:
                temp_track = TinyTag.get(path)
                # Si albumartist está vacio (false) continue
                if not temp_track.albumartist:
                    continue
                else:
                    # Si encuentra un archivo con artista idéntico, añadir path a tracks_path
                    if temp_track.albumartist.lower() == artista.lower():
                        count += 1
                        if not temp_track.title:
                            print(count, '| ' + fname)
                        else:
                            print(count,  '| ' + temp_track.albumartist +
                                  ' - ' + temp_track.title)
                        tracks_path.append(path)
            except TinyTagException:
                print("TinyTag Error")

    print("----------------------------------\n Búsqueda Terminada\n----------------------------------\n")
    print("Se ha encontrado ", count, " canciones del AlbumArtist '"+artista+"'")

    # Si encontró canciones entonces moverlas
    if count > 0:
        print("╔═════════════════════════════════════════════════════════════════════════════════════════════╗")
        print("╟---------------------------------- Moviendo Archivos... -------------------------------------╢")
        print("╚═════════════════════════════════════════════════════════════════════════════════════════════╝")
        try:
            artist_dir = os.path.join(basepath, artista)
            # Mover Archivos
            moveMp3Files(artist_dir, tracks_path)
            print("\n╔═════════════════════════════════════════════════════════════════════════════════════════════╗")
            print("╟---------------------------------- Ejecución Exitosa!... ------------------------------------╢")
            print("╚═════════════════════════════════════════════════════════════════════════════════════════════╝")
        except shutil.Error() as e:
            print(e)
    else:
        print("No se ha encontrado canciones del AlbumArtist '" +
              artista+"'")

    print("Presione una tecla para continuar")
    wait()


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
        print("Se ha creado artist_dir: "+artist_directory+"\n")
        return moveMp3Files(artist_directory, tracks_path)


def changeBasePath():
    # Cerrar ventana Tkinter y Seleccionar Directorio
    Tk().withdraw()
    basepath = askdirectory()
    return basepath


# Presionar tecla para continuar
def wait():
    m.getch()


# Mostrar lista con artistas
def artistList(basepath):
    listOfArtists = []
    for fname in os.listdir(basepath):
        path = os.path.join(basepath, fname)
        if os.path.isdir(path):
            continue
        if fname.endswith(".mp3"):
            try:
                temp_track = TinyTag.get(path)
            # Si albumartist está vacio (false) continue
                if not temp_track.albumartist:
                    continue
                else:
                    if temp_track.albumartist.lower() not in listOfArtists:
                        listOfArtists.append(temp_track.albumartist.lower())
            except TinyTagException:
                print("TinyTag Error")

    return listOfArtists


def formattedArtistList(basepath):
    artistList_string = ["%i: %s" % (index, value)
                         for index, value in enumerate(artistList(basepath))]
    artistList_formatted = "\n".join(artistList_string)

    return artistList_formatted


# Menú
continuar = True
while(continuar):
    os.system('cls')
    print("╔════════════════════════════════════════════════════════════════╗")
    print("╟════════════════════════ Menú Principal ════════════════════════╢")
    print("╟────────────────────────────────────────────────────────────────╢")
    print("╟──────────────────── 1. Organizar Canciones ────────────────────╢")
    print("╟──────────────── 2. Seleccionar Directorio Base ────────────────╢")
    print("╟─────────────────────────── 3. Salir ───────────────────────────╢")
    print("╚════════════════════════════════════════════════════════════════╝")
    print("Directorio Base: "+basepath)
    try:
        op = int(input("Ingrese Número de Opción: "))
        if op == 1:
            os.system('cls')
            print("╔════════════════════════════════════════════════════════════════╗")
            # Si basepath, por alguna razón, está vacío asignarle el default
            if not basepath:
                basepath = default_basepath
            print(formattedArtistList(basepath))
            mainManageFiles(basepath)
        elif op == 2:
            try:
                basepath = changeBasePath()
                print("Presione una tecla para continuar")
                wait()
            except:
                print("Ha ocurrido un problema al seleccionar el directorio base")
        elif op == 3:
            os.system('cls')
            print("Mr. "+os.getlogin()+"... I don't feel so good...")
            continuar = False
    except:
        os.system('cls')
        print("Por favor ingrese una opción válida...")
        wait()
