"""
Problem:
Implement Lower Bound

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/implement-lower-bound/1

Approach:
Use binary search.
Store possible answer whenever arr[mid] >= target
and continue searching on left side.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Pattern:
Binary Search
"""

def lower_bound(arr, target):
    low = 0
    high = len(arr) - 1
    answer = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer
