"""
Problem:
Set Matrix Zeroes

Source:
LeetCode

Link:
https://leetcode.com/problems/set-matrix-zeroes/

Approach:
Use first row and first column as markers.
Track separately if first row and first column need to be zeroed.

Time Complexity:
O(m * n)

Space Complexity:
O(1)

Pattern:
Matrix Manipulation / In-place marking
"""

def set_matrix_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])

    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # mark rows and columns
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # set zeroes based on marks
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(n):
                matrix[i][j] = 0

    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(m):
                matrix[i][j] = 0

    # handle first row
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    # handle first column
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

    return matrix
