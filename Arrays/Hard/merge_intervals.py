"""
Problem:
Merge Intervals

Source:
LeetCode

Link:
https://leetcode.com/problems/merge-intervals/

Approach:
1. Sort intervals based on start time
2. Compare current interval with last merged interval
3. Merge if overlapping, otherwise add new interval

Time Complexity:
O(n log n)

Space Complexity:
O(n)

Pattern:
Intervals / Sorting
"""

def merge_intervals(intervals):
    intervals.sort()
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
