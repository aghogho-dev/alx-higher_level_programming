#!/usr/bin/python3
"""Addition module.



"""
def add_integer(a, b=98):
    """Returns the sum of two ints.
    Raises: TypeError for types besides int and float
    """
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
