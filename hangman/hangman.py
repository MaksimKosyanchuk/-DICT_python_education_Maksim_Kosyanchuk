"""random module, copy module, colorama module"""
import random
import copy
from colorama import init
from colorama import Fore, Back, Style #pylint: disable=W0611
init()

vocabluary = ["python", "java", "javascript", "typescript", "assembler", "php"]


def check_win(visible_word_list):
    """check win func"""
    try:
        index_value = visible_word_list.index("-")
    except ValueError:
        index_value = -1
    return index_value


def change_visible_word(user_letter, game_word_list, visible_word_list):
    """change visible word"""
    game_word_len = len(game_word_list)
    for index in range(game_word_len):
        if game_word_list[index] == user_letter:
            visible_word_list[index] = user_letter
    return visible_word_list


def first_invert(visible_word, visible_word_list):
    """invert on firstly"""
    visible_word_len = len(visible_word_list)
    for index in range(visible_word_len):
        visible_word_list[index] = "-"
    visible_word = join_list(visible_word, visible_word_list)

    return visible_word


def join_list(visible_word, visible_word_list):
    """join list"""
    visible_word = "".join(visible_word_list)
    return visible_word


def check_letter(user_letter, word_list):
    """check user letter"""
    try:
        index_value = word_list.index(user_letter)
    except ValueError:
        index_value = -1

    if index_value == -1:
        print("That letter doesn't appear in the word")
        my_return = -1

    else:
        my_return = user_letter

    return my_return

def my_input(user_vocabluary):
    """input user letter"""
    cycle_var = True
    while cycle_var:
        user_letter = input("\nInput a letter: ")
        if len(user_letter) > 1 and user_letter == " " and user_letter == "":
            print("Please, input only 1 symbol")
            my_input(user_vocabluary)

        try:
            index_value = user_vocabluary.index(user_letter)
        except ValueError:
            index_value = -1

        if index_value == -1:
            cycle_var = False
        else:
            print("You've already guessed this letter")

    return user_letter

def game_play():
    """main func"""
    win = 0
    user_letter = None
    vocabluary_index = random.randint(0, len(vocabluary))
    user_vocabluary = []
    game_word = vocabluary[vocabluary_index]
    word_list = list(game_word)
    visible_word = game_word
    visible_word_list = copy.copy(word_list)
    visible_word = game_word
    visible_word = first_invert(visible_word, visible_word_list)
    attempts = 0

    while attempts < 8:
        print("Attempts: ", str(8 - attempts))
        print("\n", visible_word, "\n")
        user_letter = my_input(user_vocabluary)
        user_vocabluary.append(user_letter)
        guessed = check_letter(user_letter, word_list)

        if guessed == -1:
            attempts += 1

        else:
            visible_word_list = change_visible_word(user_letter,word_list, visible_word_list)
            visible_word = join_list(visible_word, visible_word_list)

            win = check_win(visible_word_list)
            if win == -1:
                print("\nYou " + Fore.GREEN + Style.DIM + "guessed" + Fore.RESET + " the word " + Fore.GREEN + game_word #pylint: disable=C0301
                      + Fore.RESET + "! You survived!\n")
                break
    if win != -1:
        print(Fore.RED + "You lost!\n" + Fore.RESET)
    lobby()


def lobby():
    """lobby func"""
    start_message = "Type " + Fore.GREEN + "play" + Fore.RESET + " to play the game, "\
                    + Fore.RED + "exit " + Fore.RESET + "to quit: "

    print(start_message.rstrip())
    play_variable = input(">> ")
    print("")

    if play_variable == "play":
        game_play()
    elif play_variable == "exit":
        print(Fore.RED + "Bye!")
        return
    else:
        print('Enter "play" or "exit"')
        lobby()


# Точка входа
print("HANGMAN \n\nThe game will be available soon.")
lobby()
