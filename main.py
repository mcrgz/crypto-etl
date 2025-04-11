from sql_handler import SQLServerHandler
from api_handler import Api
import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime, timedelta

#Carga Variables de entorno
load_dotenv()

class MainApp:
    def __init__(self, db_connection_string):
        self.db_handler = SQLServerHandler(db_connection_string)
        api_key = os.getenv("API_COINGECKO_KEY")    
        self.apiConexion = Api(api_key)
    
    def run(self):
        db_coins_pk = 'Coin'
        api_coins_pk = 'id'

        df_db_coins = self.db_handler.obtieneCoins()
        df_api_coins = self.apiConexion.obtieneCryptoCoins()

        ######################################################################################################
        #Como primer paso se actualiza el catalogo de monedas inserta las que no existen y se eliminan las que ya no:
        ######################################################################################################
        coin_table = 'Coins'
        
        df_diff = pd.merge(df_db_coins, df_api_coins, left_on=db_coins_pk,right_on=api_coins_pk,how='outer',indicator=True) 
        df_solo_api = df_diff[df_diff['_merge'] == 'right_only']
        df_solo_db = df_diff[df_diff['_merge'] == 'left_only']
        df_solo_api = df_solo_api[['id', 'symbol', 'name']]
        df_solo_api.columns = ['Coin', 'Symbol', 'Name']
        
        self.db_handler.insertTablas(df_solo_api,coin_table)

        #Se convierten los Id's a una lista para poder eliminarlos.
        ids_a_borrar = df_solo_db[db_coins_pk].tolist()
        self.db_handler.deleteTablabyList(ids_a_borrar,coin_table,db_coins_pk)

        #Se vuelve a actualizar el df con el fin de obtener los datos actualizados.
        df_db_coins = self.db_handler.obtieneCoins()

        ######################################################################################################
        #Proceso para obtener y guardar las 15 monedas con el market cap mas alto.
        ######################################################################################################

        market_table = 'CoinsMarkets'
        #Dado que son datos cambiantes los datos se eliminan para poder insertar:
        self.db_handler.truncateTable(market_table)
        df_api_coinsmarket = self.apiConexion.obtieneCoinsMarkets()

        df_market = pd.merge(df_db_coins, df_api_coinsmarket, left_on=db_coins_pk,right_on=api_coins_pk) 
        df_market = df_market.drop(columns=[db_coins_pk,api_coins_pk])

        #Se inserta dentro de la tabla los nuevos registros:
        self.db_handler.insertTablas(df_market,market_table)

        ######################################################################################################
        #Se inserta dentro de la tabla CoinsTrendings
        ######################################################################################################

        trending_table = 'CoinsTrendings'
        self.db_handler.truncateTable(trending_table)

        df_api_trending = self.apiConexion.obtieneCoinsTrending()
        df_trendingCoins = pd.merge(df_db_coins,
                                    df_api_trending,
                                    left_on=db_coins_pk,right_on=api_coins_pk)
        
        df_trendingCoins = df_trendingCoins.drop(columns=[db_coins_pk,api_coins_pk])
        self.db_handler.insertTablas(df_trendingCoins,trending_table)

        ######################################################################################################
        #Se inserta dentro de la tabla CoinsTrendings
        ######################################################################################################

        hist_table = 'CoinsHistory'
        #El registro que se llevara sera de 5 dias por lo que se eliminan el dia 6.
        fecha_eliminar = str((datetime.today() - timedelta(days=6)).date())
        self.db_handler.deleteTablabyValue(fecha_eliminar, hist_table, "CAST(fecha as date)")

        #si se ejecuta mas veces al dia se elimina el dia y se carga de nuevo
        fecha_agregar = str((datetime.today()).date())
        self.db_handler.deleteTablabyValue(fecha_agregar, hist_table, "CAST(fecha as date)")

        #self.db_handler.truncateTable(hist_table)
        df_final = pd.DataFrame()
        coin_hist_data = df_api_coinsmarket[api_coins_pk].tolist()
        TipoDato = 'prices'
        for coin in coin_hist_data:
            df_api_trending = self.apiConexion.obtieneHistorial(coin, TipoDato)
            df_final = pd.concat([df_final, df_api_trending], ignore_index=True)

        
        df_final = pd.merge(df_db_coins,
                    df_final,
                    left_on=db_coins_pk, right_on=api_coins_pk,
                    how='right')
        
        df_final = df_final.drop(columns=[db_coins_pk,api_coins_pk])
        self.db_handler.insertTablas(df_final,hist_table)



if __name__ == "__main__":
    # Configuración de la aplicación
    usuario = os.getenv("DB_USER")
    passw = os.getenv("DB_PASSWORD")
    Servidor =os.getenv("DB_HOST")
    Base = os.getenv("DB")
    db_connection_string = f'mssql+pyodbc://{usuario}:{passw}@{Servidor}/{Base}?driver=ODBC+Driver+17+for+SQL+Server'


    # Iniciar la aplicación
    app = MainApp(db_connection_string)
    app.run()