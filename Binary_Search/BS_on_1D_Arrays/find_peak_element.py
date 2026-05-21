"""
Problem:
Find Peak Element

Source:
LeetCode

Link:
https://leetcode.com/problems/find-peak-element/

Approach:
Use binary search.
If nums[mid] > nums[mid + 1],
then peak lies on left side including mid.
Otherwise peak lies on right side.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Pattern:
Binary Search
"""

def find_peak_element(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return low
