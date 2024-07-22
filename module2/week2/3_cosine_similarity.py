# Cosine Similarity

import numpy as np


def compute_vector_length(vector):
    length_of_vector = np.linalg.norm(vector)
    return length_of_vector


def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result


def compute_cosine_similarity(vector1, vector2):
    cos_simi = compute_dot_product(vector1, vector2) / (
        compute_vector_length(vector1) * compute_vector_length(vector2)
    )
    return cos_simi


v1 = np.array([1, 4, 5, 3, 5])
v2 = np.array([6, 2, 7, 4, 6])
cos_simi = compute_cosine_similarity(v1, v2)
print(cos_simi)
