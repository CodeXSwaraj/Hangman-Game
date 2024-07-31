import tkinter as tk
from random import choice

class Hangman:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hangman")
        self.window.geometry("300x400")

        self.word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        self.word = choice(self.word_list)
        self.guessed_letters = []
        self.missed_letters = []
        self.guessed_word = ['_'] * len(self.word)

        self.label = tk.Label(self.window, text="Hangman", font=("Arial", 24))
        self.label.pack()

        self.word_label = tk.Label(self.window, text=" ".join(self.guessed_word), font=("Arial", 18))
        self.word_label.pack()

        self.guess_entry = tk.Entry(self.window, font=("Arial", 18))
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.window, text="Guess", command=self.guess_letter)
        self.guess_button.pack()

        self.result_label = tk.Label(self.window, text="", font=("Arial", 18))
        self.result_label.pack()

        self.window.mainloop()

    def guess_letter(self):
        guess = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1:
            self.result_label.config(text="Please enter a single letter.")
            return

        if guess in self.guessed_letters or guess in self.missed_letters:
            self.result_label.config(text="You already guessed that letter.")
            return

        if guess in self.word:
            self.guessed_letters.append(guess)
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed_word[i] = guess
            self.word_label.config(text=" ".join(self.guessed_word))
            if "_" not in self.guessed_word:
                self.result_label.config(text=" Congratulations! You won!")
                self.guess_button.config(state="disabled")
        else:
            self.missed_letters.append(guess)
            self.result_label.config(text=f"Incorrect! You have {6 - len(self.missed_letters)} chances left.")
            if len(self.missed_letters) == 6:
                self.result_label.config(text=f"Game over! The word was {self.word}.")
                self.guess_button.config(state="disabled")

Hangman()