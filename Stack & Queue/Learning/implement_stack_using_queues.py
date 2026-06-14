"""
Problem:
Implement Stack using Queues

Source:
LeetCode

Link:
https://leetcode.com/problems/implement-stack-using-queues/

Approach:
Use a single queue to simulate
stack behavior.

Push the new element into the
queue and rotate all previous
elements behind it.

This ensures the most recently
added element always stays at
the front of the queue.

Pop removes the front element.

Top returns the front element
without removing it.

Time Complexity:
push() -> O(n)
pop() -> O(1)
top() -> O(1)
empty() -> O(1)

Space Complexity:
O(n)

Pattern:
Stack using Queue
"""

from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:

        self.q.append(x)

        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
