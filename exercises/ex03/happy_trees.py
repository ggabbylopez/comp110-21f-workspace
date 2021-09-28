"""Drawing forests in a loop."""

__author__ = "730407925"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
input_depth: str = input("Depth: ")
depth: int = int(input_depth)
i: int = 0
row: str = ""
while i < depth:
    row += TREE
    print(row)
    i = i + 1
    