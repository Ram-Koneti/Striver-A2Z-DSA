"""
Problem:
1922. Count Good Numbers

Source:
LeetCode

Link:
https://leetcode.com/problems/count-good-numbers/

Approach:
Use recursive binary exponentiation.

For a good number:
- Even indices have 5 possible digits: 0, 2, 4, 6, 8.
- Odd indices have 4 possible digits: 2, 3, 5, 7.

For n digits:
    evenPos = (n + 1) // 2
    oddPos = n // 2

Therefore:
    answer = 5^evenPos * 4^oddPos

Calculate both powers using recursion.
At every step, divide the exponent by 2.

If n is even:
    x^n = (x^(n/2)) * (x^(n/2))

If n is odd:
    x^n = (x^(n/2)) * (x^(n/2)) * x

Apply modulo 10^9 + 7 at every multiplication.

Time Complexity:
O(log n)

Space Complexity:
O(log n) due to the recursive call stack.

Pattern:
Binary Exponentiation / Recursion
"""

class Solution:
    def countGoodNumbers(self, n: int) -> int:

        evenPos = (n + 1) // 2
        oddPos = n // 2

        mod = 10**9 + 7

        def power(x, n, mod):

            # Base case
            if n == 0:
                return 1

            half = power(x, n // 2, mod)

            # Even exponent
            if n & 1 == 0:
                return (half * half) % mod

            # Odd exponent
            return (half * half * x) % mod

        return (
            power(5, evenPos, mod) *
            power(4, oddPos, mod)
        ) % mod
