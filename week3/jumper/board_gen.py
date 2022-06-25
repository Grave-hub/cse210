import random
from guesser import Guesser
#picks a word form the provided list to be used int he director
word_list = ["SAMSON", "AMULEK", "SAMUEL", "MORMON", "MORONI", "HAGOTH"]
key_word = random.choice(word_list)
#generates visuals in terminal of parachute based on how many incorrect guesses there are. You get 5-6 chances
class Boardgen:
    def __init__(self):
        self.key_word = key_word
    def generate_board(self, wrong_guesses, right_guesses):
        board = ["", "   ___   ", "  /___\\  ", "  \\   /  ", "   \ /   ", "    0    ", "   /|\\   \n   / \\   \n _ _ _ _ _ _"]
        self.wrong_guesses = wrong_guesses
        self.right_guesses = right_guesses
        if self.wrong_guesses == 0:
            for line in board:
                print(line)
        elif self.wrong_guesses == 1:
            for line in range(len(board)):
                print(board[line])
        elif self.wrong_guesses == 2:
            print(board[0])
            for line in range(2,7):
                print(board[line])
        elif self.wrong_guesses == 3:
            print(board[0])
            for line in range(3,7):
                print(board[line])
        elif self.wrong_guesses == 4:
            print(board[0])
            for line in range(4,7):
                print(board[line])
        elif self.wrong_guesses == 5:
            print(board[0])
            print(f"\n    x   ")
            for line in range(6,7):
                print(board[line])
                print("\n You lose!")
    def make_key_word(self):
        key_word = self.key_word