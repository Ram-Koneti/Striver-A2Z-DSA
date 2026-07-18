"""
Problem:
Check K-th Bit

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1

Approach:
Right shift the number by
k positions so that the
k-th bit becomes the
least significant bit.

Perform bitwise AND with 1.

If the result is 1,
the k-th bit is set.

Otherwise, it is not set.

Time Complexity:
O(1)

Space Complexity:
O(1)

Pattern:
Bit Manipulation
"""

class Solution:

    def checkKthBit(self, n, k):

        if ((n >> k) & 1) == 0:
            return False

        return True
