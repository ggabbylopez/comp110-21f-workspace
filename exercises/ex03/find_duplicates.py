"""Finding duplicate letters in a word."""

__author__ = "123456789"

word: str = str(input("Enter a word: "))
i: int = 0
j: int = 0
output: bool = False
while i < len(word):
    j = i + 1
    while j < len(word):
        if word[i] == word[j]:
            output = True
        j += 1
    i += 1
        
print ("Found duplicate: " + str(output))