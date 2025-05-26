# pip install ttkbootstrap

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def main():
    # Create main application window with dark theme
    root = ttk.Window(themename="superhero")  # Other themes: 'cyborg', 'superhero', 'solar'

    root.title("Multi-Tabbed Dark Theme App")
    root.geometry("600x400")

    # Create a notebook (tab control)
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # Tab 1
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text='Home')

    ttk.Label(tab1, text="Welcome to the Home Tab!", font=('Helvetica', 14)).pack(pady=20)
    ttk.Button(tab1, text="Click Me").pack()

    # Tab 2
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text='Settings')

    ttk.Label(tab2, text="Settings Panel", font=('Helvetica', 14)).pack(pady=20)
    ttk.Checkbutton(tab2, text="Enable notifications").pack(pady=5)
    ttk.Checkbutton(tab2, text="Dark mode").pack(pady=5)

    # Tab 3
    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text='About')

    ttk.Label(tab3, text="Multi-tab App using Tkinter and ttkbootstrap", wraplength=400).pack(pady=30)
    ttk.Button(tab3, text="Close", command=root.destroy).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
