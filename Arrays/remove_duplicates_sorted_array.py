"""
Problem:
Remove Duplicates from Sorted Array

Source:
LeetCode

Link:
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Approach:
Use two-pointer technique.
Pointer i tracks the position of the last unique element.
Pointer j scans the array. When a new unique element is found, increment i and place it at index i.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Two Pointer
"""

def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1
