"""
Problem:
Second Largest Element in Array

Source:
Striver A2Z DSA Sheet

Link:
https://takeuforward.org/data-structure/find-second-smallest-and-second-largest-element-in-an-array/

Approach:
Traverse array and maintain largest and second largest values while iterating.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Array Traversal
"""

def second_largest(arr):
    if len(arr) < 2:
        return None

    largest = second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second
