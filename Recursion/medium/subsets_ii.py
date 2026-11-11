"""
Problem:
90. Subsets II

Source:
LeetCode

Link:
https://leetcode.com/problems/subsets-ii/

Approach:
Use backtracking with sorting and duplicate skipping.

First, sort the array to bring duplicate elements together.

For every element, we have two choices:
1. Include the current element.
2. Exclude the current element.

After exploring the include path:
- Backtrack using pop().
- Skip consecutive duplicate elements.
- Explore the exclude path.

When the index reaches n, add a copy of the current
subset to the result.

Sorting and skipping duplicates ensure that no duplicate
subsets are generated.

Time Complexity:
O(n * 2^n)

Space Complexity:
O(n) for the recursion stack and current subset,
excluding the output.

Pattern:
Backtracking / Include-Exclude / Duplicate Skipping
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
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

            # Skip duplicate elements
            while ind + 1 < n and nums[ind] == nums[ind + 1]:
                ind += 1

            # Exclude current element
            backtrack(ind + 1, curr)

        backtrack(0, [])

        return res
