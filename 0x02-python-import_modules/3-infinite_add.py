#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    args = argv[1:]
    
    sums: int = 0

    for value in argv[1:]:
        sums += int(value)

    print(f"{sums}")
