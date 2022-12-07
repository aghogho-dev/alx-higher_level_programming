#!/src/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0 or not isinstance(my_list, list):
        return 0
    products = 0
    sum_wt = 0
    for one in my_list:
        products += one[0] * one[1]
        sum_wt += one[1]
    return products / sum_wt
