"""Repeating a beat in a loop."""

__author__ = "730407925"


# Begin your solution here...
beat: str = input("What beat do you want to repeat?")
numberstr: str = input("How many times do you want to repeat it")
number = int(numberstr)
final_beat: str = beat
if number <= 0:
    print("No beat...")
else: 
    count: int = 0 
    while count < number - 1:
        if count == number - 1: 
            beat = beat + final_beat
        else:
            beat = beat + " " + final_beat
        count = count + 1
    print(beat)