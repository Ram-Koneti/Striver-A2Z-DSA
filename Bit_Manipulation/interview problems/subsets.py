"""
Problem:
78. Subsets

Source:
LeetCode

Link:
https://leetcode.com/problems/subsets/

Approach:
Generate all possible
subsets using bit
manipulation.

For an array of size n,
there are 2^n possible
subsets.

Each number from
0 to (2^n - 1)
represents one subset.

If the i-th bit is set,
include nums[i] in the
current subset.

Time Complexity:
O(n * 2^n)

Space Complexity:
O(n * 2^n)

Pattern:
Bit Manipulation
"""

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        res = []

        for num in range(1 << n):

            subset = []

            for i in range(n):

                if num & (1 << i):

                    subset.append(nums[i])

            res.append(subset)

        return res
