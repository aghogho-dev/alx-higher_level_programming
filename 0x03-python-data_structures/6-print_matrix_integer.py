#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for one_list in matrix:
        if not one_list:
            print("{}".format(""))
            break
        lens = len(one_list) - 1
        for idx, ele in enumerate(one_list):
            if idx != lens:
                print("{:d}".format(ele), end=" ")
            else:
                print("{:d}".format(ele))
