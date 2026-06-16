"""
Problem:
Min Stack

Source:
LeetCode

Link:
https://leetcode.com/problems/min-stack/

Approach:
Maintain the current minimum value.

When a new value is smaller than
the current minimum, store an
encoded value:

2 * value - minimum

and update the minimum.

During pop, if the popped value
is smaller than the current minimum,
it represents an encoded value.

Decode the previous minimum using:

2 * minimum - encoded_value

This allows retrieving the minimum
in O(1) time without using an
extra stack.

Time Complexity:
push()   -> O(1)
pop()    -> O(1)
top()    -> O(1)
getMin() -> O(1)

Space Complexity:
O(n)

Pattern:
Stack with Minimum Tracking
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float("inf")

    def push(self, value: int) -> None:

        if not self.stack:
            self.stack.append(value)
            self.mini = value

        elif value >= self.mini:
            self.stack.append(value)

        else:
            self.stack.append(2 * value - self.mini)
            self.mini = value

    def pop(self) -> None:

        if not self.stack:
            return

        top = self.stack.pop()

        if top < self.mini:
            self.mini = 2 * self.mini - top

    def top(self) -> int:

        if not self.stack:
            return -1

        if self.stack[-1] >= self.mini:
            return self.stack[-1]

        return self.mini

    def getMin(self) -> int:
        return self.mini
