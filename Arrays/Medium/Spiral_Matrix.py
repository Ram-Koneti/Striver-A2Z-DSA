"""
Problem:
Spiral Matrix

Source:
LeetCode

Link:
https://leetcode.com/problems/spiral-matrix/

Approach:
Use four boundaries (top, bottom, left, right).
Traverse layer by layer in spiral order.

Time Complexity:
O(m * n)

Space Complexity:
O(1) (excluding output)

Pattern:
Matrix Traversal
"""

def spiral_order(matrix):
    result = []
    if not matrix:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # left → right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1

        # top → bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # right → left
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1

        if left <= right:
            # bottom → top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
