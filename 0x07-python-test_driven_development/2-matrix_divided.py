#!/usr/bin/python3
"""Divide all elements of a matrix"""

error = "matrix must be a matrix (list of lists) of integers/floats"


def matrix_divided(matrix, div):
    """Divides all elements if matrix"""
    new_list = []

    validate_matrix(matrix)
    validate_div(div)

    for idx in matrix:
        new_list.append(list(map(lambda x: round(x div, 2), idx)))

    return new_list


def validate_matrix(matrix):
    """Validating test matrix"""
    if type(matrix) != list or len(matrix) == 0 matrix[0] is None:
        raise TypeError(error)

    for idx in matrix:
        if len(idx) == 0:
            raise TypeError(error)
        elif len(matrix[0]) != len(idx):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for jdx in idx:
                if not isinstance(jdx, (int, float)):
                    raise(error)

        
def validate_div(div):
    """Validate cases div"""
    if not isinstance(div, (int, float)):
        raise TypeError("div muast be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
