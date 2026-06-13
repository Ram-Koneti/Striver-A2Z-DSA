"""
Problem:
Implement Queue using Arrays

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/implement-queue-using-array/1

Approach:
Use a Python list as the underlying
array for queue implementation.

Enqueue operation inserts an element
at the rear of the queue.

Dequeue operation removes and returns
the front element from the queue.

The first inserted element is removed
first, following the FIFO principle.

Time Complexity:
enqueue() -> O(1)
dequeue() -> O(n)

Space Complexity:
O(n)

Pattern:
Queue Implementation
"""

class MyQueue:

    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if len(self.arr) == 0:
            return -1

        return self.arr.pop(0)
