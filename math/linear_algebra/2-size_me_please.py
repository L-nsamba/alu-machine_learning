#!/usr/bin/env python3
"""
Module: 2-size_me_please
========================

This module provides a utility function for determining the shape of a matrix.

Functions:
----------
matrix_shape(matrix):
    Computes the dimensions of a matrix represented as nested lists.
    The function traverses the matrix recursively, counting the length
    of each level until reaching non-list elements.

Example:
--------
>>> matrix_shape([[1, 2], [3, 4]])
[2, 2]

>>> matrix_shape([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
[2, 2, 2]

Returns:
--------
list
    A list of integers representing the size of the matrix at each dimension.
"""
def matrix_shape(matrix):
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape

