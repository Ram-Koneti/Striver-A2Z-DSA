"""
Problem:
2220. Minimum Bit Flips to Convert Number

Source:
LeetCode

Link:
https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

Approach:
Take the XOR of start
and goal.

The XOR result has
set bits at positions
where the two numbers
differ.

Count the number of
set bits using Brian
Kernighan's algorithm.

The count represents
the minimum number of
bit flips required.

Time Complexity:
O(number of set bits)

Space Complexity:
O(1)

Pattern:
Bit Manipulation
"""

class Solution:

    def minBitFlips(self, start: int, goal: int) -> int:

        ans = start ^ goal

        count = 0

        while ans:

            ans &= (ans - 1)

            count += 1

        return count
