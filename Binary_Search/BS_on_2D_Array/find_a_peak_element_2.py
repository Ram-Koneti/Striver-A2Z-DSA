"""
Problem:
Find a Peak Element II

Source:
LeetCode

Link:
https://leetcode.com/problems/find-a-peak-element-ii/

Approach:
Use binary search on columns.

For each middle column:
- find row having maximum element
- compare with left and right neighbors

If current element is greater than both:
it is a peak.

Otherwise move towards greater neighbor.

Time Complexity:
O(m * log(n))

Space Complexity:
O(1)

Pattern:
Binary Search on Matrix
"""

def find_peak_grid(mat):

    rows = len(mat)
    cols = len(mat[0])

    low = 0
    high = cols - 1

    while low <= high:

        mid = (low + high) // 2

        # Find max element row in current column
        max_row = 0

        for row in range(rows):

            if mat[row][mid] > mat[max_row][mid]:
                max_row = row

        left = -1
        right = -1

        if mid - 1 >= 0:
            left = mat[max_row][mid - 1]

        if mid + 1 < cols:
            right = mat[max_row][mid + 1]

        current = mat[max_row][mid]

        # Peak found
        if current > left and current > right:
            return [max_row, mid]

        # Move left
        elif left > current:
            high = mid - 1

        # Move right
        else:
            low = mid + 1
