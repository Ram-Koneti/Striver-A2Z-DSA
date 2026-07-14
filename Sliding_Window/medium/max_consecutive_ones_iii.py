"""
Problem:
Max Consecutive Ones III

Source:
LeetCode

Link:
https://leetcode.com/problems/max-consecutive-ones-iii/

Approach:
Use Sliding Window.

Maintain two pointers:

left
right

Keep track of the number
of zeros inside the
current window.

Expand the window by
moving the right pointer.

If the number of zeros
exceeds k, shrink the
window from the left
until it becomes valid.

Update the maximum window
length whenever the
window contains at most
k zeros.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Sliding Window
"""

class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:

        n = len(nums)

        left = 0
        zeroCount = 0
        maxLen = 0

        for right in range(n):

            if nums[right] == 0:
                zeroCount += 1

            while zeroCount > k:

                if nums[left] == 0:
                    zeroCount -= 1

                left += 1

            maxLen = max(
                maxLen,
                right - left + 1
            )

        return maxLen
