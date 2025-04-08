import requests

url = 'https://api.coingecko.com/api/v3/'
headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": "CG-MDXzwMkZTEMXsp5ktsHGZZWa"
    }

endp_topten = 'coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1'

response = requests.get(url+endp_topten, headers=headers)

print(response.text)