"""
Problem:
Implement Stack using Arrays

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/implement-stack-using-array/1

Approach:
Use a Python list as the underlying
array for stack implementation.

Push operation appends an element
to the end of the list.

Pop operation removes and returns
the last element from the list.

The last inserted element is removed
first, following the LIFO principle.

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
        self.arr = []

    def push(self, data):
        self.arr.append(data)

    def pop(self):
        if len(self.arr) == 0:
            return -1
        return self.arr.pop()
