"""
Problem:
Implement Queue using Linked List

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/implement-queue-using-linked-list/1

Approach:
Use a linked list with front and
rear pointers.

Enqueue operation inserts a new
node at the rear of the queue.

Dequeue operation removes and
returns the front node.

This follows the FIFO principle.

Time Complexity:
push() -> O(1)
pop() -> O(1)

Space Complexity:
O(n)

Pattern:
Queue Implementation
"""

class MyQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    def push(self, item):

        new = Node(item)

        if self.front is None:
            self.front = new
            self.rear = new
            return

        self.rear.next = new
        self.rear = new

    def pop(self):

        if self.front is None:
            return -1

        val = self.front.data

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return val
