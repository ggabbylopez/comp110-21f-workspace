"""An exercise in remainders and boolean logic."""

__author__ = "730407925"

prompt: int = int(input("Enter an int: "))

if (prompt % 2 == 0 and prompt % 7 == 0):
    print("TAR HEELS")
elif prompt % 2 == 0:
        print("TAR")
elif prompt % 7 == 0:
    print("HEELS")
else:
    print("CAROlINA")