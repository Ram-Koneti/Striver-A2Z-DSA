"""
Problem:
Split Array Largest Sum

Source:
LeetCode

Link:
https://leetcode.com/problems/split-array-largest-sum/

Approach:
Use binary search on largest subarray sum.
For each value, check how many subarrays are needed.
Find the minimum possible largest sum.

Time Complexity:
O(n log(sum(nums)))

Space Complexity:
O(1)

Pattern:
Binary Search on Answer
"""

def split_array(nums, k):

    def count_subarrays(max_sum):
        subarrays = 1
        current_sum = 0

        for num in nums:

            if current_sum + num <= max_sum:
                current_sum += num
            else:
                subarrays += 1
                current_sum = num

        return subarrays

    low = max(nums)
    high = sum(nums)
    answer = high

    while low <= high:
        mid = (low + high) // 2

        if count_subarrays(mid) <= k:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer
