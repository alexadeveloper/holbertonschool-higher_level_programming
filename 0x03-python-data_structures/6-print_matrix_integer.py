#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        largo = len(matrix[i])
        for j in range(largo):
            if j == largo - 1:
                print("{}".format(matrix[i][j]), end='')
            else:
                print("{}".format(matrix[i][j]), end=' ')
        print()
