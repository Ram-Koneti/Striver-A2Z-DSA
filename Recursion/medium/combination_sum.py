"""
Problem:
39. Combination Sum

Source:
LeetCode

Link:
https://leetcode.com/problems/combination-sum/

Approach:
Use backtracking with the include-exclude pattern.

For every element, we have two choices:
1. Include the current element.
   Stay at the same index because the element can be reused.
2. Exclude the current element.
   Move to the next index.

If the current sum equals k:
    Add a copy of the current combination to the result.

If the index reaches n or the sum exceeds k:
    Stop the recursion.

Time Complexity:
O(2^(k/m) * k), where m is the smallest candidate.
This is an upper-bound style estimate for the search.

Space Complexity:
O(k/m) for the recursion stack and current combination,
excluding the output.

Pattern:
Backtracking / Include-Exclude
"""

class Solution:
    def combinationSum(self, arr: List[int], k: int) -> List[List[int]]:

        n = len(arr)
        res = []

        def dfs(ind, curr, sumi):

            # Target sum found
            if sumi == k:
                res.append(curr.copy())
                return

            # Invalid condition
            if ind >= n or sumi > k:
                return

            # Include current element (reuse allowed)
            curr.append(arr[ind])
            dfs(ind, curr, sumi + arr[ind])

            # Undo the choice
            curr.pop()

            # Exclude current element
            dfs(ind + 1, curr, sumi)

        dfs(0, [], 0)

        return res
