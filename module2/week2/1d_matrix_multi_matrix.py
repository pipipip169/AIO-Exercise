# Multiply matrix with a matrix

import numpy as np


def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result


m1 = np.array([[1, 2, -4], [4, 2, -1]])
m2 = np.array([[1, -4], [8, 5], [1, -6]])
result = matrix_multi_matrix(m1, m2)
print(result)
