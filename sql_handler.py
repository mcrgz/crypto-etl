from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String,Boolean,Date

import pandas as pd

class SQLServerHandler:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    #Esta funcion obtiene la lista de criptomonedas
    def obtieneCoins(self):
        query = text("select IDCoin,Coin from Coins")
        try:
            with self.engine.connect() as connection:
                df_tabla = pd.read_sql(query, connection)
            return df_tabla

        except SQLAlchemyError as e:
            print(f"Error en la base de datos: {e}")
            raise

    def truncateTable(self,tabla):
        with self.engine.connect() as connection:
            connection.execute(text(f"TRUNCATE TABLE {tabla}"))
            connection.commit()

    def insertTablas(self,df,NombreTabla):
        df.to_sql(NombreTabla, con=self.engine, if_exists='append', index=False)

    def deleteTabla(self,lista,NombreTabla,campo):
        #Por cada valor se genera una lista con ids
        where = ','.join([f":id{i}" for i in range(len(lista))])

        query = text(f"DELETE FROM {NombreTabla} WHERE {campo} IN ({where})")

        #Se genera un diccionario con la asignacion de Id's y valor
        params = {f"id{i}": id_val for i, id_val in enumerate(lista)}

        # Ejecutar
        if params:
            with self.engine.connect() as conn:
                conn.execute(query, params)
            conn.commit()