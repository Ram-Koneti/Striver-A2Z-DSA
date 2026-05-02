"""
Problem:
Max Consecutive Ones

Source:
LeetCode

Link:
https://leetcode.com/problems/max-consecutive-ones/

Approach:
Traverse the array and count consecutive 1s.
Reset the count when a 0 is encountered.
Track the maximum count.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Array Traversal / Counting
"""

def max_consecutive_ones(nums):
    count = 0
    max_count = 0

    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count
