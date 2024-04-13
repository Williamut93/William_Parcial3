import requests
import pywhatkit

def obtener_frase_por_id(id):
    url = "http://127.0.0.1:5000/tasks"
    try:
        response = requests.get(url)
        data = response.json()
        for frase in data:
            if frase["id"] == id:
                return frase["frase"]
        return "No se encontró una frase."
    except Exception as e:
        return f"Error: {e}"

def main():
    try:
        id = int(input("Ingresa el ID del 1 al 3: "))
        frase = obtener_frase_por_id(id)
        pywhatkit.sendwhatmsg_instantly("+5214442883246", frase)
        print("Mensja Enviado")

    except ValueError:
        print("Por favor, ingresa otro nuemero.")

if __name__ == "__main__":
    main()
