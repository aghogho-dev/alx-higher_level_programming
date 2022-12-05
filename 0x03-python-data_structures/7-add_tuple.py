#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lena = len(tuple_a)
    lenb = len(tuple_b)
    if lena >= 2 and lenb >= 2:
        a1, a2 = tuple_a[:2]
        b1, b2 = tuple_b[:2]
        return a1 + b1, a2 + b2
    elif lena == 1 and lenb == 2:
        a1 = tuple_a[0]
        b1, b2 = tuple_b
        return a1 + b1, b2
    elif lena == 2 and lenb == 1:
        a1, a2 = tuple_a
        b1 = tuple_b[0]
        return a1 + b1, a2
    elif lena == 0 and lenb:
        return tuple_b
    elif lena and lenb == 0:
        return tuple_a
    elif lena == lenb == 0:
        return (0, 0)
