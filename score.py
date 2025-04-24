# Guardar como score.py en el directorio simple_model
import json
import pickle
import numpy as np
import os
from azureml.core.model import Model

def init():
    global modelo
    print("Iniciando init()")
    
    # Cargar el modelo simple
    model_path = Model.get_model_path('modelo_actualizado')
    modelo = pickle.load(open(model_path, 'rb'))
    print("Modelo cargado correctamente")

def run(data):
    try:
        print("Procesando solicitud")
        # Parsear los datos JSON
        data_dict = json.loads(data)
        input_data = np.array(data_dict['data'])
        
        # Hacer la predicción
        result = modelo.predict(input_data).tolist()
        
        # Devolver el resultado
        return {"result": result}
        
    except Exception as e:
        error = str(e)
        return {"error": error}