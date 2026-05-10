"""
Problem:
Search Insert Position

Source:
LeetCode

Link:
https://leetcode.com/problems/search-insert-position/

Approach:
Use binary search.
If target is found return its index.
Otherwise return the position where it should be inserted.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Pattern:
Binary Search
"""

def search_insert(nums, target):
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

    return low
