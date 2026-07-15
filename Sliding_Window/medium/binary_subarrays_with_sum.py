"""
Problem:
Binary Subarrays With Sum

Source:
LeetCode

Link:
https://leetcode.com/problems/binary-subarrays-with-sum/

Approach:
Use Sliding Window with
the At Most technique.

The number of subarrays
with sum exactly equal to
goal is:

AtMost(goal) -
AtMost(goal - 1)

The helper function
counts the number of
subarrays whose sum is
less than or equal to k.

Maintain two pointers:

left
right

Expand the window by
moving the right pointer.

If the window sum exceeds
k, shrink it from the
left.

For every valid window,
add its length to the
answer because every
subarray ending at right
is valid.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Sliding Window + At Most
"""

class Solution:

    def numSubarraysWithSum(
        self,
        nums: List[int],
        goal: int
    ) -> int:

        return (
            self.atMost(nums, goal)
            - self.atMost(nums, goal - 1)
        )

    def atMost(
        self,
        nums: List[int],
        k: int
    ) -> int:

        if k < 0:
            return 0

        left = 0
        windowSum = 0
        count = 0

        for right in range(len(nums)):

            windowSum += nums[right]

            while windowSum > k:

                windowSum -= nums[left]
                left += 1

            count += right - left + 1

        return count
