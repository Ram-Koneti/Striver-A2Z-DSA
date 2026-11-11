"""
Problem:
216. Combination Sum III

Source:
LeetCode

Link:
https://leetcode.com/problems/combination-sum-iii/

Approach:
Use backtracking with the include-exclude pattern.

Only numbers from 1 to 9 can be used, and each number
can be selected only once.

For every number, we have two choices:
1. Include the current number.
2. Exclude the current number.

Maintain three variables:
- curr: Current combination.
- sumi: Current sum.
- m: Number of elements selected.

If m == k and sumi == n:
    Add a copy of the current combination to the result.

Stop recursion if:
- m > k
- sumi > n
- i > 9

After including a number, use pop() to backtrack.

Time Complexity:
O(2^9)

Space Complexity:
O(k) for the recursion stack and current combination,
excluding the output.

Pattern:
Backtracking / Include-Exclude
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []

        def dfs(i, curr, sumi, m):

            # Base case: valid combination found
            if m == k and sumi == n:
                res.append(curr.copy())
                return

            # Pruning conditions
            if m > k or sumi > n or i > 9:
                return

            # Include current number
            curr.append(i)
            dfs(i + 1, curr, sumi + i, m + 1)

            # Undo the choice
            curr.pop()

            # Exclude current number
            dfs(i + 1, curr, sumi, m)

        dfs(1, [], 0, 0)

        return res
