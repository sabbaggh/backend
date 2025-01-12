import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from itertools import product
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv('historial_dataset.csv')
data.replace('ganarMasa', 1, inplace=True)
data.replace('bajarPeso', 2, inplace=True)
data.replace('definir', 3, inplace=True)

data.replace('principiante', 1, inplace=True)
data.replace('medio', 2, inplace=True)
data.replace('experto', 3, inplace=True)



print(data.columns)
X =  data[['usuario_peso', 'usuario_estatura', 'usuario_objetivo', 'usuario_nivel', 'usuario_rutinas_completadas', 'usuario_tiempo_en_completar', 'dificultad_percibida', 'cansancio_percibido']]
y = data['id_ejercicio']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

model = LogisticRegression(max_iter=15000)
#model = SVC(kernel='linear', C=0.5)
#model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")

joblib.dump(model, 'modelo_entrenado.joblib')
print("Modelo guardado exitosamente.")

'''usuario_base = {
    'usuario_peso': 68,
    'usuario_estatura': 175,
    'usuario_objetivo': 2,
    'usuario_nivel': 2,
    'usuario_rutinas_completadas': 1,
    'usuario_tiempo_en_completar': 3000
}

# Valores que deseas variar
dificultad_percibida = [2, 3, 4, 5]
cansancio_percibido = [2, 3, 4, 5]
niveles = [1,2,3]

# Crear combinaciones de variaciones
variaciones = [
    {**usuario_base, 
     'dificultad_percibida': dif, 
     'cansancio_percibido': cans, 
     'usuario_nivel': nivel}
    for dif, cans, nivel in product(dificultad_percibida, cansancio_percibido, niveles)
]

# Convertir a DataFrame
nuevos_usuarios = pd.DataFrame(variaciones)

# Realizar predicciones para todas las variaciones
ejercicios_recomendados = model.predict(nuevos_usuarios)

# Agregar las predicciones al DataFrame
nuevos_usuarios['ejercicio_recomendado'] = ejercicios_recomendados

# Ver resultados
print(nuevos_usuarios['ejercicio_recomendado'].unique())'''
