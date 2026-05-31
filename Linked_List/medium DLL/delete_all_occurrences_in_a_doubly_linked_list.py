"""
Problem:
Delete all Occurrences in a Doubly Linked List

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1

Approach:
Traverse the DLL.

Whenever a node with value x is found,
remove it by updating the previous
and next pointers.

Handle the head node separately.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Doubly Linked List Manipulation
"""

class Solution:
    def deleteAllOccurOfX(self, head, x):

        curr = head

        while curr:

            # Store next node before deletion
            nxt = curr.next

            # Delete current node if value matches x
            if curr.data == x:

                # Update previous node's next pointer
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    head = curr.next

                # Update next node's prev pointer
                if curr.next:
                    curr.next.prev = curr.prev

            curr = nxt

        return head
