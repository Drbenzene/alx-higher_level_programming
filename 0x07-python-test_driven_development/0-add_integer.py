#!/usr/bin/python3
"""Adding Two Integers"""

def add_integer(a, b=98):

    """
    Add Two Integers

    Args:
    a: is a integer
    b: is a integer
    Return is the sum of the int (a + b)
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)