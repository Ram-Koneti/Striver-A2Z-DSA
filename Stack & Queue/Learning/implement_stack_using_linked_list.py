"""
Problem:
Implement Stack using Linked List

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/implement-stack-using-linked-list/1

Approach:
Use a linked list where the head
represents the top of the stack.

Push operation inserts a new node
at the beginning of the list.

Pop operation removes and returns
the head node.

This follows the LIFO principle.

Time Complexity:
push() -> O(1)
pop() -> O(1)

Space Complexity:
O(n)

Pattern:
Stack Implementation
"""

class MyStack:

    def __init__(self):
        self.top = None

    def push(self, data):

        new = StackNode(data)

        new.next = self.top
        self.top = new

    def pop(self):

        if self.top is None:
            return -1

        val = self.top.data
        self.top = self.top.next

        return val
