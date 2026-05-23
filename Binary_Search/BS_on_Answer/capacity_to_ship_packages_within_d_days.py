"""
Problem:
Capacity To Ship Packages Within D Days

Source:
LeetCode

Link:
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

Approach:
Use binary search on ship capacity.
For each capacity, calculate how many days are needed.
Find the minimum capacity that ships all packages within given days.

Time Complexity:
O(n log(sum(weights)))

Space Complexity:
O(1)

Pattern:
Binary Search on Answer
"""

def ship_within_days(weights, days):

    def required_days(capacity):
        days_needed = 1
        current_weight = 0

        for weight in weights:

            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = weight
            else:
                current_weight += weight

        return days_needed

    low = max(weights)
    high = sum(weights)
    answer = high

    while low <= high:
        mid = (low + high) // 2

        if required_days(mid) <= days:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer
