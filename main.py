
iimport pandas as pd
import matplotlib.pyplot as plt
import os

# creo la carpeta graficos si no existe
if not os.path.exists("graficos"):
    os.makedirs("graficos")

# ruta del archivo csv
ruta_csv = "datos/output_salto_competicion_augusto_matias.csv"

# verifico que el archivo exista
if not os.path.exists(ruta_csv):
    raise FileNotFoundError("No se encontró el archivo csv")

# cargo el dataset
df = pd.read_csv(ruta_csv)

# muestro primeras filas y columnas
print(df.head())

print(df.columns)

# validacion de valores vacios
if df.isna().any().any():
    raise ValueError("El dataset tiene valores vacíos")

# validacion temporal
if not df["timestamp"].is_monotonic_increasing:
    raise ValueError("Los valores de tiempo no están ordenados")

# validacion de negativos
if (df["x_A"] < 0).any():
    raise ValueError("Hay valores negativos en x_A")

# creo tiempo relativo desde el inicio
df["tiempo_relativo"] = (
    df["timestamp"] - df["timestamp"].iloc[0]
)

# muestro resultados
print(df["tiempo_relativo"].head())
