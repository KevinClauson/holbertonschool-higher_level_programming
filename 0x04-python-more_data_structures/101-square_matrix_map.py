#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    my_matrix = [list(map(lambda x: x*x, x)) for x in matrix]
    return my_matrix
