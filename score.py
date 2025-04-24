import json
import numpy as np
import pandas as pd
import pickle
from datetime import datetime
from azureml.core.model import Model
from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType

def init():
    global modelo, encoder, scaler, columnas_categoricas, columnas_numericas, fecha_referencia
    
    model_path = Model.get_model_path('model')
    modelo = pickle.load(open(model_path, 'rb'))
    
    encoder = pickle.load(open('./encoder.pkl', 'rb'))
    scaler = pickle.load(open('./scaler.pkl', 'rb'))
    columnas_categoricas = pickle.load(open('./columnas_categoricas.pkl', 'rb'))
    columnas_numericas = pickle.load(open('./columnas_numericas.pkl', 'rb'))
    
    fecha_referencia = datetime(2000, 1, 1)

input_sample = pd.DataFrame({
    'CustomerID': [1001],
    'NameStyle': [False],
    'Title': ['Sr.'],
    'FirstName': ['Carlos'],
    'MiddleName': [None],
    'LastName': ['Gómez'],
    'Suffix': [None],
    'CompanyName': ['Empresa Nueva'],
    'SalesPerson': ['adventure-works\\david8'],
    'EmailAddress': ['carlos@ejemplo.com'],
    'Phone': ['555-123-4567']
})

output_sample = {"predicted_date": "2006-09-09"}

@input_schema('data', PandasParameterType(input_sample))
@output_schema(NumpyParameterType(output_sample))
def run(data):
    try:
        cliente = data.copy()
        
        if columnas_categoricas:
            for col in columnas_categoricas:
                if col in cliente.columns:
                    cliente[col] = cliente[col].fillna('Desconocido')
            
            nuevo_encoded = encoder.transform(cliente[columnas_categoricas])
            if hasattr(nuevo_encoded, 'toarray'):
                nuevo_encoded = nuevo_encoded.toarray()
                
            nuevo_encoded_df = pd.DataFrame(
                nuevo_encoded,
                columns=encoder.get_feature_names_out(columnas_categoricas)
            )
            
            cliente = cliente.drop(columnas_categoricas, axis=1)
            cliente = pd.concat([cliente, nuevo_encoded_df], axis=1)
        
        for col in columnas_numericas:
            if col in cliente.columns:
                cliente[col] = cliente[col].fillna(cliente[col].mean())
        
        if columnas_numericas:
            cliente[columnas_numericas] = scaler.transform(cliente[columnas_numericas])
    
        dias_predichos = modelo.predict(cliente)[0]
        fecha_predicha = fecha_referencia + pd.Timedelta(days=int(dias_predichos))
        
        result = {"predicted_date": fecha_predicha.strftime('%Y-%m-%d')}
        return result
    except Exception as e:
        error = str(e)
        return {"error": error}