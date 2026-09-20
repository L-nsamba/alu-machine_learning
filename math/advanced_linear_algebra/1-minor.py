#!/usr/bin/env python3
""" Module defines a function to calculate the minor matrix of a matrix """


def minor(matrix):
    """Calculates the minor matrix of a matrix"""

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    minor_matrix = []

    for i in range(n):
        minor_row = []
        for j in range(n):
            submatrix = [
                row[:j] + row[j + 1:]
                for k, row in enumerate(matrix)
                if k != i
            ]
            minor_row.append(determinant(submatrix))
        minor_matrix.append(minor_row)

    return minor_matrix
