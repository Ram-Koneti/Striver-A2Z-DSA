"""
Problem:
Find Kth Rotation

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/rotation4723/1

Approach:
The index of the minimum element gives the number of rotations.
Use binary search to find the minimum element.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Pattern:
Binary Search
"""

def find_k_rotation(arr):
    low = 0
    high = len(arr) - 1
    answer = float("inf")
    index = -1

    while low <= high:

        # array already sorted
        if arr[low] <= arr[high]:
            if arr[low] < answer:
                answer = arr[low]
                index = low
            break

        mid = (low + high) // 2

        # left half sorted
        if arr[low] <= arr[mid]:

            if arr[low] < answer:
                answer = arr[low]
                index = low

            low = mid + 1

        # right half sorted
        else:

            if arr[mid] < answer:
                answer = arr[mid]
                index = mid

            high = mid - 1

    return index
