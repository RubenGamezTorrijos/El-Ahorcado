import random

class Ahorcado:
    def __init__(self):
        self.palabras = ['perro', 'gato', 'elefante', 'jirafa', 'rinoceronte', 'cocodrilo', 'leon', 'tigre', 'mono', 'cebra']
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

    def iniciar_juego(self):
        self.palabra = random.choice(self.palabras)
        self.letras_adivinadas = ['_'] * len(self.palabra)
        self.letras_erroneas = []

        print("¡Bienvenido al juego del Ahorcado!")
        self.jugar()

    def jugar(self):
        while True:
            self.mostrar_estado()
            letra = self.obtener_input()
            if letra in self.palabra:
                self.actualizar_letras_adivinadas(letra)
                if '_' not in self.letras_adivinadas:
                    print(f"¡Felicidades! Has adivinado el animal: {self.palabra}")
                    break
            else:
                self.letras_erroneas.append(letra)
                if len(self.letras_erroneas) == len(self.dibujo):
                    self.mostrar_estado()
                    print(f"Has perdido. La palabra del animal era {self.palabra}")
                    break
        self.pedir_reiniciar()

    def mostrar_estado(self):
        print(self.dibujo[len(self.letras_erroneas)])
        print(' '.join(self.letras_adivinadas))

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
        opcion = input('¿Quieres jugar de nuevo? (S/N): ').lower()
        if opcion == 's':
            self.iniciar_juego()

# Crear instancia y comenzar el juego
juego = Ahorcado()
juego.iniciar_juego()

