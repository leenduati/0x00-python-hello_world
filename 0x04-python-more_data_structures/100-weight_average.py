#!/usr/bin/python3


def weight_average(my_list=[]):
    count = 0
    total = 0
    for i in my_list:
        total = total + (i[0] * i[1])
        count = count + (i[1])
    return total / count
