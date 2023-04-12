import random

palabras = ['perro', 'gato', 'elefante', 'jirafa', 'rinoceronte', 'cocodrilo', 'leon', 'tigre', 'mono', 'cebra']

def jugar_ahorcado():
    palabra = random.choice(palabras)
    letras_adivinadas = ['_'] * len(palabra)
    letras_erroneas = []
    dibujo = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    while True:
        print(dibujo[len(letras_erroneas)])
        print(' '.join(letras_adivinadas))
        letra = input('Ingrese una letra: ').lower()
        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    letras_adivinadas[i] = letra
            if '_' not in letras_adivinadas:
                print('¡Felicidades! Has adivinado la palabra')
                break
        else:
            letras_erroneas.append(letra)
            if len(letras_erroneas) == len(dibujo):
                print(dibujo[-1])
                print('Has perdido. La palabra era', palabra)
                break

    opcion = input('¿Quieres jugar de nuevo? (S/N)').lower()
    if opcion == 's':
        jugar_ahorcado()

jugar_ahorcado()
