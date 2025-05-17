#!/usr/bin/python3
"""
This is the "2-matrix_divided" modulo.
It contains the function :
matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Divided all elements of matrix.

    parameter:
    matrix : list of list to same size.
    div : divider.

    return :
    divide the elements of matrix.
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
            )
    for tab in matrix:
        if not isinstance(tab, list):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats'
                )
        if len(tab) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for num in tab:
            if type(num) is not int and type(num) is not float:
                raise TypeError(
                    'matrix must be a matrix (list of lists)'
                    'of integers/floats'
                    )
    new_m = []
    for i in matrix:
        new_m.append(list(map(lambda x: int(x / div * 100) / 100, i)))
    return new_m
