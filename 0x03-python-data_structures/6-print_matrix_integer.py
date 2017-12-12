#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    i = 0
    j = 0
    for r in matrix:
        j = 0
        s = ''
        for c in r:
            s += "{:d} ".format(matrix[i][j])
            j += 1
        print(s)
        i += 1
