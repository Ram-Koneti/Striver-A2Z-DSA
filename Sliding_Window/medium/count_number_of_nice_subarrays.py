"""
Problem:
Count Number of Nice Subarrays

Source:
LeetCode

Link:
https://leetcode.com/problems/count-number-of-nice-subarrays/

Approach:
Use Sliding Window with
the At Most technique.

A nice subarray contains
exactly k odd numbers.

The answer is:

AtMost(k) -
AtMost(k - 1)

The helper function
counts the number of
subarrays containing at
most k odd numbers.

Treat every odd number as
1 and every even number
as 0.

Maintain two pointers:

left
right

Expand the window by
moving the right pointer.

If the number of odd
numbers exceeds k,
shrink the window from
the left.

For every valid window,
add its length to the
answer.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Sliding Window + At Most
"""

class Solution:

    def numberOfSubarrays(
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
        oddCount = 0
        count = 0

        for right in range(len(nums)):

            oddCount += nums[right] % 2

            while oddCount > k:

                oddCount -= nums[left] % 2
                left += 1

            count += right - left + 1

        return count
