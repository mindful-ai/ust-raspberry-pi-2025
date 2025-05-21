# gui.py
import tkinter as tk
from tkinter import messagebox

class WordJumbleGUI:
    def __init__(self, root, game):
        self.game = game
        self.root = root
        self.root.title("Word Jumble Game")

        self.label = tk.Label(root, text="Guess the word:", font=("Arial", 16))
        self.label.pack(pady=10)

        self.jumbled_label = tk.Label(root, text=self.game.get_jumbled(), font=("Arial", 20, "bold"))
        self.jumbled_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check", command=self.check_answer)
        self.check_button.pack(pady=5)

    def check_answer(self):
        user_input = self.entry.get()
        correct = self.game.check_answer(user_input)

        if correct:
            messagebox.showinfo("Correct!", "Well done! That's the right word.")
        else:
            messagebox.showerror("Wrong!", f"Oops! The correct word was: {self.game.get_answer()}")

        self.entry.delete(0, tk.END)

        if self.game.is_finished():
            self.end_game()
        else:
            self.jumbled_label.config(text=self.game.get_jumbled())

    def end_game(self):
        score = self.game.get_score()
        messagebox.showinfo("Game Over", f"Your final score is {score} out of {len(self.game.all_words)}.")
        self.jumbled_label.config(text="Game Over!")
        self.entry.config(state='disabled')
        self.check_button.config(state='disabled')
