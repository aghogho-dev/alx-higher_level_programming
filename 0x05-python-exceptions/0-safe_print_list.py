#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for idx in range(x):
            print(my_list[idx], end="")
            n += 1
    except IndexError:
        pass
    finally:
        print()
    return n
