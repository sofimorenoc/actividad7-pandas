import pandas as pd
import matplotlib.pyplot as plt
import os

"""
Carga y validación de datos experimentales
utilizando Pandas y Matplotlib.
"""

# crear carpeta de gráficos si no existe
if not os.path.exists("graficos"):
    os.makedirs("graficos")

# ruta del dataset
ruta_csv = "datos/output_salto_competicion_augusto_matias.csv"

# validar que el archivo exista
if not os.path.exists(ruta_csv):
    raise FileNotFoundError("No se encontró el archivo csv")

# cargar dataset
df = pd.read_csv(ruta_csv)

# mostrar primeras filas
print(df.head())

# mostrar columnas
print(df.columns)

# validar valores vacíos
if df.isna().all().all():
    raise ValueError("El dataset está completamente vacío")

# validar tiempo creciente
if not df["timestamp"].is_monotonic_increasing:
    raise ValueError("Los valores de tiempo no están ordenados")

# validar negativos
if (df["x_A"] < 0).any():
    raise ValueError("Hay valores negativos en x_A")

# crear tiempo relativo
df["tiempo_relativo"] = (
    df["timestamp"] - df["timestamp"].iloc[0]
)

# mostrar tiempo relativo
print(df["tiempo_relativo"].head())

# Hits totales

def calcular_hits(df):
    """
   Calcula la cantidad total de hits por jugador y el total general.

   Parámetros:
       df (pd.DataFrame): DataFrame cargado desde el CSV del experimento.

   Retorna:
       dict: Diccionario con hits de A, hits de B y hits totales.
   """
    hits_A = df["hit_A"].sum()
    hits_B = df["hit_B"].sum()
    hits_total = hits_A + hits_B
 
    print(f"Hits Augusto (A): {hits_A}")
    print(f"Hits Matías (B):  {hits_B}")
    print(f"Hits totales:     {hits_total}")
 
    return {"hits_A": hits_A, "hits_B": hits_B, "hits_total": hits_total}

# Hit rate

def calcular_hit_rate(df):
    """
    Calcula el hit rate de cada jugador: proporción de frames con hit
    sobre el total de frames donde el jugador fue detectado (activity_roi = True).
 
    Parámetros:
        df (pd.DataFrame): DataFrame cargado desde el CSV del experimento.
 
    Retorna:
        dict: Diccionario con hit rate de A y hit rate de B (valores entre 0 y 1).
    """
    frames_activos_A = df["activity_roi_A"].sum()
    frames_activos_B = df["activity_roi_B"].sum()
 
    hit_rate_A = df["hit_A"].sum() / frames_activos_A if frames_activos_A > 0 else 0
    hit_rate_B = df["hit_B"].sum() / frames_activos_B if frames_activos_B > 0 else 0
 
    print(f"Hit rate Augusto (A): {hit_rate_A:.4f}")
    print(f"Hit rate Matías (B):  {hit_rate_B:.4f}")
 
    return {"hit_rate_A": hit_rate_A, "hit_rate_B": hit_rate_B}

# Distancia recorrida

def calcular_distancia_recorrida(df):

# Distancia por hit

def calcular_distancia_por_hit(distancias, hits):

# Determinar ganador

def determinar_ganador(hits):
    """
    Determina el ganador de la competición basándose en la cantidad de hits.
 
    Parámetros:
        hits (dict): Resultado de calcular_hits().
 
    Retorna:
        str: Nombre del ganador o mensaje de empate.
    """
    if hits["hits_A"] > hits["hits_B"]:
        ganador = "Augusto (A)"
    elif hits["hits_B"] > hits["hits_A"]:
        ganador = "Matías (B)"
    else:
        ganador = "Empate"
 
    print(f"Ganador: {ganador}")
    return ganador

# Filtrados

def filtrar_frames_con_actividad(df):
    """
    Filtra y retorna solo los frames donde al menos uno de los dos
    jugadores fue detectado en la región de interés (activity_roi = True).
 
    Parámetros:
        df (pd.DataFrame): DataFrame cargado desde el CSV del experimento.
 
    Retorna:
        pd.DataFrame: Subconjunto del DataFrame con actividad detectada.
    """
    df_activo = df[df["activity_roi_A"] | df["activity_roi_B"]]
    print(f"Frames con actividad: {len(df_activo)} de {len(df)} totales")
    return df_activo

# Groupby

def resumen_por_condicion(df):
    """
    Agrupa los datos por condición experimental y calcula el promedio
    de hits totales acumulados en cada grupo.
 
    Parámetros:
        df (pd.DataFrame): DataFrame cargado desde el CSV del experimento.
 
    Retorna:
        pd.Series: Promedio de hits_total agrupado por condición.
    """
    resumen = df.groupby("condicion")["hits_total"].mean()
    print("\nResumen por condición:")
    print(resumen)
    return resumen

# Llamando a las funciones

hits        = calcular_hits(df)
hit_rates   = calcular_hit_rate(df)
distancias  = calcular_distancia_recorrida(df)
dist_x_hit  = calcular_distancia_por_hit(distancias, hits)
ganador     = determinar_ganador(hits)
resumen     = resumen_por_condicion(df)
df_activo   = filtrar_frames_con_actividad(df)