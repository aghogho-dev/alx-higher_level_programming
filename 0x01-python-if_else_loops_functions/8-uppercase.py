#!/usr/bin/python3
def uppercase(str):
    for idx, s in enumerate(str):
        if s >= 'a' and s <= 'z':
            s = "{}".format(chr(ord(s) - 32))

        if idx < len(str) - 1:
            print("{}".format(s), end="")
        else:
            print("{}".format(s))
