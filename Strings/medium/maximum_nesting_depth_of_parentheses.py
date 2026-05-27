"""
Problem:
Maximum Nesting Depth of the Parentheses

Source:
LeetCode

Link:
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

Approach:
Traverse the string and maintain
current depth of parentheses.

For every '(':
increase depth and update maximum.

For every ')':
decrease depth.

The maximum depth reached
is the answer.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Stack / Parentheses Traversal
"""

def max_depth(s):

    depth = 0
    maxi = 0

    for ch in s:

        if ch == '(':

            depth += 1
            maxi = max(maxi, depth)

        elif ch == ')':

            depth -= 1

    return maxi
