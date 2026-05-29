"""
Problem:
Palindrome Linked List

Source:
LeetCode

Link:
https://leetcode.com/problems/palindrome-linked-list/

Approach:
1. Find middle of linked list
   using slow and fast pointers.

2. Reverse second half
   of the linked list.

3. Compare first half
   and reversed second half.

If all nodes match,
the linked list is palindrome.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Linked List / Two Pointers
"""

class Solution:

    def isPalindrome(self, head):

        slow = head
        fast = head

        # Find middle
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None

        while slow:

            next_node = slow.next

            slow.next = prev

            prev = slow
            slow = next_node

        # Compare both halves
        left = head
        right = prev

        while right:

            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
