"""Counting letters in a string."""

__author__ = "730407925"


# need to find how many of a letter is in a word
letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i = 0
count = 0
while i < len(word): 
    if word[i] == letter:
        count = count + 1
    i = i + 1
print("Count: " + str(count))