"""
Problem:
Floor in a Sorted Array

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1

Approach:
Use binary search.
Store possible answer whenever arr[mid] <= x
and continue searching on right side.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Pattern:
Binary Search
"""

def find_floor(arr, x):
    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] <= x:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer
