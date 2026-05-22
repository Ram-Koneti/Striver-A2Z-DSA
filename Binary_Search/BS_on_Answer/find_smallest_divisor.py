"""
Problem:
Find the Smallest Divisor Given a Threshold

Source:
LeetCode

Link:
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

Approach:
Use binary search on divisor.
For each divisor, calculate the sum of ceilings.
Find the smallest divisor whose sum <= threshold.

Time Complexity:
O(n log(max(nums)))

Space Complexity:
O(1)

Pattern:
Binary Search on Answer
"""

import math

def smallest_divisor(nums, threshold):

    low = 1
    high = max(nums)
    answer = high

    while low <= high:
        mid = (low + high) // 2

        total = 0

        for num in nums:
            total += math.ceil(num / mid)

        if total <= threshold:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer
