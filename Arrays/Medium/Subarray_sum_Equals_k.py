"""
Problem:
Subarray Sum Equals K

Source:
LeetCode

Link:
https://leetcode.com/problems/subarray-sum-equals-k/

Approach:
Use prefix sum and hashmap.
Store frequency of prefix sums.
If (current_sum - k) exists, add its frequency to count.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Prefix Sum + HashMap
"""

def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0
    prefix_map = {0: 1}

    for num in nums:
        prefix_sum += num

        if (prefix_sum - k) in prefix_map:
            count += prefix_map[prefix_sum - k]

        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count
