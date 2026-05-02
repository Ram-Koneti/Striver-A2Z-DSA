"""
Problem:
Move Zeroes

Source:
LeetCode

Link:
https://leetcode.com/problems/move-zeroes/

Approach:
Use two-pointer technique.
Pointer i tracks the position to place the next non-zero element.
Traverse with j, and whenever a non-zero element is found, swap it with index i.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Two Pointer / In-place array manipulation
"""

def move_zeroes(nums):
    i = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    return nums
