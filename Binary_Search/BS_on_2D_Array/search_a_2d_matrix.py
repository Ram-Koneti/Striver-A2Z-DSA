"""
Problem:
Search a 2D Matrix

Source:
LeetCode

Link:
https://leetcode.com/problems/search-a-2d-matrix/

Approach:
Treat matrix as a flattened sorted array.
Apply binary search from:
0 to (m * n - 1)

Convert mid index to:
row = mid // cols
col = mid % cols

Time Complexity:
O(log(m * n))

Space Complexity:
O(1)

Pattern:
Binary Search on Matrix
"""

def search_matrix(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    low = 0
    high = rows * cols - 1

    while low <= high:

        mid = (low + high) // 2

        row = mid // cols
        col = mid % cols

        value = matrix[row][col]

        if value == target:
            return True

        elif value < target:
            low = mid + 1

        else:
            high = mid - 1

    return False
