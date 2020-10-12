special_characters = ["\\","/",":","*","?",'"',"<",">","|",]

artista = 'songs: ohia'

for char in artista:
    print(char)
    if char in special_characters:
        print(char + "se encuentra en List")
        print("artista antes: "+ artista)
        artista = artista.replace(char,'')
        print("artista despues: "+ artista)

print("artista fuera del caos: "+ artista)
