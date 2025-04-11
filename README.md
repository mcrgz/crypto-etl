# ETL Crypto Coin

## Descripcion del Proyecto

El objetivo del proyecto es construir un ETL pipeline. Recolectando datos ciertas fuentes, transformando los datos de acuerdo a los requerimientos y cargarlos dentro de un destino de almacenamiento de datos.

    crypto-etl/
    ├── Exploracion/
    │ ├── CoinGecko.postman_collection.json # Colección de Postman para pruebas de API
    │ └── APL-crypto.ipynb # Notebook de exploración de datos
    ├── Documentacion/
    │ ├── Data_Pipeline_Explicacion.md # Detalle del flujo ETL
    │ ├── Esquematizacion_Diseño.pdf # Diseño de la solución
    │ └── ERD.png # Diagrama Entidad-Relación
    ├── main.py # Script principal
    ├── api_handler.py # Manejo de API
    ├── sql_handler.py # Operaciones con DB
    ├── .env.example # Plantilla de variables de entorno
    ├── requisitos.txt # Dependencias
    └── .gitignore # Archivos ignorados por Git


## Como Ejecutar el Proyecto
### Ejecutar ETL pipeline desde la linea de comando:

### Requisitos
- Python 3+
- Ejecutor de codigo python de preferencia


- Instrucciones:
  - Copiar el ``.env.example`` a un archivo llamado `.env` y llenar las variables 
  de entorno
    - Para la variable `API_COINGECKO_KEY` la key se puede obtener siguiendo las instrucciones de el siguiente link: [Generar API key CoinGecko](https://support.coingecko.com/hc/en-us/articles/21880397454233-User-Guide-How-to-sign-up-for-CoinGecko-Demo-API-and-generate-an-API-key)
  - Instalar las librerias necesarias para ejecutar `main.py`
  - Ejecutar el script `main.py`
  

- Windows:
```
  pip install -r requisitos.txt
```
```
  python main.py
```

- Mac:
```
  pip3 install -r requisitos.txt
```

```
  python3 main.py
```
# Documentación Técnica

Para detalles del diseño, flujo de datos y esquema de la base de datos, consulta:<br>

- [Esquematizacion y Diseño](Documentacion/Esquematizacion_Diseño.md)
- [Explicacion de Pipeline](Documentacion/Data_Pipeline_Explicacion.md)

---