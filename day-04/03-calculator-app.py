# Calculator app using Tkinter

from tkinter import *

class CalculatorApp:

    def __init__(self, master):
        # Entry field
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("400x600")
        self.master.config(bg="lightblue")
        self.master.resizable(width=False, height=False)
        
        # Two entry fields with labels Operand1 and Operand2
        self.label1 = Label(master, text="Operand 1", bg="lightblue", font=("Arial", 12))
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        self.entry1 = Entry(master, width=16, font=("Arial", 24), bd=10, insertwidth=2, justify='right')
        self.entry1.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        self.label2 = Label(master, text="Operand 2", bg="lightblue", font=("Arial", 12))
        self.label2.grid(row=1, column=0, padx=10, pady=10)
        self.entry2 = Entry(master, width=16, font=("Arial", 24), bd=10, insertwidth=2, justify='right')
        self.entry2.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        # Four Radio buttons for operations addition, subtraction, multiplication and division
        self.label_op = Label(master, text="Select Operation", bg="lightblue", font=("Arial", 12))
        self.label_op.grid(row=2, column=0, padx=10, pady=10)
        self.v_op = StringVar()
        self.v_op.set("add")
        self.r1 = Radiobutton(master, text='Add', value='add', bg="lightblue", variable=self.v_op, font=("Arial", 12))
        self.r1.select()  # Set default selection
        self.r2 = Radiobutton(master, text='Subtract', value='subtract', bg="lightblue", variable=self.v_op, font=("Arial", 12))
        self.r3 = Radiobutton(master, text='Multiply', value='multiply', bg="lightblue", variable=self.v_op, font=("Arial", 12))
        self.r4 = Radiobutton(master, text='Divide', value='divide', bg="lightblue", variable=self.v_op, font=("Arial", 12))
        self.r1.grid(row=2, column=1, padx=10, pady=10)
        self.r2.grid(row=2, column=2, padx=10, pady=10)
        self.r3.grid(row=2, column=3, padx=10, pady=10)
        self.r4.grid(row=2, column=4, padx=10, pady=10)

        # Button to calculate result
        self.button = Button(master, text="Calculate", padx=20, pady=20, font=("Arial", 18), command=self.calculate)
        self.button.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        # Label with large font to display result
        self.label_result = Label(master, text="Result", bg="lightblue", font=("Arial", 12))
        self.label_result.grid(row=4, column=0, padx=10, pady=10)
        self.result = Label(master, text="", bg="lightblue", font=("Arial", 24))
        self.result.grid(row=4, column=1, columnspan=3, padx=10, pady=10)

        # Adjust goemetry of the window
        self.master.geometry("600x400")

    # Calculate function to perform the operation based on selected radio button
    def calculate(self):
        try:
            operand1 = float(self.entry1.get())
            operand2 = float(self.entry2.get())
            operation = self.v_op.get()

            if operation == 'add':
                result = operand1 + operand2
            elif operation == 'subtract':
                result = operand1 - operand2
            elif operation == 'multiply':
                result = operand1 * operand2
            elif operation == 'divide':
                result = operand1 / operand2

            self.result.config(text=str(result))
        except Exception as e:
            self.result.config(text="Error")

if __name__ == "__main__":
    root1 = Tk()
    root1.title("Calculator 1")
    calculator1 = CalculatorApp(root1)
    root1.mainloop()



