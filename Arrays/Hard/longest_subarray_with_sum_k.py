"""
Problem:
Longest Subarray with Sum K

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

Approach:
Use prefix sum and hashmap.
Store the first occurrence of each prefix sum.
If (prefix_sum - k) exists in hashmap, a subarray with sum k is found.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Prefix Sum + HashMap
"""

def longest_subarray_sum_k(arr, k):
    prefix_sum = 0
    prefix_map = {}
    max_len = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == k:
            max_len = i + 1

        if (prefix_sum - k) in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum - k])

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_len
