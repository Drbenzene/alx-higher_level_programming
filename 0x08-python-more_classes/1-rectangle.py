#!/usr/bin/python3
"""Define a class Rectangle"""

class Rectangle:
    """Representing a Reactangle"""
     def __init__(self, width=0, height=0):
        """Initialize a new Square.

        Args:
        width = width of the rectangle
        height = Height of the rectangle

        Size of the new Square."""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return the width of the rectangle"""
        return(self.__width)

    @width.setter
    def width(self, value):
        if isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the Rectangle"""
        return(self.__height)

    @height.setter
    def height(self, value):
        if isinstance(height, int):
            raise TypeError("width must be an integer")
        elif height < 0:
            raise ValueError("width must be >= 0")
        self.__height = value