#!/usr/bin/env python3
"""
Matrix shape utility
"""
def matrix_shape(matrix):
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
