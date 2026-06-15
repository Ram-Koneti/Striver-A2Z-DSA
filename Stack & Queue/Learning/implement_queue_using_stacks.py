"""
Problem:
Implement Queue using Stacks

Source:
LeetCode

Link:
https://leetcode.com/problems/implement-queue-using-stacks/

Approach:
Use two stacks.

Push elements into the input stack.

When pop or peek is requested,
transfer all elements from the
input stack to the output stack
only if the output stack is empty.

This reversal makes the oldest
element appear on top, maintaining
FIFO order.

Time Complexity:
push() -> O(1)
pop() -> O(1) Amortized
peek() -> O(1) Amortized
empty() -> O(1)

Space Complexity:
O(n)

Pattern:
Queue using Stacks
"""

class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:

        if not self.out_stack:

            while self.in_stack:
                self.out_stack.append(
                    self.in_stack.pop()
                )

        return self.out_stack.pop()

    def peek(self) -> int:

        if not self.out_stack:

            while self.in_stack:
                self.out_stack.append(
                    self.in_stack.pop()
                )

        return self.out_stack[-1]

    def empty(self) -> bool:
        return (
            len(self.in_stack) == 0 and
            len(self.out_stack) == 0
        )
