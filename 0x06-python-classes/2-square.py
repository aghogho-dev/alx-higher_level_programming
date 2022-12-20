#!/usr/bin/python3
"""The class Square module."""


class Square:
    """Inside the Square class."""


    def __init__(self, size=0):
        """The initialization of Square.

        Args:
            size (int): The square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must ne >= 0")
        else:
            self.__size = size
