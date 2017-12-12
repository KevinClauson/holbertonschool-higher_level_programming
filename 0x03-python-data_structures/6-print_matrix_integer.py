#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    i = 0
    j = 0
    for r in matrix:
        j = 0
        for c in r:
            print("{:d} ".format(matrix[i][j]), end='')
            j += 1
        print()
        i += 1
