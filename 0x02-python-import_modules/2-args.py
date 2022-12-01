#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    lens = len(argv[1:])

    if lens == 0:
        print(f"{lens} arguments.")

    else:
        if lens == 1:
            print(f"{lens} argument:")
        else:
            print(f"{lens} arguments:")

        for idx, value in enumerate(argv[1:], start=1):
            print(f"{idx}: {value}")
