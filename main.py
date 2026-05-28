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
