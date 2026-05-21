"""
Problem:
Search in Rotated Sorted Array II

Source:
LeetCode

Link:
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

Approach:
Use modified binary search.
Handle duplicates by shrinking search space when
nums[low] == nums[mid] == nums[high].

Time Complexity:
O(log n) average case
O(n) worst case

Space Complexity:
O(1)

Pattern:
Binary Search
"""

def search_rotated_array_duplicates(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return True

        # handle duplicates
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1

        # left half sorted
        elif nums[low] <= nums[mid]:

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

    return False
