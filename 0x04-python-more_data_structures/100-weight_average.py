#!/usr/bin/python3
def weight_average(my_list=[]):
    s = 0
    div = 0
    for i in my_list:
        a, b = i
        s += a * b
        div += b
    if div == 0:
        return 0
    return s/div
