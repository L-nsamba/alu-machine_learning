#!/usr/bin/env python3
""" Module defines a function to calculate the definiteness of a matrix """

import numpy as np


def definiteness(matrix):
    """Calculation of the definiteness of a matrix"""
    # Validate input type
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    # Ensure matrix is square and non-empty
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None
    if matrix.shape[0] == 0:
        return None

    # Check symmetry
    if not np.allclose(matrix, matrix.T):
        return None

    # Compute eigenvalues
    try:
        eigvals = np.linalg.eigvals(matrix)
    except Exception:
        return None

    # Check definiteness based on eigenvalues
    if np.all(eigvals > 0):
        return "Positive definite"
    if np.all(eigvals >= 0):
        return "Positive semi-definite"
    if np.all(eigvals < 0):
        return "Negative definite"
    if np.all(eigvals <= 0):
        return "Negative semi-definite"
    if np.any(eigvals > 0) and np.any(eigvals < 0):
        return "Indefinite"

    return None
