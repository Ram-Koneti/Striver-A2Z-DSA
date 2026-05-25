"""
Problem:
Median in a Row-wise Sorted Matrix

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1

Approach:
Use binary search on answer.

For each middle value:
count how many elements are <= mid
using binary search in every row.

Median position:
(n * m) // 2

Time Complexity:
O(log(max-min) * n * log(m))

Space Complexity:
O(1)

Pattern:
Binary Search on Answer
"""

from bisect import bisect_right

def matrix_median(mat):

    rows = len(mat)
    cols = len(mat[0])

    low = min(row[0] for row in mat)
    high = max(row[-1] for row in mat)

    required = (rows * cols) // 2

    while low <= high:

        mid = (low + high) // 2

        count = 0

        for row in mat:
            count += bisect_right(row, mid)

        if count <= required:
            low = mid + 1
        else:
            high = mid - 1

    return low
