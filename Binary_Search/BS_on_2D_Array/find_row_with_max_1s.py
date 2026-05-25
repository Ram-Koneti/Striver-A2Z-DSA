"""
Problem:
Row With Maximum Ones

Source:
LeetCode

Link:
https://leetcode.com/problems/row-with-maximum-ones/

Approach:
Traverse each row and count number of ones.
Track:
- maximum ones count
- corresponding row index

If multiple rows have same count,
choose smaller row index.

Time Complexity:
O(m * n)

Space Complexity:
O(1)

Pattern:
Matrix Traversal
"""

def row_and_maximum_ones(mat):

    max_ones = 0
    row_index = 0

    for i in range(len(mat)):

        ones = sum(mat[i])

        if ones > max_ones:
            max_ones = ones
            row_index = i

    return [row_index, max_ones]
