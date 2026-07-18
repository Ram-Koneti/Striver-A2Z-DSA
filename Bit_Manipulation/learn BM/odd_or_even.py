"""
Problem:
Odd or Even

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/odd-or-even3618/1

Approach:
Check the least significant
bit of the number using
bitwise AND with 1.

If the result is 1,
the number is odd.

Otherwise, it is even.

Time Complexity:
O(1)

Space Complexity:
O(1)

Pattern:
Bit Manipulation
"""

class Solution:

    def isEven(self, n):

        if (n & 1) == 1:
            return False

        return True
