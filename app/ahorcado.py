import random
from .dibujo import obtener_dibujo
from .estadisticas import mostrar_estadisticas
from .palabras import cargar_palabras

class Ahorcado:
    def __init__(self):
        self.palabras = cargar_palabras()
        self.dibujo = obtener_dibujo
        self.palabra = ""
        self.letras_adivinadas = []
        self.letras_erroneas = []
        self.estadisticas = {"Ganadas": 0, "Perdidas": 0}

    def iniciar_juego(self):
        while True:
            if not self.palabras:
                print("No hay palabras disponibles para jugar.")
                break

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
                if len(self.letras_erroneas) == len(self.dibujo(self.letras_erroneas)) - 1:
                    self.mostrar_estado()
                    print(f"Has perdido. La palabra del animal era {self.palabra}")
                    self.estadisticas["Perdidas"] += 1
                    break

        mostrar_estadisticas(self.estadisticas)

    def mostrar_estado(self):
        print(obtener_dibujo(len(self.letras_erroneas)))
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

    def pedir_reiniciar(self):
        while True:
            opcion = input('¿Quieres jugar de nuevo? (S/N): ').lower()
            if opcion == 's':
                return True
            elif opcion == 'n':
                return False
            else:
                print("Por favor, ingresa 'S' para sí o 'N' para no.")
