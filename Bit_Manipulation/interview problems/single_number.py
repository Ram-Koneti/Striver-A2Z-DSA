"""
Problem:
136. Single Number

Source:
LeetCode

Link:
https://leetcode.com/problems/single-number/

Approach:
Use the XOR operation
on all elements.

A number XOR itself
becomes 0.

0 XOR any number
returns that number.

Since every element
appears twice except
one, all duplicate
elements cancel out,
leaving only the
single number.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Bit Manipulation
"""

class Solution:

    def singleNumber(self, nums: List[int]) -> int:

        ans = 0

        for num in nums:

            ans ^= num

        return ans
