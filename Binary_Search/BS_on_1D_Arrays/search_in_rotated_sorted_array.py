"""
Problem:
Search in Rotated Sorted Array

Source:
LeetCode

Link:
https://leetcode.com/problems/search-in-rotated-sorted-array/

Approach:
Use binary search.
At every step, one half will always be sorted.
Check whether target lies in sorted half and move accordingly.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Pattern:
Binary Search
"""

def search_rotated_array(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # left half sorted
        if nums[low] <= nums[mid]:

            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # right half sorted
        else:

            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
