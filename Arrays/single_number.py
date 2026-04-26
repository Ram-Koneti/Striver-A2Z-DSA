"""
Problem:
Single Number

Source:
LeetCode

Link:
https://leetcode.com/problems/single-number/

Approach:
Use XOR operation.
XOR of a number with itself is 0, and XOR with 0 gives the number.
So all duplicate elements cancel out, leaving the single number.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Bit Manipulation (XOR)
"""

def single_number(nums):
    result = 0

    for num in nums:
        result ^= num

    return result
