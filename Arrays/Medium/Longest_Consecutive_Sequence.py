"""
Problem:
Longest Consecutive Sequence

Source:
LeetCode

Link:
https://leetcode.com/problems/longest-consecutive-sequence/

Approach:
Use a set for O(1) lookups.
Only start counting when the current number is the start of a sequence
(i.e., num - 1 is not in the set).

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Hashing / Set
"""

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # start of sequence
            current = num
            count = 1

            while current + 1 in num_set:
                current += 1
                count += 1

            longest = max(longest, count)

    return longest
