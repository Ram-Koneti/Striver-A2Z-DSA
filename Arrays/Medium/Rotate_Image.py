"""
Problem:
Rotate Image

Source:
LeetCode

Link:
https://leetcode.com/problems/rotate-image/

Approach:
1. Transpose the matrix (swap matrix[i][j] with matrix[j][i])
2. Reverse each row

Time Complexity:
O(n^2)

Space Complexity:
O(1)

Pattern:
Matrix Manipulation / Transpose + Reverse
"""

def rotate_image(matrix):
    n = len(matrix)

    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

    return matrix
