"""
Problem:
Rotate Array (Right Rotation by K steps)

Source:
LeetCode

Link:
https://leetcode.com/problems/rotate-array/

Approach:
Use reversal algorithm:
1. Reverse entire array
2. Reverse first k elements
3. Reverse remaining elements

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Array Rotation / Reversal
"""

def rotate_array(nums, k):
    n = len(nums)
    if n == 0:
        return nums

    k = k % n

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

    return nums
