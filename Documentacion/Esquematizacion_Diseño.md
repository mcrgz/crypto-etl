# Evaluación de la Solución
## Exploración
- Herramientas:  
    - Postman + Jupyter Notebooks
- Justificación:
    - **Postman** : Se utilizaría para la exploración de los diferentes endpoints de la API, con el fin de entender las estructuras y los datos disponibles.
    - **Jupyter Notebooks**: Facilitara la inspección y limpieza de los datos, con el fin de reutilizarlos localmente sin la necesidad de realizar múltiples peticiones.

## Extracción
- Herramientas: 
    - Python + requests
- Justificación:
    - **requests**:  Una vez identificado los endpoints relevantes se utilizará esta librería para la extracción de datos desde la API

## Transformación
- Herramientas: 
    - Python + Pandas
- Justificación:
    - **Pandas**: Se utilizará esta librería para la transformación y limpieza de datos, de igual manera ya se tendrá una idea de lo que se tiene que hacer por la exploración realizada en Jupyter.
## Carga
- Herramientas: 
    - Python + SQLAlchemy 🡪 SQL Server
- Justificación:
    - **SQLAlchemy**: Para la conexión y carga a la BD.

## Diagrama Data Pipeline

![Diagrama Pipeline](pipeline.png)