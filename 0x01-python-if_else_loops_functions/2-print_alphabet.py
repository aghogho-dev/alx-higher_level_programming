#!/usr/bin/python3
i = 97
while True:
    if chr(i) > 'z':
        break
    print(chr(i), end="")
    i += 1
