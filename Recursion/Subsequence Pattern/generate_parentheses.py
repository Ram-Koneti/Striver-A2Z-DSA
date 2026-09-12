"""
Problem:
22. Generate Parentheses

Source:
LeetCode

Link:
https://leetcode.com/problems/generate-parentheses/

Approach:
Use backtracking to generate all valid combinations of n pairs
of parentheses.

Maintain two counters:
- openN: number of opening parentheses used.
- closeN: number of closing parentheses used.

Rules:
1. Add "(" if openN < n.
2. Add ")" only if closeN < openN.
   This ensures that we never have more closing parentheses than
   opening parentheses at any point.

When openN == closeN == n, a valid combination is complete.
Add it to the result.

Use stack.pop() after each recursive call to undo the choice
and explore the next possibility.

Time Complexity:
O(4^n / sqrt(n))

Space Complexity:
O(n) for the recursion stack and current combination,
excluding the output.

Pattern:
Backtracking / Decision Tree
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtrack(openN, closeN):

            # Base case
            if openN == closeN == n:
                res.append("".join(stack))
                return

            # Add opening parenthesis
            if openN < n:
                stack.append("(")

                backtrack(openN + 1, closeN)

                # Undo the choice
                stack.pop()

            # Add closing parenthesis
            if closeN < openN:
                stack.append(")")

                backtrack(openN, closeN + 1)

                # Undo the choice
                stack.pop()

        backtrack(0, 0)

        return res
