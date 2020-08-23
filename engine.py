from functions import Vocabulary_learning
from language_choice import Language
from tkinter import *
import time

while True:
    localtime = time.asctime(time.localtime(time.time()))
    wrong_answers = [localtime]

    program = Vocabulary_learning()

    tk = Tk()
    choose_language = Language(tk)
    tk.mainloop()

    choosen_language = choose_language.choosen_language
    print(f'>>>>> Wybrałeś język {choosen_language}')

    if choosen_language == 'angielski':
        program.set_english_language()
    else:
        program.set_polish_language()

    while True:
        my_word = program.get_word()
        print(f'>>>>> Pozostało słów: {len(program.all_words)}')
        print(f'>>>>> Wylosowane słowo >>>>> {my_word[program.index[0]]}')
        answer = program.get_answer()
        if answer == my_word[program.index[1]]:
            print('>>>>> Dobrze! :)')
            program.all_words.remove(my_word)
        else:
            print('<<<<< Źle! :(')
            wrong_answers.append(f'{my_word[program.index[0]]} [{my_word[program.index[1]]}]: {answer}')
        print(f'>>>>> {program.language_to_guess} znaczenie -> {my_word[program.index[1]]}')
        print()
        if len(program.all_words) == 0:
            print('>>>>> Przerobiłeś już wszystkie słowa, zapraszam do logów :)')
            wrong_answers.append("\n")
            print('\n'.join(wrong_answers))

            file = open("logs.txt", "a+")
            file.write('\n'.join(wrong_answers))
            file.close()

            if program.ask_to_play_again():
                break
            else:
                exit(0)