"""
Problem:
Rearrange Array Elements by Sign

Source:
LeetCode

Link:
https://leetcode.com/problems/rearrange-array-elements-by-sign/

Approach:
Use two pointers to place positive numbers at even indices
and negative numbers at odd indices.
Maintain order by traversing once.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Array Rearrangement
"""

def rearrange_array(nums):
    n = len(nums)
    result = [0] * n

    pos_index = 0
    neg_index = 1

    for num in nums:
        if num > 0:
            result[pos_index] = num
            pos_index += 2
        else:
            result[neg_index] = num
            neg_index += 2

    return result
