#!/usr/bin/python3
"""The Rectangle module."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inside the Rectangle class."""

    def __init__(self, width, height):
        """Iintialize Rectange.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        
        self.__width = width
        self.__height = height

    def area(self):
        """Cal area of Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """String representation."""
        return "[{}] {}/{}".format(str(self.__class__.__name__), self.__width, self.__height)
