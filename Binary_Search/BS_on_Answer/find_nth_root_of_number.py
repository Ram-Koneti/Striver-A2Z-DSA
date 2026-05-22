"""
Problem:
Find nth Root of m

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1

Approach:
Use binary search on answer.
Check whether mid^n equals m.
If integer nth root does not exist, return -1.

Time Complexity:
O(log m * n)

Space Complexity:
O(1)

Pattern:
Binary Search on Answer
"""

def nth_root(n, m):
    low = 1
    high = m

    while low <= high:
        mid = (low + high) // 2

        value = mid ** n

        if value == m:
            return mid

        elif value < m:
            low = mid + 1

        else:
            high = mid - 1

    return -1
