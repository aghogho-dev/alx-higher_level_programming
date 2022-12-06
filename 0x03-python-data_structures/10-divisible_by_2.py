#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ans = []
    for ele in my_list:
        if ele % 2 == 0:
            ans.append(True)
        else:
            ans.append(False)
    return ans
