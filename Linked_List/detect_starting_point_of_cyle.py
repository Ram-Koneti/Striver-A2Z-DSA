"""
Problem:
Linked List Cycle II

Source:
LeetCode

Link:
https://leetcode.com/problems/linked-list-cycle-ii/

Approach:
Use Floyd’s Cycle Detection Algorithm.

Step 1:
Use slow and fast pointers
to detect the cycle.

Step 2:
When both pointers meet,
move one pointer to head.

Now move both pointers
one step at a time.

The node where they meet again
is the starting node of the cycle.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Linked List / Floyd Cycle Detection
"""

class Solution:

    def detectCycle(self, head):

        slow = head
        fast = head

        # Detect cycle
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                ptr = head

                while ptr != slow:

                    ptr = ptr.next
                    slow = slow.next

                return ptr

        return None
