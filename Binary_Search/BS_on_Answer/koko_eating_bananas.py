"""
Problem:
Koko Eating Bananas

Source:
LeetCode

Link:
https://leetcode.com/problems/koko-eating-bananas/

Approach:
Use binary search on eating speed.
For each speed, calculate total hours needed.
Find the minimum speed that allows finishing within h hours.

Time Complexity:
O(n log(max(piles)))

Space Complexity:
O(1)

Pattern:
Binary Search on Answer
"""

import math

def min_eating_speed(piles, h):
    low = 1
    high = max(piles)
    answer = high

    while low <= high:
        mid = (low + high) // 2

        total_hours = 0

        for bananas in piles:
            total_hours += math.ceil(bananas / mid)

        if total_hours <= h:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer
