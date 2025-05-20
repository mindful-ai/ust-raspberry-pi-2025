# Class based calculator application using tkinter

from tkinter import *

class CalculatorApp:

    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("400x600")
        self.master.config(bg="lightblue")

        # Entry field
        self.entry = Entry(master, width=16, font=("Arial", 24), bd=10, insertwidth=2, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            Button(master, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, END)
                self.entry.insert(0, str(result))
            except Exception as e:
                self.entry.delete(0, END)
                self.entry.insert(0, "Error")
        else:
            current_text = self.entry.get()
            new_text = current_text + str(button)
            self.entry.delete(0, END)
            self.entry.insert(0, new_text)

if __name__ == "__main__":
    root = Tk()
    calculator = CalculatorApp(root)
    root.mainloop()
    