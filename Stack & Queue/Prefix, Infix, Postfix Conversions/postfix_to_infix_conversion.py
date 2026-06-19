"""
Problem:
Postfix to Infix Conversion

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/postfix-to-infix-conversion/1

Approach:
Traverse the postfix expression
from left to right.

If the character is an operand,
push it onto the stack.

If the character is an operator,
pop two operands from the stack.

Form an infix expression:

(op1 operator op2)

and push it back onto the stack.

The final stack element is the
required infix expression.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Expression Conversion
"""

class Solution:

    def postToInfix(self, postfix):

        stack = []

        for ch in postfix:

            if ch.isalnum():
                stack.append(ch)

            else:

                op2 = stack.pop()
                op1 = stack.pop()

                exp = "(" + op1 + ch + op2 + ")"

                stack.append(exp)

        return stack[-1]
