from tkinter import *
from logic import *

window = Tk()
window.title("My First GUI")

window.geometry("600x400")
window.minsize(300, 200)
window.maxsize(800, 600)
window.config(bg="lightblue")
window.resizable(width=True, height=True)


# ------------------------ Button 1 -------------------------- #

# Button
button1 = Button(window, text="Print", command=lambda: print("Button Clicked!"))
button1.place(x=100, y=50, width=80, height=20)  # in terms of pixels
button1.pack(pady=20)

# Label
label1 = Label(window, text="Print 1", bg="lightblue", font=("Arial", 16))
label1.pack(pady=20)  # Add some padding around the label
label1.place(x=50, y=50)  # Place the label at specific coordinates

# Read entry value and print it when button is clicked
def on_button1_click():
    print(f"Button 1 clicked")
    print1()

button1.config(command=on_button1_click)  # Update button command to use the new function

# ------------------------ Button 2 -------------------------- #

# Button
button2 = Button(window, text="Print", command=lambda: print("Button Clicked!"))
button2.place(x=100, y=100, width=80, height=20)
button2.pack(pady=20)

# Label
label2 = Label(window, text="Print 2", bg="lightblue", font=("Arial", 16))
label2.pack(pady=20)  # Add some padding around the label
label2.place(x=50, y=100)  # Place the label at specific coordinates

# Read entry value and print it when button is clicked
def on_button2_click():
    print(f"Button 2 clicked")
    print2()

button2.config(command=on_button2_click)  # Update button command to use the new function


# ------------------------ Button 3 -------------------------- #

# Button
button3 = Button(window, text="Print", command=lambda: print("Button Clicked!"))
button3.place(x=100, y=150)
button3.pack(pady=20)

# Label
label3 = Label(window, text="Print 3", bg="lightblue", font=("Arial", 16))
label3.pack(pady=20)  # Add some padding around the label
label3.place(x=50, y=150, width=80, height=20)  # Place the label at specific coordinates

# Read entry value and print it when button is clicked
def on_button3_click():
    print(f"Button 3 clicked")
    print3()

button3.config(command=on_button3_click)  # Update button command to use the new function



