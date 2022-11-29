#!/usr/bin/python3
def islower(c):
    if not c:
        raise Exception

    if c >= 'a' and c <= 'z':
        return True
    return False
