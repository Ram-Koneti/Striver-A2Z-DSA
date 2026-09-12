"""
Problem:
Generate Binary Strings Without Consecutive 1s

Source:
Take U Forward

Link:
https://takeuforward.org/data-structure/generate-all-binary-strings

Approach:
Use dynamic programming with two states.

zeroEnd:
Number of valid binary strings of length i ending with 0.

oneEnd:
Number of valid binary strings of length i ending with 1.

For a string ending in 0:
    We can append 0 to any valid string.
    Therefore:
    zeroEnd = zeroEnd + oneEnd

For a string ending in 1:
    We can only append 1 after a string ending in 0.
    Therefore:
    oneEnd = zeroEnd

Initialize for length 1:
    zeroEnd = 1  -> "0"
    oneEnd = 1   -> "1"

The answer is:
    zeroEnd + oneEnd

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Dynamic Programming / Fibonacci Pattern
"""

class Solution:
    def countStrings(self, n):

        zeroEnd = 1
        oneEnd = 1

        if n == 1:
            return zeroEnd + oneEnd

        i = 2

        while i <= n:

            total = zeroEnd + oneEnd

            # A string ending in 1 can only
            # come from a string ending in 0
            oneEnd = zeroEnd

            # We can append 0 to both states
            zeroEnd = total

            i += 1

        return zeroEnd + oneEnd
