"""
Problem:
40. Combination Sum II

Source:
LeetCode

Link:
https://leetcode.com/problems/combination-sum-ii/

Approach:
Use backtracking with sorting and duplicate skipping.

First, sort the array to bring duplicate elements together.

For every element, we have two choices:
1. Include the current element and move to the next index.
2. Exclude the current element and move to the next index.

Each element can be used only once.

To avoid duplicate combinations:
- Skip consecutive duplicate elements when excluding an element.
- Sorting helps identify duplicates easily.

If the current sum equals k:
    Add a copy of the current combination to the result.

If the sum exceeds k or the index reaches n:
    Stop the recursion.

Time Complexity:
O(2^n * n) including copying combinations.

Space Complexity:
O(n) for the recursion stack and current combination,
excluding the output.

Pattern:
Backtracking / Include-Exclude / Duplicate Skipping
"""

class Solution:
    def combinationSum2(self, arr: List[int], k: int) -> List[List[int]]:

        arr.sort()
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

            # Include current element (use only once)
            curr.append(arr[ind])
            dfs(ind + 1, curr, sumi + arr[ind])

            # Undo the choice
            curr.pop()

            # Skip duplicate elements
            while ind + 1 < n and arr[ind] == arr[ind + 1]:
                ind += 1

            # Exclude current element
            dfs(ind + 1, curr, sumi)

        dfs(0, [], 0)

        return res
