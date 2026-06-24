"""
Problem:
Remove K Digits

Source:
LeetCode

Link:
https://leetcode.com/problems/remove-k-digits/

Approach:
Use a monotonic increasing stack.

While the current digit is smaller
than the stack top and removals
are still available, remove the
larger digit from the stack.

This greedily keeps smaller digits
towards the front, producing the
smallest possible number.

If removals remain after traversal,
remove digits from the end.

Build the result, remove leading
zeros, and handle the empty case.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Monotonic Stack Greedy
"""

class Solution:

    def removeKdigits(
        self,
        num: str,
        k: int
    ) -> str:

        stack = []

        for digit in num:

            while (
                stack and
                k > 0 and
                stack[-1] > digit
            ):
                stack.pop()
                k -= 1

            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1

        ans = "".join(stack).lstrip('0')

        return ans if ans else "0"
