# 🧩 El Ahorcado 🧑‍🏫

¡Bienvenido al juego clásico de "El Ahorcado"! Adivina la palabra secreta antes de que el ahorcado complete su dibujo. Este juego es simple, entretenido y perfecto para poner a prueba tu conocimiento de animales.

## 🎮 Cómo Jugar 

1. **Inicio del juego**: Al iniciar, el juego elegirá una palabra aleatoria relacionada con animales.
2. **Seleccionar letras**: Adivina una letra a la vez. Si la letra está en la palabra, aparecerá en su lugar correspondiente.
3. **Intentos**: Si la letra no está en la palabra, se sumará un error y se mostrará una parte del dibujo del ahorcado.
4. **Fin del juego**:
   - **Victoria**: Si adivinas todas las letras de la palabra antes de que se complete el dibujo del ahorcado, ¡ganas!
   - **Derrota**: Si cometes demasiados errores, perderás el juego.

## 📝 Características 

- 🎲 Palabras aleatorias relacionadas con animales.
- 🖼️ Dibujo progresivo del ahorcado con 7 fases.
- 🔄 Opción de jugar varias veces con un nuevo animal.
- 🔤 Validación de entradas para garantizar que solo se ingrese una letra válida.
- 🎲 Python v.3.11.3

## 🗂️ Arquitectura del proyecto
```
ahorcado/
│
├── datos/
│   └── animales.json        # Listado de animales.
│
├── app/
│   ├── __init__.py          # Inicialización del paquete de la aplicación.
│   ├── ahorcado.py          # Lógica del juego del ahorcado.
│   ├── estadisticas.py      # Lógica de estadísticas y gráficos.
│   ├── palabras.py          # Carga de las palabras desde el archivo JSON.
│   └── dibujo.py            # Representación del ahorcado (dibujo).
│
├── requirements.txt         # Dependencias del proyecto.
└── main.py                  # Archivo principal para ejecutar el juego.
```

## 🖥️ Requisitos del Sistema 

Este juego está desarrollado en Python y no requiere dependencias externas.

- **Python 3.8 o superior**.

## 🔧 Instalación

Sigue estos pasos para jugar el juego en tu máquina:

### Clonar el Repositorio

1. Clona este repositorio en tu máquina local utilizando Git:

    ```bash
    git clone https://github.com/RubenGamezTorrijos/El-Ahorcado.git
    ```

2. Accede a la carpeta del proyecto:

    ```bash
    cd ahorcado
    ```

3. Si no tienes Python instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### 🚀 Ejecutar el Juego

1. Navega a la carpeta donde has clonado el proyecto.
2. Ejecuta el juego con el siguiente comando:

    ```bash
    # Crear un entorno virtual
    python -m venv venv

    # Activar el entorno (en Windows)
    venv\Scripts\activate

    #Activar el entorno (en MacOS/Linux)
    source venv/bin/activate
    
    ```
3. Una vez activado el entorno virtual, puedes instalar las dependencias con el comando:

   ```bash
    pip install -r requirements.txt
    ```

3. ¡El juego comenzará y podrás empezar a adivinar!

## Ejemplo de Juego 🕹️

| Juego entorno usuario |
|:-----------------------:|
|![image](https://github.com/user-attachments/assets/237ac6df-20fd-4142-a20b-1ef2b5c2b147)|
