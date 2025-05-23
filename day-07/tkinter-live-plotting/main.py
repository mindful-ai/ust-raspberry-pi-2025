# main.py

import tkinter as tk
from logic import BitcoinPriceFetcher
from gui import BitcoinPriceGUI

def main():
    root = tk.Tk()

    fetcher = BitcoinPriceFetcher()

    def get_data():
        return fetcher.update_data()

    app = BitcoinPriceGUI(root, get_data)
    root.mainloop()

if __name__ == "__main__":
    main()
