# game_logic.py
import random

WORDS = ["python", "developer", "jumble", "training", "interface", "computer", "keyboard"]

class WordJumbleGame:
    def __init__(self):
        self.all_words = WORDS.copy()
        random.shuffle(self.all_words)
        self.current_index = 0
        self.score = 0
        self.word = ""
        self.jumbled = ""
        self.finished = False
        self._load_next_word()

    def _load_next_word(self):
        if self.current_index < len(self.all_words):
            self.word = self.all_words[self.current_index]
            self.jumbled = self._jumble_word(self.word)
        else:
            self.finished = True

    def _jumble_word(self, word):
        word_list = list(word)
        while True:
            random.shuffle(word_list)
            jumbled = ''.join(word_list)
            if jumbled != word:
                return jumbled

    def check_answer(self, user_input):
        correct = user_input.strip().lower() == self.word.lower()
        if correct:
            self.score += 1
        self.current_index += 1
        self._load_next_word()
        return correct

    def get_jumbled(self):
        return self.jumbled

    def get_answer(self):
        return self.word

    def get_score(self):
        return self.score

    def is_finished(self):
        return self.finished
