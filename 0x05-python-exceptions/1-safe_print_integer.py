#!/usr/bin/python3
def safe_print_integer(value):
    answer = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        answer = False
    return answer
