#!/usr/bin/env python3
""" Module defines a function to calculate the minor matrix of a matrix """


def minor(matrix):
    """Calculation of the minor matrix of a matrix"""
    # Validate input type and structure
    if (not isinstance(matrix, list)
            or not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or any(len(r) != n for r in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Compute minor matrix by excluding row and column for each element
    minors = []
    for i in range(n):
        row_minors = []
        for j in range(n):
            sub = [r[:j] + r[j+1:] for k, r in enumerate(matrix) if k != i]
            row_minors.append(determinant(sub))
        minors.append(row_minors)

    return minors

