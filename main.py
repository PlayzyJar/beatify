from typing import Union
from fastapi import FastAPI, Request
import requests
from api_functions import * 
from dotenv import load_dotenv
import os
import asyncio
from contextlib import asynccontextmanager

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.spotify_token = get_access_token(
        client_id=CLIENT_ID, 
        client_secret=CLIENT_SECRET
    )

    print("token adquirido com sucesso!")

    yield

    print("servidor encerrado... tenha um bom dia!")


async def refresh_token(app: FastAPI):
    while True:
        await asyncio.sleep(3300)
        
        app.state.spotify_token = get_access_token(
            client_id=CLIENT_ID, 
            client_secret=CLIENT_SECRET
        )

        print("spotify token renovado!")


app = FastAPI(lifespan=lifespan)

@app.get("/token")
def get_token(request: Request):
    return (request.app.state.spotify_token)



