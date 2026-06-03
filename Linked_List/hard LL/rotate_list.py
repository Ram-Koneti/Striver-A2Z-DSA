"""
Problem:
Rotate List

Source:
LeetCode

Link:
https://leetcode.com/problems/rotate-list/

Approach:
Find the length of the linked list
and connect the tail to the head
to form a circular list.

The new head will be at position
(length - k % length) from the start.

Break the circle at the new tail
and return the new head.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Linked List Traversal
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):

        # Empty list or single node
        if not head or not head.next:
            return head

        # Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Make list circular
        tail.next = head

        # Find new tail
        steps = length - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # New head is next of new tail
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head
