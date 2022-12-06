#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return
    max_value = my_list[0]
    for ele in my_list[1:]:
        if ele > max_value:
            max_value = ele
    return max_value
