"""
Problem:
Left Rotate Array by One

Source:
Striver A2Z DSA Sheet

Link:
https://takeuforward.org/data-structure/left-rotate-the-array-by-one/

Approach:
Store first element, shift all elements left by one, place first at end.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Array Rotation
"""

def left_rotate_by_one(arr):
    if not arr:
        return arr

    first = arr[0]

    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]

    arr[-1] = first

    return arr
