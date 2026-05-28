"""
Problem:
String to Integer (atoi)

Source:
LeetCode

Link:
https://leetcode.com/problems/string-to-integer-atoi/

Approach:
1. Remove leading spaces
2. Check sign (+ or -)
3. Convert consecutive digits
4. Stop at first non-digit character
5. Clamp result within
   32-bit signed integer range

Range:
[-2^31, 2^31 - 1]

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
String Parsing
"""

def my_atoi(s):

    i = 0
    n = len(s)

    # Skip leading spaces
    while i < n and s[i] == ' ':
        i += 1

    # Check sign
    sign = 1

    if i < n and (s[i] == '+' or s[i] == '-'):

        if s[i] == '-':
            sign = -1

        i += 1

    num = 0

    # Convert digits
    while i < n and s[i].isdigit():

        num = num * 10 + int(s[i])

        i += 1

    num *= sign

    # Clamp to 32-bit range
    INT_MIN = -(2 ** 31)
    INT_MAX = (2 ** 31) - 1

    if num < INT_MIN:
        return INT_MIN

    if num > INT_MAX:
        return INT_MAX

    return num
