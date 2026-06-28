"""
Problem:
Online Stock Span

Source:
LeetCode

Link:
https://leetcode.com/problems/online-stock-span/

Approach:
Use a monotonic decreasing stack
to store pairs of:

(price, index)

Remove all previous prices that
are less than or equal to the
current price.

The top of the stack becomes the
previous greater price.

The span is the distance between
the current index and the previous
greater index.

If no previous greater price
exists, the span is current
index + 1.

Time Complexity:
O(1) Amortized

Space Complexity:
O(n)

Pattern:
Monotonic Stack
"""

class StockSpanner:

    def __init__(self):

        self.stack = []
        self.idx = -1

    def next(self, price: int) -> int:

        self.idx += 1

        while (
            self.stack and
            price >= self.stack[-1][0]
        ):
            self.stack.pop()

        if self.stack:
            ans = self.idx - self.stack[-1][1]

        else:
            ans = self.idx + 1

        self.stack.append((price, self.idx))

        return ans
