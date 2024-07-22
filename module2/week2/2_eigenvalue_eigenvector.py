# Eigenvalue and eigenvector

import numpy as np


def compute_eigenval_eigenvec(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


matrix = np.array([[0.9, 0.2], [0.3, 0.4]])
eigenvalues, eigenvectors = compute_eigenval_eigenvec(matrix)
print(eigenvectors)
print(eigenvalues)
