"""
Problem:
Find Minimum in Rotated Sorted Array

Source:
LeetCode

Link:
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Approach:
Use binary search.
One half will always be sorted.
The minimum element lies in the unsorted half.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Pattern:
Binary Search
"""

def find_minimum(nums):
    low = 0
    high = len(nums) - 1
    answer = nums[0]

    while low <= high:

        # array already sorted
        if nums[low] <= nums[high]:
            answer = min(answer, nums[low])
            break

        mid = (low + high) // 2

        # left half sorted
        if nums[low] <= nums[mid]:
            answer = min(answer, nums[low])
            low = mid + 1

        # right half sorted
        else:
            answer = min(answer, nums[mid])
            high = mid - 1

    return answer
