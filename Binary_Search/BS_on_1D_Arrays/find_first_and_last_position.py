"""
Problem:
Find First and Last Position of Element in Sorted Array

Source:
LeetCode

Link:
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Approach:
Use binary search twice.
First binary search finds the first occurrence of target.
Second binary search finds the last occurrence of target.

If target is not found return [-1, -1].

Time Complexity:
O(log n)

Space Complexity:
O(1)

Pattern:
Binary Search
"""

def search_range(nums, target):

    def first_occurrence():
        low = 0
        high = len(nums) - 1
        first = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                first = mid
                high = mid - 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return first

    def last_occurrence():
        low = 0
        high = len(nums) - 1
        last = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                last = mid
                low = mid + 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return last

    return [first_occurrence(), last_occurrence()]
