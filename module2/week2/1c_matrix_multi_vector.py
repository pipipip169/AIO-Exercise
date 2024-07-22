# Multiply matrix with a vector

import numpy as np


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result


m = np.array([[1, 2, -4], [4, 2, -1]])
v = np.array([1, -4, 9])
result = matrix_multi_vector(m, v)
print(result)
