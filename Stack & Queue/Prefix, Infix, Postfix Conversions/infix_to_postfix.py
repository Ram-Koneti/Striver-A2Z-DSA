"""
Problem:
Infix to Postfix

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1

Approach:
Use a stack to store operators
and parentheses.

Append operands directly to
the result.

For operators, pop operators
from the stack while they have
higher precedence or equal
precedence (for left associative
operators).

Handle '^' separately because
it is right associative.

Push '(' onto the stack and
pop until '(' when ')' is found.

Finally, pop all remaining
operators into the result.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Monotonic Operator Stack
"""

class Solution:

    def precedence(self, ch):

        if ch == '^':
            return 3

        if ch in '*/':
            return 2

        if ch in '+-':
            return 1

        return -1

    def infixToPostfix(self, s):

        stack = []
        ans = ""

        for ch in s:

            if ch.isalnum():
                ans += ch

            elif ch == '(':
                stack.append(ch)

            elif ch == ')':

                while stack and stack[-1] != '(':
                    ans += stack.pop()

                stack.pop()

            else:

                while (
                    stack
                    and stack[-1] != '('
                    and (
                        self.precedence(stack[-1]) > self.precedence(ch)
                        or (
                            self.precedence(stack[-1]) == self.precedence(ch)
                            and ch != '^'
                        )
                    )
                ):
                    ans += stack.pop()

                stack.append(ch)

        while stack:
            ans += stack.pop()

        return ans
