"""
Problem:
Majority Element II

Source:
LeetCode

Link:
https://leetcode.com/problems/majority-element-ii/

Approach:
Use extended Boyer-Moore Voting Algorithm.
At most two elements can appear more than n/3 times.
Find two candidates, then verify their counts.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Boyer-Moore Voting Algorithm
"""

def majority_element_n_by_3(nums):
    candidate1 = candidate2 = None
    count1 = count2 = 0

    # Step 1: find candidates
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    # Step 2: verify candidates
    result = []
    count1 = count2 = 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    n = len(nums)
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)

    return result
