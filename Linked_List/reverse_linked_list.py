"""
Problem:
Reverse Linked List

Source:
LeetCode

Link:
https://leetcode.com/problems/reverse-linked-list/

Approach:
Use three pointers:
- prev
- curr
- next_node

Reverse links one by one
while traversing the list.

Finally return prev
as the new head.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Linked List / Iterative Reversal
"""

class Solution:

    def reverseList(self, head):

        prev = None
        curr = head

        while curr:

            next_node = curr.next

            curr.next = prev

            prev = curr
            curr = next_node

        return prev
