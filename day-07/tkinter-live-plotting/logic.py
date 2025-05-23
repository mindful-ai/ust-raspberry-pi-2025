# logic.py

import requests
import time

class BitcoinPriceFetcher:
    def __init__(self):
        self.timestamps = []
        self.prices = []

    def fetch_price(self):
        try:
            url = "https://api.coindesk.com/v1/bpi/currentprice/USD.json"
            response = requests.get(url)
            data = response.json()
            price = float(data['bpi']['USD']['rate'].replace(',', ''))
            return price
        except Exception as e:
            print("Error fetching price:", e)
            return None

    def update_data(self):
        price = self.fetch_price()
        if price is not None:
            timestamp = time.strftime("%H:%M:%S")
            self.timestamps.append(timestamp)
            self.prices.append(price)

            # Keep only last 20 records
            self.timestamps = self.timestamps[-20:]
            self.prices = self.prices[-20:]

        return self.timestamps, self.prices
