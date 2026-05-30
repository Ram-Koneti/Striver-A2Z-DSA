"""
Problem:
Delete the Middle Node of a Linked List

Source:
LeetCode

Link:
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

Approach:
Use slow and fast pointers to find
the middle node.

Keep a previous pointer to track
the node before the middle.

When fast reaches the end,
slow will be at the middle node.

Remove the middle node by updating
the previous node's next pointer.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Fast & Slow Pointers
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head):

        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head
