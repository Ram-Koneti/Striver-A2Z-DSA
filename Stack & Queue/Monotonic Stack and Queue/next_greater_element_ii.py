"""
Problem:
Next Greater Element II

Source:
LeetCode

Link:
https://leetcode.com/problems/next-greater-element-ii/

Approach:
Use a monotonic decreasing stack
and traverse the array twice
from right to left.

The second traversal simulates
the circular nature of the array.

Remove all elements smaller than
or equal to the current element.

The stack top then represents the
next greater element.

Store answers only during the
first pass through the array.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Circular Monotonic Stack
"""

class Solution:

    def nextGreaterElements(
        self,
        nums: List[int]
    ) -> List[int]:

        n = len(nums)

        ans = [-1] * n

        stack = []

        for i in range(2 * n - 1, -1, -1):

            while stack and stack[-1] <= nums[i % n]:
                stack.pop()

            if i < n and stack:
                ans[i] = stack[-1]

            stack.append(nums[i % n])

        return ans
