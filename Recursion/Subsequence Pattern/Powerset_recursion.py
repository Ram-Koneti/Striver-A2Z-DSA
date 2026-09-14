"""
Problem:
78. Subsets

Source:
LeetCode

Link:
https://leetcode.com/problems/subsets/

Approach:
Use backtracking to generate all possible subsets.

For every element, we have two choices:
1. Include the current element.
2. Exclude the current element.

Recursively explore both choices.

When ind reaches n, all elements have been considered,
so add a copy of the current subset to the result.

After including an element, use pop() to undo the choice
before exploring the exclude path.

Time Complexity:
O(n * 2^n)

Space Complexity:
O(n) for the recursion stack and current subset,
excluding the output.

Pattern:
Backtracking / Include-Exclude
"""

class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:

        n = len(arr)
        res = []

        def backtrack(ind, curr):

            # Base case
            if ind >= n:
                res.append(curr.copy())
                return

            # Include arr[ind]
            curr.append(arr[ind])
            backtrack(ind + 1, curr)

            # Undo the choice
            curr.pop()

            # Exclude arr[ind]
            backtrack(ind + 1, curr)

        backtrack(0, [])

        return res
