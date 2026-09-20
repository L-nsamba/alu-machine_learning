#!/usr/bin/env python3
""" Module defines functions to calculate determinant and minor matrix """


def determinant(matrix):
    """Calculation of the determinant of a matrix"""
    if (not isinstance(matrix, list)
            or not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or (n == 1 and len(matrix[0]) == 0):
        return 1  # determinant of a 0x0 matrix is conventionally 1

    if any(len(r) != n for r in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base cases
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive expansion by first row (Laplace expansion)
    det = 0
    for col in range(n):
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det


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
