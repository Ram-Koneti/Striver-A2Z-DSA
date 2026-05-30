"""
Problem:
Remove Nth Node From End of List

Source:
LeetCode

Link:
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Approach:
Use two pointers with a dummy node.

Move the fast pointer n steps ahead.
Then move both fast and slow pointers
until fast reaches the last node.

The slow pointer will be just before
the node to be removed.

Update the links and return the head.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Two Pointers / Linked List
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
