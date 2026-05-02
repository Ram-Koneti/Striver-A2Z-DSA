"""
Problem:
Two Sum

Source:
LeetCode

Link:
https://leetcode.com/problems/two-sum/

Approach:
Use hashmap (dictionary) to store visited numbers and their indices.
For each element, check if (target - current) exists in the hashmap.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Hashing / Lookup
"""

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
