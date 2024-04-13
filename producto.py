import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('La Solicitud Exitosa')
    print("Los Datos son: ", data.get("icon_url"))
    print("Los Datos son: ", data.get("id"))
    print("Los Datos son: ", data.get("url"))
    print("Los Datos son: ", data.get("value"))
else:
    print("error en la solicitud: ", response.text)
