#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print()
        return
    for j in matrix:
        for i in range(len(j)):
            if i < (len(j) - 1):
                print('{:d}'.format(row[i]), end=' ')
            else:
                print('{:d}'.format(row[i]))
