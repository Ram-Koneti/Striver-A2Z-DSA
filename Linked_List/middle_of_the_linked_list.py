"""
Problem:
Middle of the Linked List

Source:
LeetCode

Link:
https://leetcode.com/problems/middle-of-the-linked-list/

Approach:
Use slow and fast pointers.

- slow moves one step
- fast moves two steps

When fast reaches the end,
slow will be at the middle node.

If there are two middle nodes,
this returns the second middle node.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Linked List / Two Pointers
"""

class Solution:

    def middleNode(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        return slow
