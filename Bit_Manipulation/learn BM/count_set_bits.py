"""
Problem:
Count Set Bits

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/set-bits0143/1

Approach:
Use Brian Kernighan's
algorithm.

In each iteration,
perform n & (n - 1),
which removes the
rightmost set bit.

Count the number of
iterations until n
becomes 0.

Time Complexity:
O(number of set bits)

Space Complexity:
O(1)

Pattern:
Bit Manipulation
"""

class Solution:

    def setBits(self, n):

        count = 0

        while n != 0:

            n = n & (n - 1)

            count += 1

        return count
