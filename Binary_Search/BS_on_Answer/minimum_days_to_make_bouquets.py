"""
Problem:
Minimum Number of Days to Make m Bouquets

Source:
LeetCode

Link:
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

Approach:
Use binary search on number of days.
For each day, check if it is possible to make
m bouquets using k adjacent flowers.

Time Complexity:
O(n log(max(bloomDay)))

Space Complexity:
O(1)

Pattern:
Binary Search on Answer
"""

def min_days(bloom_day, m, k):

    if m * k > len(bloom_day):
        return -1

    def can_make(days):
        bouquets = 0
        flowers = 0

        for bloom in bloom_day:

            if bloom <= days:
                flowers += 1

                if flowers == k:
                    bouquets += 1
                    flowers = 0

            else:
                flowers = 0

        return bouquets >= m

    low = min(bloom_day)
    high = max(bloom_day)
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if can_make(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer
