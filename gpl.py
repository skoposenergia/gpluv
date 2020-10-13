import json
import requests

global url_base
url_base = "https://pluvia.app"

def auth_session():
    

    url = url_base + "/api/token"

    headers = {
        "content-type": "application/x-www-form-urlencoded"
    }


    data = {
        "grant_type": "password",
        "username" : "daniel.mazucanti",
        "password" : "D4ni3lM@zucant1!"
    }

    token_resp = requests.post(
        url, headers=headers, data=data, verify=True)
    token_json = token_resp.json()
    token =  token_json["access_token"]
    return token


token = auth_session()

url = url_base + "/api/valoresParametros/mapas"

headers = {
        'Authorization': 'Bearer ' + token,
        "Content-Type": "application/json"
    }

mapas = requests.get(url, headers=headers, verify=True)
mapas = mapas.json()
for mapa in mapas:
    with open('mapa%s.json' % mapa['id'], 'w') as m:
        val = json.dumps(mapa)
        m.write(val)

url = url_base + "/api/valoresParametros/modelos"

modelos = requests.get(url, headers=headers, verify=True)
modelos = modelos.json()
for modelo in modelos:
    with open('modelo%s.json' % modelo['id'], 'w') as m:
        val = json.dumps(modelo)
        m.write(val)