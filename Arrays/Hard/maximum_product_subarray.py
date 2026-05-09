"""
Problem:
Maximum Product Subarray

Source:
LeetCode

Link:
https://leetcode.com/problems/maximum-product-subarray/

Approach:
Track both maximum and minimum product ending at current position.
A negative number can turn minimum product into maximum product.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Dynamic Programming / Kadane Variant
"""

def max_product_subarray(nums):
    current_max = nums[0]
    current_min = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):

        if nums[i] < 0:
            current_max, current_min = current_min, current_max

        current_max = max(nums[i], current_max * nums[i])
        current_min = min(nums[i], current_min * nums[i])

        result = max(result, current_max)

    return result
