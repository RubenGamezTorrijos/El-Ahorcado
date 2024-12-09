import random
import matplotlib.pyplot as plt
import json  # Importamos la librería json

class Ahorcado:
    def __init__(self):
        # Cargar los animales desde el archivo JSON
        with open('/datos/animales.json', 'r') as archivo:
            data = json.load(archivo)
            self.palabras = data["animales"]  # Cargar la lista de animales
        
        self.dibujo = [
            '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
            '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
            '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
            '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
            '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
            '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
            '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''' 
        ]
        self.palabra = ""
        self.letras_adivinadas = []
        self.letras_erroneas = []
        self.estadisticas = {"Ganadas": 0, "Perdidas": 0}

    def iniciar_juego(self):
        while True:
            self.palabra = random.choice(self.palabras)
            self.letras_adivinadas = ['_'] * len(self.palabra)
            self.letras_erroneas = []

            print("\n¡Bienvenido al juego del Ahorcado!")
            self.jugar()

            if not self.pedir_reiniciar():
                print("¡Gracias por jugar! ¡Hasta pronto!")
                break

    def jugar(self):
        while True:
            self.mostrar_estado()
            letra = self.obtener_input()
            if letra in self.palabra:
                self.actualizar_letras_adivinadas(letra)
                if '_' not in self.letras_adivinadas:
                    print(f"¡Felicidades! Has adivinado el animal: {self.palabra}")
                    self.estadisticas["Ganadas"] += 1
                    break
            else:
                self.letras_erroneas.append(letra)
                if len(self.letras_erroneas) == len(self.dibujo) - 1:
                    self.mostrar_estado()
                    print(f"Has perdido. La palabra del animal era {self.palabra}")
                    self.estadisticas["Perdidas"] += 1
                    break

        self.mostrar_estadisticas()

    def mostrar_estado(self):
        print(self.dibujo[len(self.letras_erroneas)])
        print(' '.join(self.letras_adivinadas))
        print(f"Letras incorrectas: {', '.join(self.letras_erroneas)}")

    def obtener_input(self):
        while True:
            letra = input('¿Qué animal es? Elige una letra: ').lower()
            if letra.isalpha() and len(letra) == 1:
                if letra not in self.letras_erroneas and letra not in self.letras_adivinadas:
                    return letra
                else:
                    print("Ya has adivinado esa letra o la has intentado incorrectamente.")
            else:
                print("Por favor, ingresa una letra válida.")

    def actualizar_letras_adivinadas(self, letra):
        for i in range(len(self.palabra)):
            if self.palabra[i] == letra:
                self.letras_adivinadas[i] = letra

    def mostrar_estadisticas(self):
        """Muestra un gráfico circular con las estadísticas de victorias y derrotas."""
        etiquetas = list(self.estadisticas.keys())
        valores = list(self.estadisticas.values())
        colores = ['#4CAF50', '#F44336']  # Verde para ganadas, rojo para perdidas
        explode = (0.1, 0)  # Resalta el primer sector (Ganadas)

        print(f"\nEstadísticas actuales:\nGanadas: {self.estadisticas['Ganadas']}\nPerdidas: {self.estadisticas['Perdidas']}\n")
        plt.figure(figsize=(6, 6))
        plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=colores, explode=explode)
        plt.title("Estadísticas de Juego: Ganadas vs Perdidas")
        plt.show()

    def pedir_reiniciar(self):
        while True:
            opcion = input('¿Quieres jugar de nuevo? (S/N): ').lower()
            if opcion == 's':
                return True
            elif opcion == 'n':
                return False
            else:
                print("Por favor, ingresa 'S' para sí o 'N' para no.")

# Crear instancia y comenzar el juego
juego = Ahorcado()
juego.iniciar_juego()
