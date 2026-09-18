"""
Problem:
Subsequence with Sum K

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/subsequence-with-sum-k/1

Approach:
Use backtracking with the include-exclude pattern.

For every element, we have two choices:
1. Include the current element in the subsequence.
2. Exclude the current element.

Keep track of the current sum.

If the current sum becomes equal to k, return True.
If the sum becomes greater than k, return False.
If all elements are processed without reaching k, return False.

If either the include or exclude path returns True,
a valid subsequence exists.

Time Complexity:
O(2^n)

Space Complexity:
O(n) due to the recursive call stack.

Pattern:
Backtracking / Include-Exclude
"""

class Solution:
    def checkSubsequenceSum(self, arr, k):

        n = len(arr)

        def backtrack(ind, sumi):

            # Base case: target sum found
            if sumi == k:
                return True

            # Stop if sum exceeds k
            if sumi > k:
                return False

            # No elements left
            if ind >= n:
                return False

            # Include arr[ind]
            if backtrack(ind + 1, sumi + arr[ind]):
                return True

            # Exclude arr[ind]
            if backtrack(ind + 1, sumi):
                return True

            return False

        return backtrack(0, 0)
