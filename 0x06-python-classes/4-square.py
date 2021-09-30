#!/usr/bin/python3
""" Defining class square"""


class Square:
    """Representing a Square"""

    def __init__(self, size):
        """Initialize a new square.

        Args:
        size (int): The size of the new square.
        """

        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
