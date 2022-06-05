#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        if len(matrix[0]) == 0:
            pass
            #print("{}".format('$'))
        else:
            for elem in matrix:
                print("{} {} {}".format(*elem))
