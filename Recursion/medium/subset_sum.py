"""
Problem:
Subset Sum Problem

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

Approach:
Use recursion with the include-exclude pattern.

For every element, we have two choices:
1. Include the current element in the subset.
2. Exclude the current element from the subset.

Maintain the remaining target sum.

If target becomes 0:
    A valid subset is found. Return True.

If the index reaches n:
    All elements are processed. Return False.

If either include or exclude path returns True,
a valid subset exists.

Since all array elements are positive, we can also
stop when the remaining target becomes negative.

Time Complexity:
O(2^n)

Space Complexity:
O(n) due to the recursive call stack.

Pattern:
Recursion / Backtracking / Include-Exclude
"""

class Solution:
    def isSubsetSum(self, arr, sum):
        
        n = len(arr)

        def dfs(ind, target):

            # Target found
            if target == 0:
                return True

            # No elements left
            if ind >= n or target < 0:
                return False

            # Include current element
            if dfs(ind + 1, target - arr[ind]):
                return True

            # Exclude current element
            if dfs(ind + 1, target):
                return True

            return False

        return dfs(0, sum)
