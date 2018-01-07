#!/usr/bin/python3
""" 
module to divide a matrix by a given number
"""


def matrix_divided(matrix, div):
    """ divides every element of matrix by div """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(isinstance(elem, list) for elem in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new = []
    for row in matrix:
        temp = []
        if len(row) == len(matrix[0]):
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            temp.append(round(i/div, 2))
        new.append(temp)               
    return new