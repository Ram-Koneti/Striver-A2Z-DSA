"""
Problem:
Majority Element

Source:
LeetCode

Link:
https://leetcode.com/problems/majority-element/

Approach:
Use Boyer-Moore Voting Algorithm.
Keep a candidate and a count.
If count becomes 0, update candidate.
Increase count if same, decrease if different.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Boyer-Moore Voting Algorithm
"""

def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate
