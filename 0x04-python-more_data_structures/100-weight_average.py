#!/src/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    products = sum(map(lambda x: x[0] * x[1], my_list))
    sum_wt = sum(map(lambda x: x[1], my_list))
    return products / sum_wt
