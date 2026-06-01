"""
Problem:
Remove Duplicates from a Sorted DLL

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1

Approach:
Since the DLL is sorted,
duplicate values will be adjacent.

Traverse the list and compare
the current node with its next node.

If both values are equal,
remove the next node by updating
the next and prev pointers.

Otherwise, move to the next node.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Doubly Linked List Manipulation
"""

class Solution:
    def removeDuplicates(self, head):

        curr = head

        while curr and curr.next:

            # Duplicate found
            if curr.data == curr.next.data:

                duplicate = curr.next

                # Remove duplicate node
                curr.next = duplicate.next

                if duplicate.next:
                    duplicate.next.prev = curr

            else:
                # Move to next distinct node
                curr = curr.next

        return head
