"""
Problem:
Prefix to Postfix Conversion

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/prefix-to-postfix-conversion/1

Approach:
Traverse the prefix expression
from right to left.

If the character is an operand,
push it onto the stack.

If the character is an operator,
pop two operands from the stack.

Form a postfix expression:

op1 op2 operator

and push it back onto the stack.

The final stack element is the
required postfix expression.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Expression Conversion
"""

class Solution:

    def preToPost(self, pre_exp):

        stack = []

        for ch in reversed(pre_exp):

            if ch.isalnum():
                stack.append(ch)

            else:

                op1 = stack.pop()
                op2 = stack.pop()

                exp = op1 + op2 + ch

                stack.append(exp)

        return stack[-1]
