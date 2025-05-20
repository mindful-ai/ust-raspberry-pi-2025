from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("My First GUI")

window.geometry("600x400")
window.minsize(300, 200)
window.maxsize(800, 600)
window.config(bg="lightblue")
window.resizable(width=True, height=True)

# window.iconbitmap("icon.ico")  # Uncomment this line to set a custom icon

# Button
button = Button(window, text="Click Me", command=lambda: print("Button Clicked!"))

# Label
label = Label(window, text="Hello, Tkinter!", bg="lightblue", font=("Arial", 16))
label.pack(pady=20)  # Add some padding around the label
label.place(x=50, y=50)  # Place the label at specific coordinates

# Text Entry
entry = Entry(window, width=30)
entry.place(x=50, y=100)  # Place the entry at specific coordinates
entry.insert(0, "Type something here...")  # Default text in the entry

# Read entry value and print it when button is clicked
def on_button_click():
    entry_value = entry.get()
    print(f"Entry Value: {entry_value}")

button.config(command=on_button_click)  # Update button command to use the new function

# Radio buttons with male and female options with variable v0 
# label for radio buttons
label_radio = Label(window, text="Select Gender", bg="lightblue", font=("Arial", 10))
label_radio.place(x=50, y=120)  # Place the label at specific coordinates
v0 = IntVar()  # Variable to hold the value of the selected radio button
v0.set(1)  # Set default value to 1 
r1 = Radiobutton(window, text='male', value=1, bg="lightblue", variable=v0, command=lambda: print(f"Selected Radio Button Value: {v0.get()}"))  
r2 = Radiobutton(window, text='female', value=2, bg="lightblue", variable=v0, command=lambda: print(f"Selected Radio Button Value: {v0.get()}"))
r1.place(x=50, y=150)  # Place the radio button at specific coordinates
r2.place(x=50, y=180)  # Place the radio button at specific coordinates

# Read v0 value and print it when radio button is clicked
def on_radio_click():
    selected_value = v0.get()
    print(f"Selected Radio Button Value: {selected_value}")

# Updates to the radio button command    
r1.config(command=on_radio_click)  # Update radio button command to use the new function
r2.config(command=on_radio_click)  # Update radio button command to use the new function

# Checkbutton with options for "Cricket", "Football", "Badminton", "Chess" with variable v1, v2, v3 and v4
# label for check buttons
label_check = Label(window, text="Select Sports", bg="lightblue", font=("Arial", 10))
label_check.place(x=50, y=200)  # Place the label at specific coordinates
v1 = IntVar()  # Variable to hold the value of the selected check button
v2 = IntVar()  # Variable to hold the value of the selected check button
v3 = IntVar()  # Variable to hold the value of the selected check button
v4 = IntVar()  # Variable to hold the value of the selected check button
c1 = Checkbutton(window, text='Cricket', variable=v1, bg="lightblue", command=lambda: print(f"Selected Check Button Value: {v1.get()}"))
c2 = Checkbutton(window, text='Football', variable=v2, bg="lightblue", command=lambda: print(f"Selected Check Button Value: {v2.get()}"))
c3 = Checkbutton(window, text='Badminton', variable=v3, bg="lightblue", command=lambda: print(f"Selected Check Button Value: {v3.get()}"))
c4 = Checkbutton(window, text='Chess', variable=v4, bg="lightblue", command=lambda: print(f"Selected Check Button Value: {v4.get()}"))
c1.place(x=50, y=210 + 20)  # Place the check button at specific coordinates
c2.place(x=50, y=240 + 20)  # Place the check button at specific coordinates
c3.place(x=50, y=270 + 20)  # Place the check button at specific coordinates
c4.place(x=50, y=300 + 20)  # Place the check button at specific coordinates

# Read v1, v2, v3 and v4 values and print it when check button is clicked  
def on_check_click():
    selected_values = [v1.get(), v2.get(), v3.get(), v4.get()]
    options = ["Cricket", "Football", "Badminton", "Chess"]
    selected_options = [options[i] for i, value in enumerate(selected_values) if value == 1]
    print(f"Selected Check Button Values: {selected_options}")

# Re-configure the check button command to use the new function
c1.config(command=on_check_click)  # Update check button command to use the new function
c2.config(command=on_check_click)  # Update check button command to use the new function
c3.config(command=on_check_click)  # Update check button command to use the new function
c4.config(command=on_check_click)  # Update check button command to use the new function


# Listbox with options for "Python", "Java", "C++", "JavaScript" with variable v5
# label for list box
label_list = Label(window, text="Select Language", bg="lightblue", font=("Arial", 10))
label_list.place(x=250, y=100)  # Place the label at specific coordinates
v5 = StringVar()  # Variable to hold the value of the selected list box
listbox = Listbox(window, listvariable=v5, height=4, selectmode=SINGLE, bg="lightblue")
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.insert(4, "JavaScript")
listbox.place(x=250, y=120)  # Place the list box at specific coordinates


# Read v5 value and print it when list box is clicked
def on_listbox_click(event):
    selected_value = listbox.get(listbox.curselection())  # Get the selected value from the list box
    print(f"Selected List Box Value: {selected_value}")
#listbox.config(command=on_listbox_click)  # Update list box command to use the new function
listbox.bind("<<ListboxSelect>>", on_listbox_click)  # Bind the list box selection event to the function

# Combobox with options for "Red", "Green", "Blue", "Yellow" with variable v6
# label for combo box
label_combo = Label(window, text="Select Color", bg="lightblue", font=("Arial", 10))
label_combo.place(x=250, y=200)  # Place the label at specific coordinates
v6 = StringVar()  # Variable to hold the value of the selected combo box
combo = Combobox(window, textvariable=v6, state="readonly", width=15)
combo['values'] = ("Red", "Green", "Blue", "Yellow")
combo.current(0)  # Set default value to "Red"
combo.place(x=250, y=220)  # Place the combo box at specific coordinates
# Read v6 value and print it when combo box is clicked
def on_combobox_click(event):
    selected_value = combo.get()  # Get the selected value from the combo box
    print(f"Selected Combo Box Value: {selected_value}")
combo.bind("<<ComboboxSelected>>", on_combobox_click)  # Bind the combo box selection event to the function

# Listboc with option for physics, chemistry, maths, biology with variable v7
# label for list box
label_list2 = Label(window, text="Select Subject", bg="lightblue", font=("Arial", 10))
label_list2.place(x=250, y=300)  # Place the label at specific coordinates
v7 = StringVar()  # Variable to hold the value of the selected list box
listbox2 = Listbox(window, listvariable=v7, height=4, selectmode='multiple', bg="lightblue")
listbox2.insert(1, "Physics")
listbox2.insert(2, "Chemistry")
listbox2.insert(3, "Maths")
listbox2.insert(4, "Biology")
listbox2.place(x=250, y=320)  # Place the list box at specific coordinates
# Read v7 value and print it when list box is clicked
def on_listbox2_click(event):
    selected_indices = listbox2.curselection()  # Get the selected indices from the list box
    selected_values = [listbox2.get(i) for i in selected_indices]  # Get the selected values from the list box
    print(f"Selected List Box 2 Values: {selected_values}")
listbox2.bind("<<ListboxSelect>>", on_listbox2_click)  # Bind the list box selection event to the function

# Add a button to close the window
def close_window():
    window.destroy()
close_button = Button(window, text="Close", command=close_window)
close_button.place(x=500, y=350)  # Place the close button at specific coordinates


if __name__ == "__main__":
    button.pack(pady=20)  # Add some padding around the button
    window.mainloop()