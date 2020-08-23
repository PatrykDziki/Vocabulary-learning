from words import Words
from random import choice

class Vocabulary_learning:

    def __init__(self):

        self.all_words = Words().words_list
        self.language_to_guess = ''
        self.index = []

    def get_word(self):
        my_word = choice(self.all_words)
        return my_word
    def number_of_words_to_guess(self):
        return len(self.all_words)

    def set_english_language(self):
        self.index.append(0)
        self.index.append(1)
        self.language_to_guess = 'polskie'

    def set_polish_language(self):
        self.index.append(1)
        self.index.append(0)
        self.language_to_guess = 'angielskie'

    def get_answer(self):
        return input(f'>>>>> Podaj {self.language_to_guess} znaczenie tego słowa: ')

    def ask_to_play_again(self):
        while True:
            self.again = input(">>>>> Ćwiczymy dalej? :) [T/N] ").upper()
            if self.again == 'N':
                return False
            elif self.again == 'T':
                return True
            else:
                print("<<<<< Nieprawidłowe polecenie (T = Ćwiczymy dalej, N = Wychodzimy z aplikacji)")
