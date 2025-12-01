import asyncio
import os
from contextlib import asynccontextmanager
from typing import Union

import requests
from api.api_functions import *
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.spotify_token = get_access_token(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET
    )

    print("token adquirido com sucesso!")

    yield

    print("servidor encerrado... tenha um bom dia!")


async def refresh_token(app: FastAPI):
    while True:
        await asyncio.sleep(3300)

        app.state.spotify_token = get_access_token(
            client_id=CLIENT_ID, client_secret=CLIENT_SECRET
        )

        print("spotify token renovado!")


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou "http://localhost:3000"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/token")
def get_token(request: Request):
    return request.app.state.spotify_token


@app.get("/search")
def search_musics(q: str, request: Request):
    access_token = request.app.state.spotify_token

    return search_for_tracks(track_alias=q, access_token=access_token)
