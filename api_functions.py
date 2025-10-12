import requests


def get_access_token(client_id, client_secret):
    TOKEN_URL = "https://accounts.spotify.com/api/token"

    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    headers = {
        "Content_Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(TOKEN_URL, data=data, headers=headers)

    # se status=ok -- retorna o token
    if response.status_code == 200:
        access_token = response.json()["access_token"]

        return access_token

    # caso contrário -- retorna o Erro
    return f"Erro: {response.text}"


def get_artist_name_by_id(artist_id, access_token):
    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"

    headers = { "Authorization": f"Bearer  {access_token}" }

    response = requests.get(artist_url, headers=headers)

    # se status=ok -- retorna o nome do artista
    if response.status_code == 200:
        artist_name = response.json().get('name')

        return artist_name

    # caso contrário -- retorna o Erro
    return f"Erro: {response.text}"


def search_for_tracks(track_alias, access_token, limit=5, offset=0):
    search_url = f'https://api.spotify.com/v1/search'

    headers = { "Authorization": f"Bearer {access_token}" }

    params = {
        "q": f"track:{track_alias}",
        "type": "track",
         "limit": f"{limit}",
         "offset": f"{offset}" 
    }

    response = requests.get(search_url, params=params, headers=headers)

    # se satus=ok -- retorna um dicionario de sugestões
    if response.status_code == 200:
        track_suggestions = response.json()

        return track_suggestions.get('tracks', {}).get('items', [])

    # caso contrário -- retorna o Erro
    return f"Erro: {response.text}"


# fazer a função pra quando o usuário escolher uma das sugestões ele pegar o id 
#  do artista pelo nome
# def get_artist_id_by_name(artist_name, access_token):

