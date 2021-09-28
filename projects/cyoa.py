"""This is a game designed to make the player guess a random number."""

__author__ = "730407925"
from random import randint
"""Emojis"""
smiley_face: str = '\U0001F601'
winky_face: str = '\U0001F609'
celebration: str = '\U0001F389'
thumbs_up: str = '\U0001F44D'
sparkles: str = '\U00002728'

points: int
player: str


def greet() -> None:
    """This function is used to greet the player and ask their name."""
    player = input("Player what is your name? ")
    print(f"Welcome {player}! You are playing a number guessing game! I have chosen a random number 1-10 and you get as many tries as it takes to figure it out! Good luck! The less points you get the better you are! {sparkles}{smiley_face}")
    return None


def guess() -> None:  
    """This is the main game function and the player will input their guesses of the random number."""
    num_guess: str = input("Enter your first guess: ")
    num_rand: int = randint(1, 10)
    num = int(num_guess)
    i: int = 0 
    points = 0
    print(num_rand)
    while (i == 0):
        if num != num_rand:
            points += 1
            num_guess = input(f"Aw good try! Keep guessing!{winky_face}: ")
            num = int(num_guess)
            print(f"you have {points} points!")
        else:
            print(f"Great job, you ended the game with {points} points{celebration}")
            i -= 1
    return None


def play_again() -> None:
    """This function asks whether the player wants to play again."""
    play_again_q = input("Do you want to play again? yes or no? ")
    x = play_again_q
    if x == "yes":
        return main()
    else:
        print(f"game over! See you next time! {thumbs_up}")
    return None
  

def bonus(points: int) -> str:
    """Function designed to congratulate winners!"""
    if points == 0: 
        return ("Wow you got the answer on your first try!")
    else: 
        return "Dang it took you a few tries!"


def main() -> None:
    """The main function is used to run all of the defined functions."""
    greet()
    guess() 
    play_again()
    return None


if __name__ == "__main__":
    main()
  
  
