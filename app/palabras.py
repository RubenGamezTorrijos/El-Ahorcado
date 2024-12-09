import json
import os

def cargar_palabras():
    archivo = os.path.join(os.path.dirname(__file__), '../datos/animales.json')
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data['animales']
    except FileNotFoundError:
        print("El archivo de animales no se encuentra.")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return []
