import random

#converts random word into a list item which could be used to display correct letters guessed so far at the top of the program
class Guesser:
    def __init__(self):
        pass
    def rand_word(random_word):
        word_list = ["SAMSON", "AMULEK", "SAMUEL", "MORMON", "MORONI", "HAGOTH"]
        random_word = random.choice(word_list)
        list_word = list(random_word)
        return random_word
