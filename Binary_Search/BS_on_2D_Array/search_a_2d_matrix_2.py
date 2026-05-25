"""
Problem:
Search a 2D Matrix II

Source:
LeetCode

Link:
https://leetcode.com/problems/search-a-2d-matrix-ii/

Approach:
Start from top-right corner.

If current value > target:
move left

If current value < target:
move down

This works because:
- rows are sorted
- columns are sorted

Time Complexity:
O(m + n)

Space Complexity:
O(1)

Pattern:
Matrix Traversal
"""

def search_matrix(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1

    while row < rows and col >= 0:

        value = matrix[row][col]

        if value == target:
            return True

        elif value > target:
            col -= 1

        else:
            row += 1

    return False
