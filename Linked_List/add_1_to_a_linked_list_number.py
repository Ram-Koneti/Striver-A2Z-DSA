"""
Problem:
Add 1 to a Linked List Number

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1

Approach:
Reverse the linked list so that
addition starts from the least
significant digit.

Add 1 and propagate the carry.

If a carry remains after processing
all nodes, create a new node.

Finally reverse the list again
to restore the original order.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Linked List Reversal
"""

class Solution:

    def reverse(self, head):

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def addOne(self, head):

        head = self.reverse(head)

        curr = head
        carry = 1

        while curr and carry:

            total = curr.data + carry
            curr.data = total % 10
            carry = total // 10

            if not curr.next and carry:
                curr.next = Node(carry)
                carry = 0

            curr = curr.next

        return self.reverse(head)
