#!/usr/bin/python3
"""Module that divides all elements of a matrix.

This module provides a function that returns a new matrix with
all elements divided by a given number, rounded to 2 decimals.
"""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Args:
        matrix: list of lists of integers or floats.
        div: number to divide by, integer or float.

    Returns:
        A new matrix with divided elements rounded to 2 decimals.

    Raises:
        TypeError: if matrix is invalid, rows have different sizes,
            or div is not a number.
        ZeroDivisionError: if div is equal to 0.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(el, (int, float))
                    for row in matrix for el in row)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]
