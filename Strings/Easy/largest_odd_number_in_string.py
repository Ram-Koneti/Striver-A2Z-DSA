"""
Problem:
Largest Odd Number in String

Source:
LeetCode

Link:
https://leetcode.com/problems/largest-odd-number-in-string/

Approach:
Traverse the string from right to left.

The first odd digit found gives
the largest odd-numbered substring,
because any prefix ending there
forms the maximum possible odd number.

If no odd digit exists,
return empty string.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Greedy / String Traversal
"""

def largest_odd_number(num):

    for i in range(len(num) - 1, -1, -1):

        if int(num[i]) % 2 == 1:
            return num[:i + 1]

    return ""
