"""
Problem:
Sort Colors

Source:
LeetCode

Link:
https://leetcode.com/problems/sort-colors/

Approach:
Use Dutch National Flag algorithm (3 pointers):
low → boundary for 0s
mid → current element
high → boundary for 2s

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Three Pointer / Dutch National Flag
"""

def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums
