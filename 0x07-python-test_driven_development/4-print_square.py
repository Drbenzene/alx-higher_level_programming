#!/bin/usr/python3
"""Function that prints a square"""

def print_square(size):
    """
    Prints A Square

    Args: 
    size = Size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif not isinstance(size, (float)) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for i in range(size):
                print("#", end="")
            print()



