"""
Problem:
Roman to Integer

Source:
LeetCode

Link:
https://leetcode.com/problems/roman-to-integer/

Approach:
Store values of Roman symbols
in a hashmap.

Traverse the string:
- If current value is smaller than
  next value, subtract it.
- Otherwise, add it.

This handles special cases like:
IV = 4
IX = 9
XL = 40

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Hashing / String Traversal
"""

def roman_to_int(s):

    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    ans = 0

    for i in range(len(s)):

        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            ans -= roman[s[i]]
        else:
            ans += roman[s[i]]

    return ans
