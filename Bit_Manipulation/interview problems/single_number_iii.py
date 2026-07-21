"""
Problem:
260. Single Number III

Source:
LeetCode

Link:
https://leetcode.com/problems/single-number-iii/

Approach:
Use XOR bit manipulation.

First XOR all numbers.

Since two numbers appear only
once and all others appear twice,
the XOR result contains the
difference between the two
unique numbers.

Find the rightmost set bit
using:

xor & (-xor)

This bit helps divide the
numbers into two groups.

XOR numbers in each group
separately to get the two
unique numbers.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Bit Manipulation
"""

class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:

        xor = 0

        for num in nums:

            xor ^= num

        rightmost = xor & (-xor)

        b1, b2 = 0, 0

        for num in nums:

            if num & rightmost:

                b1 ^= num

            else:

                b2 ^= num

        return [b1, b2]
