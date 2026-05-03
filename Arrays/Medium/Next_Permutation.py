"""
Problem:
Next Permutation

Source:
LeetCode

Link:
https://leetcode.com/problems/next-permutation/

Approach:
1. Find the first index (i) from right where nums[i] < nums[i+1]
2. Find index (j) from right where nums[j] > nums[i]
3. Swap nums[i] and nums[j]
4. Reverse the subarray from i+1 to end

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Array Manipulation / Permutation
"""

def next_permutation(nums):
    n = len(nums)

    # Step 1: find breakpoint
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: find next greater element
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: reverse the suffix
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums
