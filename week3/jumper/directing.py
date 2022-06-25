from board_gen import Boardgen
from terminal_text import TextTerminal
from guesser import Guesser

#director for program
class Directing():
    def __init__(self):
        self.key_word = Guesser.rand_word(self)
        self._board_gen = Boardgen()
        self._text_terminal = TextTerminal()
        self._is_playing = True
        self._guesser = Guesser()
    #starts game and keep track of if it's playing or not based on incorrect and correct guesses
    def game_start(self, wrong_guesses, right_guesses):
        self.wrong_guesses = wrong_guesses
        self.right_guesses = right_guesses
        if wrong_guesses >= 6:
            self._is_playing = False
            self._text_terminal.text_output("Sorry you've lost!")
        elif right_guesses >= 5:
            self._is_playing = False
            self._text_terminal.text_output("Congratulations, you've won!")
        #generates board based on correct or incorrect guesses
        else:
            while self._is_playing == True:
                Boardgen.generate_board(self, self.wrong_guesses, self.right_guesses)
                self._get_input(self.key_word)
    #gets the user's guesses and stores the amount of times they are correct or wrong
    def _get_input(self, key_word):
        user_guess = self._text_terminal.text_get("\nPick a letter A-Z: ")
        self.key_word = key_word
        if user_guess.upper() in self.key_word:
            self._text_terminal.text_get(f"\n{user_guess.upper()} is in the word! ")
            self.right_guesses +=1
            if self.right_guesses == 6:
                self._text_terminal.text_output(f"The word is {self.key_word}")
                self._text_terminal.text_output("\nYou win!!!")
        else:
            self._text_terminal.text_output(f"\n{user_guess.upper()} is not in the word! ")
            self.wrong_guesses +=1
#main director that controls the director class and provides the beginning counter for the wrong and right guesses (both 0 at start)     
def main():
    direct_input = Directing()
    direct_input.game_start(0,0)    
    
if __name__ == "__main__":
    main()



