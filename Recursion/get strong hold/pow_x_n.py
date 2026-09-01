"""
Problem:
50. Pow(x, n)

Source:
LeetCode

Link:
https://leetcode.com/problems/powx-n/

Approach:
Use recursive binary exponentiation.

For every recursive call, divide n by 2.
If n is even:
    x^n = (x^(n/2)) * (x^(n/2))

If n is odd:
    x^n = (x^(n/2)) * (x^(n/2)) * x

Handle negative powers using:
    x^(-n) = 1 / x^n

This reduces the exponent by half at every recursive call.

Time Complexity:
O(log n)

Space Complexity:
O(log n) due to the recursive call stack.

Pattern:
Binary Exponentiation / Divide and Conquer
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            # Base case
            if n == 0:
                return 1.0

            half = helper(x, n // 2)

            # Even exponent
            if (n & 1) == 0:
                return half * half

            # Odd exponent
            return half * half * x

        # Handle negative exponent
        if n < 0:
            return 1 / helper(x, -n)

        return helper(x, n)
