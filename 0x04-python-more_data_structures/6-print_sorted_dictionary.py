#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = map(lambda x: "{}: {}".format(x, a_dictionary.get(x)), sorted(a_dictionary))
    for one in list(a):
        print(one)
