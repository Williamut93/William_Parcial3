import requests
url = "https://jsonplaceholder.typicode.com/posts/8"
response = requests.get(url)
if response.status_code == 200:
     data = response.json() 
     print('Exito')
     print("Datos de la API: ", data)
else:
    print("Error: ", response.text)
