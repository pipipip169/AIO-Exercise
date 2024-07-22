# Dot product

import numpy as np


def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result


v1 = np.array([-2, 4, 9, 21])
v2 = np.array([-21, 2, 4, 3])
result = compute_dot_product(v1, v2)
print(round(result, 2))
