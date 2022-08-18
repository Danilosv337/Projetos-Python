import eyed3
import os



def organizar(caminho):
    lista_arquivos = os.listdir(caminho)
    for musicas in lista_arquivos:
        if ".mp3" in musicas:
            print(musicas)
            audio = eyed3.load(f"{caminho}/{musicas}")
            if not audio.tag:
                audio.initTag()
            audio.tag.title = musicas.replace(".mp3","")
            audio.tag.save(version=(2,3,0))
            print(audio.tag.title)

