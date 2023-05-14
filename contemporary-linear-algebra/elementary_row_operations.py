"""Elementray row operations on matrices.
Three functions are defined:
    1. swap_rows
    2. scale_row
    3. add_multiple_of_row
"""

import numpy as np


def swap_rows(A, i, j):
    """Swap rows i and j of matrix A."""
    A[[i, j]] = A[[j, i]]
    return A

def scale_row(A, i, c):
    """Multiply row i of matrix A by c."""
    A[i] = c * A[i]
    return A

def add_multiple_of_row(A, i, j, c):
    """Add c times row j of matrix A to row i."""
    A[i] = A[i] + c * A[j]
    return A

def get_solution(A):
    """Get the solution to the system of equations defined by matrix A."""
    for i in range(A.shape[0]):
        c = A[i+1, i] / A[i, i]
        A[i+1] = A[i+1] - c * A[i]
        

