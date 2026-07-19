"""
Problem:
29. Divide Two Integers

Source:
LeetCode

Link:
https://leetcode.com/problems/divide-two-integers/

Approach:
Use bit manipulation to
perform division without
using multiplication,
division, or modulo.

Convert both dividend and
divisor into positive values.

Repeatedly subtract the
largest shifted value of
divisor from dividend.

Use left shift operation
to multiply divisor by
powers of 2 and build the
quotient efficiently.

Handle:
- Negative numbers using sign
- Integer overflow case

Time Complexity:
O(log n ^ 2)

Space Complexity:
O(1)

Pattern:
Bit Manipulation + Binary
Exponentiation Technique
"""

class Solution:

    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == divisor:
            return 1

        # Overflow case
        if dividend == -(1 << 31) and divisor == -1:
            return (1 << 31) - 1

        # Determine sign
        sign = True

        if (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0):
            sign = False

        n = abs(dividend)
        d = abs(divisor)

        ans = 0

        while n >= d:

            count = 0

            while n >= d * (1 << (count + 1)):
                count += 1

            ans += (1 << count)

            n = n - (d * (1 << count))

        return ans if sign else -ans
