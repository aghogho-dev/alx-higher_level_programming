#!/usr/bin/python3
"""The Base class module."""


class Base:
    """Inside the base class.

    Attributes:
        __nb_objects (int): count instantiated obj.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base class instance.

        Args:
            id (int): id of class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
