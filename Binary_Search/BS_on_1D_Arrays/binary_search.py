"""
Problem:
Binary Search

Source:
LeetCode

Link:
https://leetcode.com/problems/binary-search/

Approach:
Use binary search on sorted array.
Compare middle element with target and reduce search space.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Pattern:
Binary Search
"""

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1
