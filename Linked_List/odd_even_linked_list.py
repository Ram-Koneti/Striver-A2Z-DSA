"""
Problem:
Odd Even Linked List

Source:
LeetCode

Link:
https://leetcode.com/problems/odd-even-linked-list/

Approach:
Maintain two separate chains:
one for odd-indexed nodes and
one for even-indexed nodes.

Traverse the list and reconnect
the pointers so that all odd nodes
come first followed by all even nodes.

Finally attach the even list
to the end of the odd list.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Linked List Manipulation
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head):

        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:

            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head
