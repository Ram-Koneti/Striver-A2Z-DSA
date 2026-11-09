"""
Problem:
78. Subsets

Source:
LeetCode

Link:
https://leetcode.com/problems/subsets/

Approach:
Use backtracking with the include-exclude pattern.

For every element, we have two choices:
1. Include the current element.
2. Exclude the current element.

Recursively explore both choices.

When the index reaches n, all elements have been
considered, so add a copy of the current subset to res.

Use pop() to undo the include choice before exploring
the exclude choice.

Time Complexity:
O(n * 2^n)

Space Complexity:
O(n) for the recursion stack and current subset,
excluding the output.

Pattern:
Backtracking / Include-Exclude
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []

        def backtrack(ind, curr):

            # Base case
            if ind >= n:
                res.append(curr.copy())
                return

            # Include current element
            curr.append(nums[ind])
            backtrack(ind + 1, curr)

            # Undo the choice
            curr.pop()

            # Exclude current element
            backtrack(ind + 1, curr)

        backtrack(0, [])

        return res
