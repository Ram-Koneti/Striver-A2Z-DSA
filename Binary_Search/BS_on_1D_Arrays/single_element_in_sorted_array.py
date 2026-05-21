"""
Problem:
Single Element in a Sorted Array

Source:
LeetCode

Link:
https://leetcode.com/problems/single-element-in-a-sorted-array/

Approach:
Use binary search.
Before the single element:
- pairs start at even index
After the single element:
- pairs start at odd index

Time Complexity:
O(log n)

Space Complexity:
O(1)

Pattern:
Binary Search
"""

def single_non_duplicate(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        # make mid even
        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        else:
            high = mid

    return nums[low]
