"""
Problem:
Subarrays with K Different Integers

Source:
LeetCode

Link:
https://leetcode.com/problems/subarrays-with-k-different-integers/

Approach:
Use Sliding Window with
the At Most technique.

The number of subarrays
with exactly k distinct
integers is:

AtMost(k) -
AtMost(k - 1)

The helper function
counts the number of
subarrays containing at
most k distinct integers.

Maintain two pointers:

left
right

The hash map stores the
frequency of each integer
inside the current
window.

Expand the window by
moving the right pointer.

If the number of distinct
integers exceeds k,
shrink the window from
the left.

For every valid window,
add its length to the
answer.

Time Complexity:
O(n)

Space Complexity:
O(k)

Pattern:
Sliding Window + HashMap
"""

class Solution:

    def subarraysWithKDistinct(
        self,
        nums: List[int],
        k: int
    ) -> int:

        return (
            self.atMost(nums, k)
            - self.atMost(nums, k - 1)
        )

    def atMost(
        self,
        nums: List[int],
        k: int
    ) -> int:

        if k < 0:
            return 0

        left = 0
        count = 0

        hashMap = {}

        for right in range(len(nums)):

            hashMap[nums[right]] = (
                hashMap.get(nums[right], 0) + 1
            )

            while len(hashMap) > k:

                hashMap[nums[left]] -= 1

                if hashMap[nums[left]] == 0:
                    del hashMap[nums[left]]

                left += 1

            count += right - left + 1

        return count
