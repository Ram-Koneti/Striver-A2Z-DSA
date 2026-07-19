"""
Problem:
Set the Rightmost Unset Bit

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/set-the-rightmost-unset-bit4436/1

Approach:
The expression n + 1
changes the rightmost
unset bit of n to 1.

Perform bitwise OR between
n and n + 1.

This sets the rightmost
unset bit while keeping
all other set bits unchanged.

Time Complexity:
O(1)

Space Complexity:
O(1)

Pattern:
Bit Manipulation
"""

class Solution:

    def setBit(self, n):

        return n | (n + 1)
