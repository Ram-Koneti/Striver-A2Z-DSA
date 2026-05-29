"""
Problem:
Linked List Cycle

Source:
LeetCode

Link:
https://leetcode.com/problems/linked-list-cycle/

Approach:
Use slow and fast pointers.

- slow moves one step
- fast moves two steps

If a cycle exists,
both pointers will meet.

If fast reaches the end,
there is no cycle.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Linked List / Floyd Cycle Detection
"""

class Solution:

    def hasCycle(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
