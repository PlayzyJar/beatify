from typing import Union
from fastapi import FastAPI
import requests
from api_functions import * 
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# id do artista = ex.: king gnu
# artist_id = "6wxfx1yhyqjCPYwwxJktR2"

# pega o token de acesso
access_token = get_access_token(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# captura informações de um artista usando o token (King Gnu = 6wxfx1yhyqjCPYwwxJktR2)
# artist_name = get_artist_name_by_id(artist_id=artist_id, access_token=access_token)

# print(f"Nome do Artista pelo id: {artist_name}")

while True:
    print("Pesquisar ('' + ENTER para SAIR):")

    track_alias = str(input("Nome da música: "))
    # artist_alias = str(input("Nome do artista: ")) 

    if track_alias == "":
        break

    track_suggestions = search_for_tracks(track_alias, access_token, limit=5)

    print("Músicas sugeridas:")

    for track in track_suggestions:
        print(f"{track['name']} of {track['album']['name']}")

print("Programa Encerrado... Tenha um bom dia!")

