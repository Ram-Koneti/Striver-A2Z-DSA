"""
Problem:
Valid Parentheses

Source:
LeetCode

Link:
https://leetcode.com/problems/valid-parentheses/

Approach:
Use a stack to keep track of
opening brackets.

When an opening bracket is found,
push it onto the stack.

When a closing bracket is found,
check whether the stack is empty
or the top element does not match.

If it matches, pop the opening
bracket from the stack.

The string is valid only if the
stack is empty at the end.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Matching Parentheses
"""

class Solution:

    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:

            if ch in '({[':
                stack.append(ch)

            else:

                if not stack:
                    return False

                if stack[-1] != pairs[ch]:
                    return False

                stack.pop()

        return len(stack) == 0
