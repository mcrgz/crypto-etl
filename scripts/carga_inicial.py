import requests
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

#Conexion Base de Datos
usuario = 'mariam'
passw = 'Abc123'
Servidor ='Mcrgz\MSSQLSERVERF'
Base = 'Crypto'
db_conexion = f'mssql+pyodbc://{usuario}:{passw}@{Servidor}/{Base}?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(db_conexion)


url = 'https://api.coingecko.com/api/v3/'
headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": "CG-MDXzwMkZTEMXsp5ktsHGZZWa"
    }

endp_topten = 'coins/markets?vs_currency=usd'

response = requests.get(url+endp_topten, headers=headers) 


response_data =  response.json()
df = pd.DataFrame(response_data)

df_dato_general = df[['id', 'symbol', 'name', 'image']]

df_dato_general.columns = ['Crypto', 'Symbol', 'Name', 'Image']
df_dato_general.to_sql('Crypto', con=engine, if_exists='append', index=False)