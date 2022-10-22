#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    count = 0
    total = 0
    for i in my_list:
        total = total + (i[0] * i[1])
        count = count + (i[1])
    if count == 0:
        return 0
    return total / count
