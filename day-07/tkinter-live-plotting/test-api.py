import requests

def link1():
    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        data = response.json()
        price = data['data']['priceUsd']
        print(f"Current Bitcoin Price: ${price}")
    except:
        print("Exception Occured")

def link2():
    try:
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'your_api_key',
        }

        response = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC&convert=USD", headers=headers)
        data = response.json()
        price = data['data']['BTC']['quote']['USD']['price']
        print(f"Current Bitcoin Price: ${price}")
    except:
        print("Exception Occured")

def link3():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        data = response.json()
        print (float(data['bitcoin']['usd']))
    except:
        print("Exception Occured")
if __name__ == "__main__":
    link1()
    link2()
    link3()
