from flask import Flask, request, jsonify
import requests
import json
import os

app = Flask(__name__)

# Configuración del servicio de Azure ML
SCORING_URI = os.environ.get('SCORING_URI', 'URL_DE_TU_SERVICIO_ACI')
API_KEY = os.environ.get('API_KEY', 'TU_CLAVE_API')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener datos de la solicitud
        request_data = request.get_json()
        
        # Preparar encabezados para la solicitud a Azure ML
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        }
        
        # Llamar al servicio de Azure ML
        response = requests.post(
            SCORING_URI, 
            data=json.dumps(request_data), 
            headers=headers
        )
        
        # Devolver la respuesta
        return jsonify(json.loads(response.text))
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'API funcionando correctamente'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8800, debug=True)