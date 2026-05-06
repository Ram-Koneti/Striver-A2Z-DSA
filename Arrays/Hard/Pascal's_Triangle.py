"""
Problem:
Pascal's Triangle

Source:
LeetCode

Link:
https://leetcode.com/problems/pascals-triangle/

Approach:
Build triangle row by row.
Each element is sum of two elements from previous row.

Time Complexity:
O(n^2)

Space Complexity:
O(n^2)

Pattern:
Matrix / Simulation
"""

def generate_pascal(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
