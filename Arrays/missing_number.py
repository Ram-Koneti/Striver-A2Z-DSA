"""
Problem:
Missing Number

Source:
LeetCode

Link:
https://leetcode.com/problems/missing-number/

Approach:
Use sum formula: n * (n + 1) // 2 to calculate expected sum.
Subtract actual sum of array to find the missing number.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Math
"""

def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum
