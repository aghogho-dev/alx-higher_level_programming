#!/usr/bin/python3
def uppercase(str):
    new = ""
    for idx, s in enumerate(str):
        if s >= 'a' and s <= 'z':
            s = "{}".format(chr(ord(s) - 32))

        new += s

    print("{}".format(new))
