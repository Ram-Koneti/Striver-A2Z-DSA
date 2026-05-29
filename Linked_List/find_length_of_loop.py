"""
Problem:
Find Length of Loop

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/find-length-of-loop/1

Approach:
Use Floyd’s Cycle Detection Algorithm.

- slow moves one step
- fast moves two steps

If both pointers meet,
a loop exists.

To find loop length:
start from meeting point
and traverse the loop
until reaching the same node again.

Count the number of nodes visited.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Linked List / Floyd Cycle Detection
"""

class Solution:

    def countNodesInLoop(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            # Loop detected
            if slow == fast:

                count = 1
                temp = slow.next

                while temp != slow:

                    count += 1
                    temp = temp.next

                return count

        return 0
