import matplotlib.pyplot as plt
import os

def crear_carpeta_graficos():
    """
    Crea la carpeta graficos si no existe
    
    """
    if not os.path.exists("graficos/"):
        os.makedirs("graficos")


def grafico_hits_por_jugador(df):
    """
    crea un grafico de barras con la cantidad total de hits de cada jugador.
    Guarda el grafico en la carpeta graficos/
    """
    hits_A = df["hit_A"].sum()
    hits_B = df["hit_B"].sum()
    
    jugadores = ["Augusto (A)", "Matias (B)"]
    hits = [hits_A, hits_B]
    plt.figure()
    plt.bar(jugadores, hits)
    plt.title("Hits totales por jugador")
    plt.xlabel("Jugador")
    plt.ylabel("cantidad de hits")
    plt.savefig("graficos/hits_por_jugador.png")
    plt.close()

def grafico_evolucion_hits(df):
    """
    Genera un gradico de lineas con la evolucion de hits acumulador por cada jugador.
    Guarda el grafico en la carpeta graficos/
    """    
    
    hits_acumulados_A = df["hit_A"].cumsum()
    hits_acumulados_B = df["hit_B"].cumsum()
    
    plt.figure()
    plt.plot(df["tiempo_relativo"], hits_acumulados_A, label="Augusto (A)")
    plt.plot(df["tiempo_relativo"], hits_acumulados_B, label="Matias (B)")
    plt.title("Evolucion de hits acumulados")
    plt.xlabel("Tiempo relativo")
    plt.ylabel("Hits acumulados")
    plt.legend()
    plt.savefig("graficos/evolucion_hits.png")
    plt.close()
    
    
    
    
    
    
    
    
    
    
    