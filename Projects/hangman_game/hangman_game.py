from os import system
from random import shuffle

def show_options_menu():
    OPTIONS = ("0", "1", "2")
    input_message = "Introduce an option (number): "
    option = -1
    while option not in OPTIONS:
        system("clear")
        print("=======")
        print("HANGMAN!")
        print("=======")
        print("0. Start")
        print("1. Ranking")
        print("2. Exit")
        print("=======")
        option = input(input_message)
        if option not in OPTIONS:
            input_message = "Please, introduce a valid option (0, 1 or 2): "
    return option


def load_words():
    with open("data.txt", "r", encoding="utf-8") as f:
        words = [line.strip().upper() for line in f]
    shuffle(words)
    return words


def get_letter_index(_word):
    indexes = {letter: [] for letter in _word}
    idx = 0
    for letter in _word:
        indexes.get(letter).append(idx)
        idx += 1
    return indexes


def replace_values_in_list(_list, _indexes, _value):
    for idx in _indexes:
        _list[idx] = _value
    return _list


def get_hangman(_lines):
    if _lines == 0: return ""
    hangman = """
               (    )
             (        )
               (    )
                |  |
                |  |
    ( ) ------- |  |
    \\ /         |  |
     |          |  |
    / \\         |  |"""
    idx = 0
    blocks = 0
    for letter in hangman:
        if letter == "\n":
            blocks += 1
        idx += 1
        if blocks == _lines:
            return hangman[:idx]
    return hangman


def run_level(_level, _word):
    points = 0
    miss = 0
    input_message = "Introduce a letter: "
    level_points = len(_word)
    level_output = ["_ " for letter in _word]
    word_letters_index = get_letter_index(_word)
    while points < level_points and miss < 11:
        system("clear")
        print("=======")
        print("LEVEL:", _level)
        print("WORD LENGTH:", level_points)
        print("MISS:", miss, "/ 10")
        print("WORD:","".join(level_output))
        print("")
        print(get_hangman(miss))
        print("=======")
        letter = input(input_message)
        if letter.isalpha() and len(letter) == 1:
            letter = letter.upper()
            if letter in _word:
                if not letter in "".join(level_output): 
                    points += 1
                    level_output = replace_values_in_list(level_output, word_letters_index.get(letter), letter)
            else:
                miss += 1
            input_message = "Introduce a letter: "
        else:
            input_message = "Invalid input, please introduce a letter: "

    if miss > 10:
        return -1
    else:
        return _level+1


def run_game():
    words_to_guess = load_words()
    final_level = len(words_to_guess)
    state = 0
    current_level = 0
    while state != -1:
        state = run_level(current_level, words_to_guess[current_level])
        if state > -1:
            current_level = state
    # END GAME 
    if state == -1:
        system("clear")
        print("============")
        print("YOU LOSE :(")
        print("LEVEL:", current_level)

def run():
    option = int(show_options_menu())
    if option == 0:
        run_game()
    elif option == 1:
        show_ranking()
    else:
        print("Closing...")


if __name__ == '__main__':
    run()