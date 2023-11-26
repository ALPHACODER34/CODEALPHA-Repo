import tkinter as tk
from tkinter import ttk

class CryptoTradingBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Trading Bot")

        # Default values
        self.background_color = "#3b4371"
        self.window_width = 400
        self.window_height = 200

        self.label_buy = ttk.Label(root, text="Buy")
        self.label_buy.grid(row=0, column=0, pady=10)

        self.entry_buy = ttk.Entry(root)
        self.entry_buy.grid(row=0, column=1, pady=10)

        self.label_sell = ttk.Label(root, text="Sell")
        self.label_sell.grid(row=1, column=0, pady=10)

        self.entry_sell = ttk.Entry(root)
        self.entry_sell.grid(row=1, column=1, pady=10)

        self.btn_buy = ttk.Button(root, text="Buy", command=self.buy)
        self.btn_buy.grid(row=2, column=0, pady=10)

        self.btn_sell = ttk.Button(root, text="Sell", command=self.sell)
        self.btn_sell.grid(row=2, column=1, pady=10)

        # Configure window size and background color
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.configure(bg=self.background_color)

    def buy(self):
        amount = self.entry_buy.get()
        # Add code to buy cryptocurrency here

    def sell(self):
        amount = self.entry_sell.get()
        # Add code to sell cryptocurrency here

# Create the GUI window
root = tk.Tk()
CryptoTradingBot(root)
root.mainloop()
