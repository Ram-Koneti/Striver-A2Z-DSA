"""
Problem:
3Sum

Source:
LeetCode

Link:
https://leetcode.com/problems/3sum/

Approach:
1. Sort the array
2. Fix one element
3. Use two pointers to find pairs with sum = -nums[i]
4. Skip duplicates to avoid repeated triplets

Time Complexity:
O(n^2)

Space Complexity:
O(1) (excluding output)

Pattern:
Sorting + Two Pointer
"""

def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n):

        # skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1

            elif total > 0:
                right -= 1

            else:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # skip duplicate values
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result
