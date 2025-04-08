import requests
import pandas as pd

class Api:

    def  __init__(self):

        self.url = 'https://api.coingecko.com/api/v3'
        self.headers = {
            "accept": "application/json",
            "x-cg-demo-api-key": "hyperliquid"
            }

        endp_topten = 'coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1'