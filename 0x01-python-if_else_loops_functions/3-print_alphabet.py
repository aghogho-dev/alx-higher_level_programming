#!/usr/bin/python3
i = 97
while True:
    if chr(i) > 'z':
        break
    if (chr(i) != 'e' and chr(i) != 'q'):
        print("{}".format(chr(i)), end="")
    i += 1
