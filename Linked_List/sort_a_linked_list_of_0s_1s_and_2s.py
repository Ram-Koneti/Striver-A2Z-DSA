"""
Problem:
Sort a Linked List of 0s, 1s and 2s

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

Approach:
Create three separate lists
for nodes containing 0, 1, and 2.

Traverse the original list and
attach each node to its respective list.

Finally connect the three lists:
0s -> 1s -> 2s.

This rearranges existing nodes
without modifying node values.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Linked List Partitioning
"""

class Solution:
    def segregate(self, head):

        zero = Node(-1)
        one = Node(-1)
        two = Node(-1)

        z = zero
        o = one
        t = two

        curr = head

        while curr:

            if curr.data == 0:
                z.next = curr
                z = z.next

            elif curr.data == 1:
                o.next = curr
                o = o.next

            else:
                t.next = curr
                t = t.next

            curr = curr.next

        z.next = one.next if one.next else two.next
        o.next = two.next
        t.next = None

        return zero.next
