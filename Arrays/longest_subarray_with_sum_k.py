"""
Problem:
Longest Subarray with Sum K

Source:
Striver A2Z DSA Sheet

Link:
https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

Approach:
Use prefix sum and hashmap.
Store first occurrence of each prefix sum.
If (prefix_sum - k) is found in hashmap, it means a subarray with sum k exists.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Prefix Sum + HashMap
"""

def longest_subarray_sum_k(nums, k):
    prefix_sum = 0
    prefix_map = {}
    max_len = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if prefix_sum == k:
            max_len = i + 1

        if (prefix_sum - k) in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum - k])

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_len
