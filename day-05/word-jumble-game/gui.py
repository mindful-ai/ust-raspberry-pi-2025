# gui.py
import tkinter as tk

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

        self.feedback_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
        self.feedback_label.pack(pady=10)

    def check_answer(self):
            user_input = self.entry.get()
            correct = self.game.check_answer(user_input)

            if correct:
                self.feedback_label.config(text="✅ Correct!", fg="green")
            else:
                correct_word = self.game.get_answer()
                self.feedback_label.config(text=f"❌ Wrong! Correct word was: {correct_word}", fg="red")

            self.entry.delete(0, tk.END)

            if self.game.is_finished():
                self.end_game()
            else:
                self.jumbled_label.config(text=self.game.get_jumbled())

    def end_game(self):
        # Clear all widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        final_msg = f"Game Over!\nYour Score: {self.game.get_score()} / {len(self.game.all_words)}"

        result_label = tk.Label(self.root, text=final_msg, font=("Arial", 18, "bold"), fg="purple")
        result_label.pack(pady=50)
