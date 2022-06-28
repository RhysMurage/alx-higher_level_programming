#!/usr/bin/python3
"""
Module contains matrix_divided function
"""


def matrix_divided(matrix, div):
    """Divides the elements of a matrix with div

    Args:
        matrix (nested list): an nxm matrix
        div (int): value matrix to be divided by
    """
    item = 0
    new_matrix = []
    while item < len(matrix)-1:
        if len(matrix[item]) is not len(matrix[item+1]):
            raise TypeError('Each row of matrix must have the same size')
        item += 1
    for i in matrix:
        row = []
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError('''matrix must be a matrix (list of lists)''' +
                        ''' of integers/floats''')
            row.append(round(j/div, 2))
        new_matrix.append(row)
    return new_matrix
