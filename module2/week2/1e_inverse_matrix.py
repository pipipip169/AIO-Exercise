# Inverse matrix

import numpy as np


def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result


m = np.array([[1, 2], [4, -1]])
result = inverse_matrix(m)
print(result)

result2 = np.dot(m, result)
print(result2)
