#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for col in row:
                print("{:d}".format(col), end=' ')
            print()
