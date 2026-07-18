"""
Problem:
231. Power of Two

Source:
LeetCode

Link:
https://leetcode.com/problems/power-of-two/

Approach:
A power of two has only
one set bit in its binary
representation.

For such numbers,
n & (n - 1) equals 0
because subtracting 1
flips the only set bit
and all lower bits.

Handle the edge case
where n is less than or
equal to 0, since powers
of two are positive.

Time Complexity:
O(1)

Space Complexity:
O(1)

Pattern:
Bit Manipulation
"""

class Solution:

    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False

        return (n & (n - 1)) == 0
