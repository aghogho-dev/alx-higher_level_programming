#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """ print(*my_list, sep='\n') also works """
    for ele in my_list:
        print("{:d}".format(ele))
