"""
Problem:
Flattening a Linked List

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1

Approach:
Use recursion to flatten the
linked list from right to left.

First flatten the list starting
from head.next.

Then merge the current bottom list
with the already flattened list.

Since all lists are sorted,
merge them like two sorted lists.

Time Complexity:
O(n * m)

Space Complexity:
O(n)   # Recursive stack

Pattern:
Merge Two Sorted Linked Lists
"""

class Solution:

    # Merge two sorted bottom-linked lists
    def merge(self, a, b):

        dummy = Node(0)
        curr = dummy

        while a and b:

            if a.data <= b.data:
                curr.bottom = a
                a = a.bottom
            else:
                curr.bottom = b
                b = b.bottom

            curr = curr.bottom

        # Attach remaining nodes
        curr.bottom = a if a else b

        return dummy.bottom

    def flatten(self, head):

        # Base case
        if not head or not head.next:
            return head

        # Flatten remaining lists
        merged_head = self.flatten(head.next)

        # Merge current list with flattened list
        return self.merge(head, merged_head)
