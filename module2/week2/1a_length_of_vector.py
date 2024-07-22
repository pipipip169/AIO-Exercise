# Length of a vector

import numpy as np


def compute_vector_length(vector):
    length_of_vector = np.linalg.norm(vector)
    return length_of_vector


vector = np.array([-2, 4, 9, 21])
result = compute_vector_length(vector)
print(round(result, 2))
