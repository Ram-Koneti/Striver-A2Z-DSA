"""
Problem:
4Sum

Source:
LeetCode

Link:
https://leetcode.com/problems/4sum/

Approach:
1. Sort the array
2. Fix two elements
3. Use two pointers to find remaining two numbers
4. Skip duplicates to avoid repeated quadruplets

Time Complexity:
O(n^3)

Space Complexity:
O(1) (excluding output)

Pattern:
Sorting + Two Pointer
"""

def four_sum(nums, target):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n):

        # skip duplicates for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n):

            # skip duplicates for j
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total < target:
                    left += 1

                elif total > target:
                    right -= 1

                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

    return result
