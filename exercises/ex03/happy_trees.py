"""Drawing forests in a loop."""

__author__ = "730407925"

# The string constant for the pine tree emoji
from typing import Counter


TREE: str = '\U0001F332'
input_depth: str = input("Depth: ")
depth: int = int(input_depth)
i: int = 0
count: str = ""
while i < depth:
    count += TREE
    print(count)
    i = i + 1
    