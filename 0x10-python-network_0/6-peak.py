#!/usr/bin/python3
"""Inside the module"""


def find_peak(list_of_integers):
    """Inside function.

    Arguments:
        list_of_integers (list)
    Return int
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    elif n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)
    else:
        mid = n // 2
        if list_of_integers[mid] < list_of_integers[mid - 1]:
            return find_peak(list_of_integers[:mid])
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            return find_peak(list_of_integers[mid + 1:])
        else:
            return list_of_integers[mid]
