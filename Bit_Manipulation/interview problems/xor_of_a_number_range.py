"""
Problem:
XOR of a Number Range

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/xor-of-a-number-range/1

Approach:
The XOR of numbers
from 0 to n follows
a repeating pattern
based on n % 4.

If n % 4 == 0:
XOR = n

If n % 4 == 1:
XOR = 1

If n % 4 == 2:
XOR = n + 1

If n % 4 == 3:
XOR = 0

To find the XOR of
the range [l, r],
compute:

XOR(0...r) ^
XOR(0...(l-1))

Time Complexity:
O(1)

Space Complexity:
O(1)

Pattern:
Bit Manipulation
"""

class Solution:

    def findXOR(self, l, r):

        return self.func(l - 1) ^ self.func(r)

    def func(self, n):

        if n % 4 == 0:
            return n

        elif n % 4 == 1:
            return 1

        elif n % 4 == 2:
            return n + 1

        return 0
