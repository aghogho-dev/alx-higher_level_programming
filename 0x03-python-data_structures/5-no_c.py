#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for ele in my_string:
        if ele not in "Cc":
            new_string += ele
    return new_string
