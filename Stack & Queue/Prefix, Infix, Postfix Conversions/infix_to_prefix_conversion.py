"""
Problem:
Infix to Prefix Conversion

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/infix-to-prefix-conversion/1

Approach:
Reverse the infix expression.

Swap '(' with ')' and vice versa.

Convert the modified expression
to postfix using a stack.

Reverse the postfix expression
to obtain the prefix expression.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Expression Conversion
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

    def infixToPrefix(self, s):

        s = s[::-1]

        exp = ""

        for ch in s:

            if ch == '(':
                exp += ')'

            elif ch == ')':
                exp += '('

            else:
                exp += ch

        stack = []
        postfix = ""

        for ch in exp:

            if ch.isalnum():
                postfix += ch

            elif ch == '(':
                stack.append(ch)

            elif ch == ')':

                while stack and stack[-1] != '(':
                    postfix += stack.pop()

                stack.pop()

            else:

                while (
                    stack
                    and stack[-1] != '('
                    and (
                        self.precedence(stack[-1]) > self.precedence(ch)
                        or (
                            self.precedence(stack[-1]) == self.precedence(ch)
                            and ch == '^'
                        )
                    )
                ):
                    postfix += stack.pop()

                stack.append(ch)

        while stack:
            postfix += stack.pop()

        return postfix[::-1]
