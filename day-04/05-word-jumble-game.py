import tkinter as tk
import random

class WordJumbleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Jumble Game")

        # List of original words
        self.original_words = ["python", "tkinter", "socket", "thread", "widget"]
        random.shuffle(self.original_words)  # Shuffle the list for gameplay order

        self.current_index = 0
        self.score = 0

        self.jumbled_word = tk.StringVar()
        self.user_guess = tk.StringVar()
        self.message = tk.StringVar()

        self.setup_gui()
        self.show_word()

    def setup_gui(self):
        tk.Label(self.master, text="Guess the correct word:", font=("Helvetica", 14)).pack(pady=10)

        self.word_label = tk.Label(self.master, textvariable=self.jumbled_word, font=("Helvetica", 24, "bold"))
        self.word_label.pack(pady=10)

        tk.Entry(self.master, textvariable=self.user_guess, font=("Helvetica", 14)).pack(pady=10)

        tk.Button(self.master, text="Submit", command=self.check_word, font=("Helvetica", 12)).pack(pady=5)

        self.message_label = tk.Label(self.master, textvariable=self.message, font=("Helvetica", 12))
        self.message_label.pack(pady=10)

    def jumble_word(self, word):
        word_letters = list(word)
        while True:
            random.shuffle(word_letters)
            jumbled = ''.join(word_letters)
            if jumbled != word:
                return jumbled

    def show_word(self):
        if self.current_index < len(self.original_words):
            original = self.original_words[self.current_index]
            jumbled = self.jumble_word(original)
            self.jumbled_word.set(jumbled)
            self.user_guess.set("")
            self.message.set("")
        else:
            self.end_game()

    def check_word(self):
        correct_word = self.original_words[self.current_index]
        guess = self.user_guess.get().strip().lower()

        if guess == correct_word:
            self.score += 1
            self.message.set("Correct!")
        else:
            self.message.set(f"Wrong! Correct word was: {correct_word}")

        self.current_index += 1
        #self.master.after(1000, self.show_word)
        self.show_word()

        

    def end_game(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        final_msg = f"Game Over! Your Score: {self.score}/{len(self.original_words)}"
        tk.Label(self.master, text=final_msg, font=("Helvetica", 20, "bold"), fg="blue").pack(pady=30)

if __name__ == "__main__":
    root = tk.Tk()
    game = WordJumbleGame(root)
    root.mainloop()
