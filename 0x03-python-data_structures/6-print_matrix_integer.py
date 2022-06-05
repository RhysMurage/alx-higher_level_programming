#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        pass
    else:
        for elem in matrix:
            print("{} {} {}".format(*elem))
