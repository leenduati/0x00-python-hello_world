#!/usr/bin/python3

"""
    This is a function that divides a num frm matrix
    It will be imported by 2-main.py
    This is its docstring
"""


def matrix_divided(matrix, div):

    """ This is a function that divides a num from matrix
    Args:
        matrix (int): _list value_
        div (int): _int value_
    Returns:
        list: Description of return value """

    len_mat = []
    for i in matrix:
        len_mat.append(len(i))
        for j in i:
            e = 'matrix must be a matrix (list of lists) of integers/floats'
            if type(j) not in [int, float]:
                raise TypeError(e)
    if type(matrix) != list:
        TypeError("Matrix not a list")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if len(set(len_mat)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
