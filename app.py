from flask import Flask, request, jsonify
import joblib
import pandas as pd
from itertools import product

app = Flask(__name__)

@app.route('/generarRutina', methods=['POST'])
def generarRutina():
    print('hola')
    #Hacer solicitud para obtener los datos
    datosUsuario = request.json
    
    #Ordenar los datos
    usuario_base = {
        'usuario_peso': datosUsuario.get('usuario_peso'),
        'usuario_estatura': datosUsuario.get('usuario_estatura'),
        'usuario_objetivo': int(datosUsuario.get('usuario_objetivo').replace('ganarMasa', '1').replace('bajarPeso', '2').replace('definir', '3')),
        'usuario_nivel': int(datosUsuario.get('usuario_nivel').replace('principiante', '1').replace('medio', '2').replace('experto', '3')),
        'usuario_rutinas_completadas': datosUsuario.get('usuario_rutinas_completadas'),
        'usuario_tiempo_en_completar': datosUsuario.get('usuario_tiempo_en_completar')
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
    model = joblib.load('modelo_entrenado.joblib')
    # Realizar predicciones para todas las variaciones
    ejercicios_recomendados = model.predict(nuevos_usuarios)

    # Agregar las predicciones al DataFrame
    nuevos_usuarios['ejercicio_recomendado'] = ejercicios_recomendados
    ejercicios_unicos = list(map(int, nuevos_usuarios['ejercicio_recomendado'].unique()))
    return jsonify(ejercicios_unicos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)