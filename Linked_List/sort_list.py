"""
Problem:
Sort List

Source:
LeetCode

Link:
https://leetcode.com/problems/sort-list/

Approach:
Use Merge Sort on the linked list.

Find the middle node and split
the list into two halves.

Recursively sort both halves
and merge them into a sorted list.

Merge Sort is preferred because
it achieves O(n log n) time
for linked lists.

Time Complexity:
O(n log n)

Space Complexity:
O(log n)

Pattern:
Merge Sort on Linked List
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head):

        if not head or not head.next:
            return head

        mid = self.get_middle(head)
        right = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(right)

        return self.merge(left, right)

    def get_middle(self, head):

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):

        dummy = ListNode(0)
        tail = dummy

        while left and right:

            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        tail.next = left if left else right

        return dummy.next
