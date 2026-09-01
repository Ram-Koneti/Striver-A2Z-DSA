"""
Problem:
Recursive Implementation of atoi()

Source:
Take U Forward

Link:
https://takeuforward.org/data-structure/recursive-implementation-of-atoi

Approach:
Use recursion to process the string digit by digit and build the
integer using res * 10 + digit.

First skip leading whitespaces and handle the optional sign.
The recursive helper stops when it reaches the end of the string
or encounters a non-digit character.

Finally, apply the sign and clamp the result to the 32-bit signed
integer range.

Time Complexity:
O(n)

Space Complexity:
O(n) due to the recursive call stack.

Pattern:
Recursion
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)

        # Skip leading whitespaces
        i = 0
        while i < n and s[i] == " ":
            i += 1

        # Handle sign
        sign = 1

        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        def helper(i, res):
            # Base case
            if i == n or not s[i].isdigit():
                return res

            digit = ord(s[i]) - ord("0")
            res = res * 10 + digit

            return helper(i + 1, res)

        res = helper(i, 0)
        res *= sign

        # 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if res < INT_MIN:
            return INT_MIN

        if res > INT_MAX:
            return INT_MAX

        return res
