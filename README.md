# ActividadEvdencia

Este proyecto lo desarrollamos como una evidencia de aprendizaje para aplicar un modelo de machine learning en Python. Utilizamos Jupyter Notebook para llevar a cabo todo el proceso: análisis de datos, entrenamiento y evaluación del modelo. Luego lo desplegamos mediante una API con Flask para permitir hacer predicciones desde fuera.

Los archivos más importantes del proyecto son:

- `main.ipynb`: contiene el desarrollo completo del modelo.
- `api.py`: lanza la API para consumir el modelo.
- `modelo.pkl`, `scaler.pkl`, `encoder.pkl`: archivos serializados que usamos para predecir (modelo, escalador y codificador).
- `score.py`: lo usamos para probar la API.
- `requirements.txt`: lista de librerías necesarias para que funcione el proyecto.

Para probarlo, basta con instalar los paquetes con `pip install -r requirements.txt` y ejecutar `api.py`. Con eso ya se puede hacer uso de la API local para obtener predicciones.

El proyecto está bajo licencia MIT.
