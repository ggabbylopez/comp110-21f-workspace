"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730407925"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

i = randint(1, 4)
print("Your fortune cookie says...")

if (i == 1): 
    print("You will pass all your classes")
else:
    if (i == 2): 
        print("Keep your heart open love is on its way!")
    else:
        if (i == 3): 
            print("Your world is about to change")
        else:
            print("You will be prosperous!")

print("Now, go spread positive vibes!")