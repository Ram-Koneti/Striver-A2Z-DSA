"""
Problem:
Maximum Subarray

Source:
LeetCode

Link:
https://leetcode.com/problems/maximum-subarray/

Approach:
Use Kadane’s Algorithm.
Keep track of current sum and maximum sum.
If current sum becomes negative, reset it.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Kadane's Algorithm
"""

def max_subarray(nums):
    current_sum = 0
    max_sum = nums[0]

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum
