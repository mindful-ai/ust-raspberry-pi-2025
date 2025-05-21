# main.py
import tkinter as tk
from game_logic import WordJumbleGame
from gui import WordJumbleGUI

def main():
    root = tk.Tk()
    game = WordJumbleGame()
    app = WordJumbleGUI(root, game)
    root.mainloop()

if __name__ == "__main__":
    main()
