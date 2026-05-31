"""
Problem:
Intersection of Two Linked Lists

Source:
LeetCode

Link:
https://leetcode.com/problems/intersection-of-two-linked-lists/

Approach:
Use two pointers starting at
the heads of both lists.

When a pointer reaches the end,
redirect it to the head of the
other list.

If the lists intersect,
both pointers will meet at the
intersection node.

Otherwise, both will reach None.

Time Complexity:
O(n + m)

Space Complexity:
O(1)

Pattern:
Two Pointers
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):

        p1 = headA
        p2 = headB

        while p1 != p2:

            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1
