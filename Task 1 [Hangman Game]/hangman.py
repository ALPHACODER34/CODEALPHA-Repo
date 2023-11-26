from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

class HangmanGame:
    def __init__(self, window):
        self.window = window
        self.window.title('Hangman - GUESS CITIES NAME')
        self.word_list = ['MUMBAI', 'DELHI', 'BANGALORE', 'HYDERABAD', 'AHMEDABAD', 'CHENNAI', 'KOLKATA', 'SURAT', 'PUNE',
                          'JAIPUR', 'AMRITSAR', 'ALLAHABAD', 'RANCHI', 'LUCKNOW', 'KANPUR', 'NAGPUR', 'INDORE', 'THANE',
                          'BHOPAL', 'PATNA', 'GHAZIABAD', 'AGRA', 'FARIDABAD', 'MEERUT', 'RAJKOT', 'VARANASI', 'SRINAGAR',
                          'RAIPUR', 'KOTA', 'JHANSI']

        self.photos = [PhotoImage(file=f"images/hang{i}.png") for i in range(12)]

        self.numberOfGuesses = 0
        self.the_word_with_spaces = ""
        self.lblWord = StringVar()

        self.imgLabel = Label(self.window)
        self.imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

        Label(self.window, textvariable=self.lblWord, font=('consolas 24 bold')).grid(row=0, column=3, columnspan=6, padx=10)

        n = 0
        for c in ascii_uppercase:
            Button(self.window, text=c, command=lambda c=c: self.guess(c), font=('Helvetica 18'), width=4).grid(row=1 + n // 9, column=n % 9)
            n += 1

        Button(self.window, text="New\nGame", command=self.new_game, font=("Helvetica 10 bold")).grid(row=3, column=8)

        self.new_game()

    def new_game(self):
        self.numberOfGuesses = 0
        self.the_word_with_spaces = random.choice(self.word_list)
        self.lblWord.set(' '.join("_" * len(self.the_word_with_spaces)))
        self.imgLabel.config(image=self.photos[0])

    def guess(self, letter):
        if self.numberOfGuesses < 11:
            txt = list(self.the_word_with_spaces)
            guessed = list(self.lblWord.get())
            if self.the_word_with_spaces.count(letter) > 0:
                for c in range(len(txt)):
                    if txt[c] == letter:
                        guessed[c] = letter
                self.lblWord.set("".join(guessed))
                if self.lblWord.get() == self.the_word_with_spaces:
                    messagebox.showinfo("Hangman", "YOU WON THE GAME")
            else:
                self.numberOfGuesses += 1
                self.imgLabel.config(image=self.photos[self.numberOfGuesses])
                if self.numberOfGuesses == 11:
                    messagebox.showwarning("Hangman", "GAME-OVER")

if __name__ == "__main__":
    window = Tk()
    hangman_game = HangmanGame(window)
    window.mainloop()
