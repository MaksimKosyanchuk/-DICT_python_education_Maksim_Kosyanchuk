"""random module, copy module, colorama module"""
import random
import copy
from colorama import init
from colorama import Fore, Back, Style  # pylint: disable=W0611
init()


class Hangman:
    """Main program class"""
    def __init__(self):
        self.vocabulary = ["python", "java", "javascript", "typescript", "assembler", "php"]
        self.user_letter = ""
        self.vocabulary_index = random.randint(0, len(self.vocabulary))
        self.user_vocabulary = []
        self.game_word = self.vocabulary[self.vocabulary_index]
        self.game_word_list = list(self.game_word)
        self.visible_word_list = copy.copy(self.game_word_list)
        self.visible_word = self.game_word
        self.first_invert()

    def check_win(self):
        """check win func"""
        try:
            index_value = self.visible_word_list.index("-")
        except ValueError:
            index_value = -1
        return index_value

    def change_visible_word(self):
        """change visible word"""
        game_word_len = len(self.game_word_list)
        for index in range(game_word_len):
            if self.game_word_list[index] == self.user_letter:
                self.visible_word_list[index] = self.user_letter

    def first_invert(self):
        """invert on firstly"""
        visible_word_len = len(self.visible_word_list)
        for index in range(visible_word_len):
            self.visible_word_list[index] = "-"
        self.join_list()

    def join_list(self):
        """join list"""
        self.visible_word = "".join(self.visible_word_list)

    def check_letter(self):
        """check user letter"""
        try:
            index_value = self.game_word_list.index(self.user_letter)
        except ValueError:
            index_value = -1

        if index_value == -1:
            print("That letter doesn't appear in the word")
            my_return = -1

        else:
            my_return = self.user_letter
        return my_return

    def my_input(self):
        """input user letter"""
        cycle_var = True
        while cycle_var:
            self.user_letter = input("\nInput a letter: ")
            if len(self.user_letter) > 1 and self.user_letter == " " and self.user_letter == "":
                print("Please, input only 1 symbol")
                self.my_input()

            try:
                index_value = self.user_vocabulary.index(self.user_letter)
            except ValueError:
                index_value = -1

            if index_value == -1:
                cycle_var = False
            else:
                print("You've already guessed this letter")


def game_play():
    """main func"""
    win = 0
    attempts = 0
    while attempts < 8:
        print("Attempts: ", str(8 - attempts))
        print("\n", hangman.visible_word, "\n")
        hangman.my_input()
        hangman.user_vocabulary.append(hangman.user_letter)
        guessed = hangman.check_letter()

        if guessed == -1:
            attempts += 1
        else:
            hangman.change_visible_word()
            hangman.join_list()
            win = hangman.check_win()
            if win == -1:
                print("\nYou " + Fore.GREEN + Style.DIM + "guessed" + Fore.RESET + " the word " + Fore.GREEN + hangman.game_word #pylint: disable=C0301
                      + Fore.RESET + "! You survived!\n")
                break
    if win != -1:
        print(Fore.RED + "You lost!\n" + Fore.RESET)
    lobby()


def lobby():
    """lobby func"""
    start_message = "Type " + Fore.GREEN + "play" + Fore.RESET + " to play the game, " \
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


hangman = Hangman()

# Точка входа
print("HANGMAN \n\nThe game will be available soon.")
lobby()
