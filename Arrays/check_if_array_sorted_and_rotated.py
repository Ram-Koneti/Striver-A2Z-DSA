"""
Problem:
Check if Array is Sorted and Rotated

Source:
LeetCode

Link:
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

Approach:
Traverse the array and count how many times the order decreases.
If the array is sorted and rotated, there will be at most one such violation.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Array Traversal
"""

def check_sorted_and_rotated(nums):
    count = 0
    n = len(nums)

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1

    return count <= 1
