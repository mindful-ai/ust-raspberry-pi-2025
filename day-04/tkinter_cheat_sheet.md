
# ✅ Tkinter Essentials Cheat Sheet

## 📌 Import and Main Structure
```python
import tkinter as tk

root = tk.Tk()  # Create main window
root.mainloop()  # Run the event loop
```

---

## 🎨 Window Configuration
```python
root.title("Window Title")
root.geometry("300x200")  # Width x Height
root.resizable(False, False)  # Disable resize
root.configure(bg="lightblue")  # Set background color
```

---

## 🧱 Common Widgets

| Widget         | Description                          | Example |
|----------------|--------------------------------------|---------|
| `Label`        | Display text or image                | `tk.Label(root, text="Hello")` |
| `Button`       | Triggers an action                   | `tk.Button(root, text="Click", command=func)` |
| `Entry`        | Single-line text input               | `tk.Entry(root)` |
| `Text`         | Multi-line text input                | `tk.Text(root, height=5, width=20)` |
| `Checkbutton`  | Toggle option (on/off)               | `tk.Checkbutton(root, text="Accept")` |
| `Radiobutton`  | Select one option from group         | `tk.Radiobutton(root, text="A", variable=var, value="A")` |
| `Listbox`      | Display list of items                | `tk.Listbox(root)` |
| `Combobox`     | Drop-down list (from ttk)            | `ttk.Combobox(root, values=["A", "B"])` |
| `Spinbox`      | Numeric/text spinner                 | `tk.Spinbox(root, from_=0, to=10)` |
| `Scale`        | Slider to select numeric value       | `tk.Scale(root, from_=0, to=100, orient="horizontal")` |
| `Scrollbar`    | Add scroll to widgets                | `tk.Scrollbar(root)` |
| `Frame`        | Container for grouping widgets       | `tk.Frame(root)` |
| `Canvas`       | Draw shapes, lines, images           | `tk.Canvas(root, width=100, height=100)` |
| `Menu`         | Menu bar creation                    | `tk.Menu(root)` |
| `Messagebox`   | Pop-up dialogs (info, error, etc.)   | `messagebox.showinfo("Title", "Message")` |

---

## 📦 Layout Managers

### 1. `pack()`
Packs widgets in order added.
```python
label.pack(side="top", fill="x", padx=5, pady=5)
```

### 2. `grid()`
Row/column layout (better control).
```python
label.grid(row=0, column=0, padx=5, pady=5)
```

### 3. `place()`
Absolute positioning (rarely used).
```python
widget.place(x=100, y=50)
```

---

## 🔄 Variable Classes

Used with widgets like `Checkbutton`, `Radiobutton`, `Entry`, etc.

| Type           | Example                     |
|----------------|-----------------------------|
| `StringVar()`  | `var = tk.StringVar()`      |
| `IntVar()`     | `var = tk.IntVar()`         |
| `DoubleVar()`  | `var = tk.DoubleVar()`      |
| `BooleanVar()` | `var = tk.BooleanVar()`     |

---

## 🧠 Common Widget Functions

```python
entry.get()                    # Get input from Entry
entry.insert(0, "Hi")          # Insert text
entry.delete(0, tk.END)        # Clear Entry

text.get("1.0", tk.END)        # Get Text widget content
label.config(text="New")       # Update label text

listbox.insert(tk.END, "Item") # Add item to Listbox
listbox.delete(0)              # Delete first item
listbox.get(tk.ACTIVE)         # Get selected item

widget.config(bg="red")        # Change widget property
```

---

## ✨ Useful Modules

| Module                  | Use                                |
|-------------------------|-------------------------------------|
| `tkinter.messagebox`    | Alerts & confirmations             |
| `tkinter.filedialog`    | Open/save file dialogs             |
| `tkinter.colorchooser`  | Color picker dialogs               |

---

## 💡 Sample Code Snippet

```python
import tkinter as tk
from tkinter import messagebox

def greet():
    messagebox.showinfo("Hello", f"Hello {name_var.get()}!")

root = tk.Tk()
root.title("Greeter")

tk.Label(root, text="Enter your name:").pack(pady=5)
name_var = tk.StringVar()
tk.Entry(root, textvariable=name_var).pack(pady=5)

tk.Button(root, text="Greet", command=greet).pack(pady=10)
root.mainloop()
```
