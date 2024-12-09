import matplotlib.pyplot as plt

def mostrar_estadisticas(estadisticas):
    etiquetas = list(estadisticas.keys())
    valores = list(estadisticas.values())
    colores = ['#4CAF50', '#F44336']  # Verde para ganadas, rojo para perdidas
    explode = (0.1, 0)  # Resalta el primer sector (Ganadas)

    print(f"\nEstadísticas actuales:\nGanadas: {estadisticas['Ganadas']}\nPerdidas: {estadisticas['Perdidas']}\n")
    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=colores, explode=explode)
    plt.title("Estadísticas de Juego: Ganadas vs Perdidas")
    plt.show()
