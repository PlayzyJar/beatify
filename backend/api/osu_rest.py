import os
from typing import Dict, List, Optional

import requests
from dotenv import load_dotenv
from ossapi import Ossapi

load_dotenv()

OSU_CLIENT_ID = os.getenv("OSU_CLIENT_ID")
OSU_CLIENT_SECRET = os.getenv("OSU_CLIENT_SECRET")

# create a new client at https://osu.ppy.sh/home/account/edit#oauth
api = Ossapi(OSU_CLIENT_ID, OSU_CLIENT_SECRET)

# see docs for full list of endpoints
print(api.user("PlayzyART").id)
print(api.user(29214575, mode="osu").username)
print(api.beatmap(221777).id)

def get_osu_access_token(client_id: str, client_secret: str) -> Optional[str]:
    """
    Obtains a OSU Client Credentials access token.
    Returns the token string on success or None on failure.
    """

    TOKEN_URL = "https://osu.ppy.sh/oauth/token"

    try:
        resp = requests.post(
            TOKEN_URL,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={
                "scope": "public",
                "grant_type": "client_credentials",
                "client_id": client_id,
                "client_secret": client_secret
            },
            timeout=10
        )

        resp.raise_for_status()

        body = resp.json()

        return body.get("access_token")

    except Exception as exc:
        # Simple logging for development. In production use structured logging.
        print("[api_functions.get_osu_access_token] error:", exc)
        return None


def search_osu_beatmap(query: str, api: Ossapi) -> List[Dict]:
    """
    Endpoint de busca de beatmaps do osu!.
    """

    results = set(api.search_beatmapsets(query=query, mode=0))

    print(results)

    return api.search_beatmapsets(query=query, mode=0)
