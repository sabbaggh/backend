import pandas as pd
import random

# Definir los posibles valores para campos categóricos
objetivos = ["ganarMasa", "bajarPeso", "definir"]
niveles = ["principiante", "medio", "experto"]

# Generar 1000 filas de datos sintéticos
data = {
    "usuario_peso": [random.randint(50, 120) for _ in range(2000)],
    "usuario_estatura": [random.randint(150, 200) for _ in range(2000)],
    "usuario_objetivo": [random.choice(objetivos) for _ in range(2000)],
    "usuario_nivel": [random.choice(niveles) for _ in range(2000)],
    "usuario_rutinas_completadas": [random.randint(1, 100) for _ in range(2000)],
    "usuario_tiempo_en_completar": [round(random.uniform(15, 120), 2) for _ in range(2000)],
    "ejercicios_sets": [random.randint(1, 5) for _ in range(2000)],
    "ejercicio_reps": [random.randint(5, 15) for _ in range(2000)],
    "dificultad_percibida": [random.randint(1, 5) for _ in range(2000)],
    "cansancio_percibido": [random.randint(1, 5) for _ in range(2000)],
    "id_ejercicio": [random.randint(1, 26) for _ in range(2000)],
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Guardar el dataset en un archivo CSV
df.to_csv("historial_dataset.csv", index=False)