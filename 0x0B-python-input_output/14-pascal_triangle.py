#!/usr/bin/python3


def pascal_triangle(n):
    """build pascals triangle with list of lists"""
    new = []
    if n <= 0:
        return new
    t = f = 0
    new = [[1]]
    if n == 1:
        return new
    while t < (n - 1):
        temp = []
        for i in range(len(new[t])):
            if i == 0:
                temp.append(new[t][i])
            if i < (len(new[t]) - 1):
                temp.append(new[t][i] + new[t][i+1])
            if i == (len(new[t]) - 1):
                temp.append(new[t][i])
        t += 1
        new.append(temp)
    return new
