"""
Problem:
Swap The Numbers

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1

Approach:
Use XOR bit manipulation
to swap two numbers
without using an extra
variable.

Steps:

a = a ^ b
Stores combined XOR value.

b = a ^ b
Restores original value
of a into b.

a = a ^ b
Restores original value
of b into a.

Time Complexity:
O(1)

Space Complexity:
O(1)

Pattern:
Bit Manipulation
"""

class Solution:

    def swap(self, a, b):

        a = a ^ b

        b = a ^ b

        a = a ^ b

        print(a, b)
