import json
import requests
import pandas as pd

with open("service_info.json", "r") as f:
    service_info = json.load(f)

scoring_uri = service_info["scoring_uri"]
primary_key = service_info["primary_key"]

cliente_ejemplo = {
    "data": {
        "CustomerID": [1001],
        "NameStyle": [False],
        "Title": ["Sr."],
        "FirstName": ["Carlos"],
        "MiddleName": [None],
        "LastName": ["Gómez"],
        "Suffix": [None],
        "CompanyName": ["Empresa Nueva"],
        "SalesPerson": ["adventure-works\\david8"],
        "EmailAddress": ["carlos@ejemplo.com"],
        "Phone": ["555-123-4567"]
    }
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {primary_key}"
}

print("Enviando solicitud al servicio...")
response = requests.post(
    scoring_uri, 
    data=json.dumps(cliente_ejemplo),
    headers=headers
)

print("\nRespuesta del servicio:")
print(f"Código de estado: {response.status_code}")
if response.status_code == 200:
    result = response.json()
    print(f"Fecha predicha: {result.get('predicted_date', 'No disponible')}")
    print(f"Respuesta completa: {result}")
else:
    print(f"Error: {response.text}")