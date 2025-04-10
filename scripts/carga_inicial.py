#Este funciona como punto de partida, opteniendo todas las criptos
#variables para obtener contraseñas
from dotenv import load_dotenv
import os
load_dotenv() 

import requests
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

#Conexion Base de Datos
usuario = os.getenv("DB_USER")
passw = os.getenv("DB_PASSWORD")
Servidor =os.getenv("DB_HOST")
Base = os.getenv("DB")
db_conexion = f'mssql+pyodbc://{usuario}:{passw}@{Servidor}/{Base}?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(db_conexion)

url = 'https://api.coingecko.com/api/v3/'

api_key = os.getenv("API_COINGECKO_KEY")

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": api_key
    }

endp_topten = 'coins/list'

response = requests.get(url+endp_topten, headers=headers) 

response_data =  response.json()
df = pd.DataFrame(response_data)

df_dato_general = df[['id', 'symbol', 'name']]

df_dato_general.columns = ['Coin', 'Symbol', 'Name']
df_dato_general.to_sql('Coins', con=engine, if_exists='append', index=False)