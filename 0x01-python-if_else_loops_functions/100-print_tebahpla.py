#!/usr/bin/python3
for idx, v in enumerate(list(range(ord('z'), ord('a') - 1, -1))):
    if idx % 2 == 0:
        print(chr(v), end="")
    else:
        print("{}".format(chr(v - 32)), end="")
