#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    row = len(matrix)
    col = len (matrix[0])
    my_list = [[0 for _ in range(col)]for i in range(row)]
    for i in range(row):
        for j in range (col):
            my_list[i][j] = matrix[i][j] * matrix[i][j]
    return(my_list)
