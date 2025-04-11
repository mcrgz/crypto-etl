import requests
import pandas as pd
import datetime

class Api:

    def  __init__(self,api_key):

        self.base_url = 'https://api.coingecko.com/api/v3'
        self.headers = {
            "accept": "application/json",
            "x-cg-demo-api-key": api_key
            }
        
    def obtieneCryptoCoins(self):
        url_enpoint = 'coins/list'
        url = f"{self.base_url}/{url_enpoint}"
        try:
            response = requests.get(url, headers=self.headers)  
            response.raise_for_status() 
            data =  response.json()
            df_coins = pd.json_normalize(data)
            return df_coins
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud HTTP: {e}")
            raise

    def obtieneCoinsMarkets(self):
        url_enpoint = 'coins/markets?vs_currency=usd&order=market_cap_desc&per_page=15&page=1'
        url = f"{self.base_url}/{url_enpoint}"
        try:
            response = requests.get(url, headers=self.headers)  
            response.raise_for_status() 
            data =  response.json()
            df_market = pd.json_normalize(data)
            #Estos campos son los segun la doc tipo date
            campos_fecha_market = ['ath_date','atl_date','last_updated']
            for col in campos_fecha_market:
                if col in df_market.columns:
                    df_market[col] = pd.to_datetime(df_market[col], errors='coerce')
                    df_market[col] = df_market[col].dt.tz_localize(None)
        
            col_arreglos = list(set([col.split('.')[0] for col in [col for col in df_market.columns if '.' in col]]))
            for col in col_arreglos:
                df_market = df_market.drop(columns=[col])
            df_market = df_market.rename(columns={col: col.replace('.', '_') for col in df_market.columns})
            df_market = df_market[['id','image','current_price','market_cap','market_cap_rank','fully_diluted_valuation','total_volume','high_24h','low_24h','price_change_24h','price_change_percentage_24h','market_cap_change_24h','market_cap_change_percentage_24h','circulating_supply','total_supply','max_supply','ath','ath_change_percentage','ath_date','atl','atl_change_percentage','atl_date','last_updated','roi_times','roi_currency','roi_percentage']]

            return df_market
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud HTTP: {e}")
            raise

    def obtieneCoinsTrending(self):
        url_enpoint = 'search/trending'
        url = f"{self.base_url}/{url_enpoint}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status() 
            data_market = response.json()
            trending_coins = data_market['coins']
            for coin in trending_coins:
                try:
                    del coin['item']['data']['price_change_percentage_24h']
                    del coin['item']['data']['content']
                    del coin['item']['data']['price_btc']
                except KeyError:
                    pass
            df_trending = pd.json_normalize(trending_coins)
            df_trending = df_trending.rename(columns={col: col.replace('item.', '') for col in df_trending.columns})
            df_trending = df_trending.rename(columns={col: col.replace('data.', '') for col in df_trending.columns})
            convertir_de_string = ['market_cap','market_cap_btc','total_volume','total_volume_btc']
            for col in convertir_de_string:
                df_trending[col] = (df_trending[col].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float))
            
            df_trending = df_trending[['id','market_cap_rank','thumb','price_btc','price','market_cap','market_cap_btc','total_volume','total_volume_btc']]
            
            return df_trending
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud HTTP: {e}")
            raise
        
    def obtieneHistorial(self,Coin,TipoDato):
        url_enpoint = f'coins/{Coin}/market_chart?vs_currency=usd&days=6'
        url = f"{self.base_url}/{url_enpoint}"
        try:
            response = requests.get(url, headers=self.headers)  
            response.raise_for_status() 
            data =  response.json()
            df = pd.DataFrame(data[TipoDato], columns=['fecha', 'value'])
            df['fecha'] = pd.to_datetime(df['fecha'], unit='ms')
            hoy = datetime.datetime.today().date()
            df = df[df['fecha'].dt.date == hoy]
            df['id'] = Coin
            df['type'] = TipoDato
            return df
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud HTTP: {e}")
            raise
