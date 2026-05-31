"""
Problem:
Pair Sum in Doubly Linked List

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1

Approach:
Since the DLL is sorted,
use two pointers.

Place one pointer at the head
and the other at the tail.

If their sum equals target,
store the pair.

If the sum is smaller than target,
move the left pointer forward.

If the sum is greater than target,
move the right pointer backward.

Time Complexity:
O(n)

Space Complexity:
O(1) (excluding output list)

Pattern:
Two Pointers
"""

class Solution:
    def findPairsWithGivenSum(self, target, head):

        ans = []

        # Left pointer at head
        left = head

        # Right pointer at tail
        right = head
        while right.next:
            right = right.next

        # Two pointer traversal
        while left and right and left != right and left.prev != right:

            curr_sum = left.data + right.data

            # Pair found
            if curr_sum == target:
                ans.append([left.data, right.data])

                left = left.next
                right = right.prev

            # Need larger sum
            elif curr_sum < target:
                left = left.next

            # Need smaller sum
            else:
                right = right.prev

        return ans
