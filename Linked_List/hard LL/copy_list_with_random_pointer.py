"""
Problem:
Copy List with Random Pointer

Source:
LeetCode

Link:
https://leetcode.com/problems/copy-list-with-random-pointer/

Approach:
Insert copied nodes in between
original nodes.

Set random pointers for copied nodes
using original.random.next.

Separate the copied list from the
original list while restoring the
original structure.

This avoids using extra hashmap space.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Linked List Cloning
"""

# Definition for a Node.
# class Node:
#     def __init__(self, x, next=None, random=None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head):

        if not head:
            return None

        curr = head

        # Step 1: Insert copy nodes
        while curr:

            copy = Node(curr.val)

            copy.next = curr.next
            curr.next = copy

            curr = copy.next

        curr = head

        # Step 2: Set random pointers
        while curr:

            if curr.random:
                curr.next.random = curr.random.next

            curr = curr.next.next

        curr = head

        dummy = Node(0)
        copy_curr = dummy

        # Step 3: Separate both lists
        while curr:

            copy = curr.next

            curr.next = copy.next

            copy_curr.next = copy
            copy_curr = copy

            curr = curr.next

        return dummy.next
