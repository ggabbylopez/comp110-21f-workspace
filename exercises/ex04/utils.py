"""List utility functions."""

__author__ = "730407925"


# TODO: Implement your functions here.
def all(x: list[int], y: int) -> bool:
    """Function will return false if numbers checked do not match y val."""
    i: int = 0
    while i < len(x):
        if x[i] == y:
            i += 1
        else:
            return False
    return True


def is_equal(x: list[int], y: list[int]) -> bool:
    """Function will return True if both lists are equal."""
    i: int = 0
    if len(x) == len(y):
        while i < len(x): 
            if x[i] == y[i]:
                i += 1
            else:
                return False
    else: 
        return False
    return True


def max(input: list[int]) -> int:
    """Function will return largest integer in list."""
    i: int = 0
    m: int = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(input):
        if m < input[i]:
            m = input[i]
        i += 1
    return m


def main() -> None: 
    print
    print(max([1, 2, 3, 4, 5, 8, 9]))


main()