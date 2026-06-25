"""
Problem:
Sliding Window Maximum

Source:
LeetCode

Link:
https://leetcode.com/problems/sliding-window-maximum/

Approach:
Use a deque to maintain indices
in decreasing order of values.

Remove indices that are outside
the current window.

While the current element is
greater than or equal to the
elements at the back of the deque,
remove them.

The front of the deque always
contains the index of the maximum
element in the current window.

Once the first window is formed,
record the maximum for every
window.

Time Complexity:
O(n)

Space Complexity:
O(k)

Pattern:
Monotonic Queue
"""

from collections import deque

class Solution:

    def maxSlidingWindow(
        self,
        nums: List[int],
        k: int
    ) -> List[int]:

        n = len(nums)

        maxArr = []

        dq = deque()

        for i in range(n):

            if dq and dq[0] <= i - k:
                dq.popleft()

            while (
                dq and
                nums[i] >= nums[dq[-1]]
            ):
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                maxArr.append(nums[dq[0]])

        return maxArr
