import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
from datetime import datetime
import os

# Sample products and prices
PRODUCTS = [
    {"name": "Book", "price": 10.0},
    {"name": "Pen", "price": 2.5},
    {"name": "Notebook", "price": 5.0},
    {"name": "Bag", "price": 25.0},
]

LOG_FILE = "payment_log.csv"

class PaymentKiosk:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Payment Kiosk")
        self.product_vars = []
        self.quantity_vars = []

        # Header
        tk.Label(root, text="Welcome to the Payment Kiosk", font=("Helvetica", 16)).pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Product selection
        for idx, product in enumerate(PRODUCTS):
            var = tk.IntVar()
            qty_var = tk.IntVar(value=1)

            cb = tk.Checkbutton(self.frame, text=f"{product['name']} - ${product['price']}", variable=var)
            cb.grid(row=idx, column=0, sticky="w")

            qty_entry = tk.Spinbox(self.frame, from_=1, to=10, textvariable=qty_var, width=5)
            qty_entry.grid(row=idx, column=1)

            self.product_vars.append(var)
            self.quantity_vars.append(qty_var)

        # Buttons
        tk.Button(root, text="Pay", command=self.process_payment, bg="green", fg="white", width=20).pack(pady=5)
        tk.Button(root, text="View Payment Log", command=self.view_log, width=20).pack(pady=5)

    def process_payment(self):
        selected_items = []
        total = 0.0

        for i, product in enumerate(PRODUCTS):
            if self.product_vars[i].get():
                qty = self.quantity_vars[i].get()
                amount = product["price"] * qty
                selected_items.append((product["name"], qty, amount))
                total += amount

        if not selected_items:
            messagebox.showwarning("No Selection", "Please select at least one product.")
            return

        confirm = messagebox.askyesno("Confirm Payment", f"Total Amount: ${total:.2f}\nProceed to pay?")
        if confirm:
            self.log_payment(selected_items, total)
            messagebox.showinfo("Payment Successful", "Payment has been recorded.")
            for var in self.product_vars:
                var.set(0)

    def log_payment(self, items, total):
        is_new = not os.path.exists(LOG_FILE)
        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            if is_new:
                writer.writerow(["Timestamp", "Items", "Total"])
            item_str = "; ".join([f"{name} x{qty}" for name, qty, _ in items])
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), item_str, f"{total:.2f}"])

    def view_log(self):
        if not os.path.exists(LOG_FILE):
            messagebox.showinfo("Log Empty", "No payments recorded yet.")
            return

        log_win = tk.Toplevel(self.root)
        log_win.title("Payment Log")

        tree = ttk.Treeview(log_win, columns=("Timestamp", "Items", "Total"), show="headings")
        tree.heading("Timestamp", text="Timestamp")
        tree.heading("Items", text="Items")
        tree.heading("Total", text="Total ($)")
        tree.pack(fill="both", expand=True)

        with open(LOG_FILE, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                tree.insert("", "end", values=(row["Timestamp"], row["Items"], row["Total"]))


if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentKiosk(root)
    root.geometry("400x400")
    root.mainloop()
