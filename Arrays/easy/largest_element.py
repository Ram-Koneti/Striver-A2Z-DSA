"""
Problem:
Largest Element in Array

Source:
Striver A2Z DSA Sheet

Link:
https://takeuforward.org/data-structure/find-the-largest-element-in-an-array/

Approach:
Traverse the array once and keep updating the largest element whenever a bigger value is found.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Linear Scan / Array Traversal
"""

def find_largest_element(arr):
    if not arr:
        return None

    largest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest
