"""
Problem:
Sum of Subarray Ranges

Source:
LeetCode

Link:
https://leetcode.com/problems/sum-of-subarray-ranges/

Approach:
Range of a subarray:

maximum - minimum

Therefore:

Sum of Subarray Ranges =
Sum of Subarray Maximums
-
Sum of Subarray Minimums

Use monotonic stacks to find
the contribution of each element
as a maximum and as a minimum.

For each element:

contribution =
value * left * right

Answer:

sumMax - sumMin

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Monotonic Stack Contribution
"""

class Solution:

    def subArrayRanges(
        self,
        nums: List[int]
    ) -> int:

        return (
            self.sumMax(nums) -
            self.sumMin(nums)
        )

    def sumMin(self, nums):

        n = len(nums)

        nse = self.findNse(nums)
        pse = self.findPse(nums)

        total = 0

        for i in range(n):

            left = i - pse[i]
            right = nse[i] - i

            total += (
                nums[i] *
                left *
                right
            )

        return total

    def sumMax(self, nums):

        n = len(nums)

        nge = self.findNge(nums)
        pge = self.findPge(nums)

        total = 0

        for i in range(n):

            left = i - pge[i]
            right = nge[i] - i

            total += (
                nums[i] *
                left *
                right
            )

        return total

    def findNse(self, nums):

        n = len(nums)

        ans = [n] * n

        stack = []

        for i in range(n - 1, -1, -1):

            while (
                stack and
                nums[stack[-1]] >= nums[i]
            ):
                stack.pop()

            if stack:
                ans[i] = stack[-1]

            stack.append(i)

        return ans

    def findPse(self, nums):

        n = len(nums)

        ans = [-1] * n

        stack = []

        for i in range(n):

            while (
                stack and
                nums[stack[-1]] > nums[i]
            ):
                stack.pop()

            if stack:
                ans[i] = stack[-1]

            stack.append(i)

        return ans

    def findNge(self, nums):

        n = len(nums)

        ans = [n] * n

        stack = []

        for i in range(n - 1, -1, -1):

            while (
                stack and
                nums[stack[-1]] <= nums[i]
            ):
                stack.pop()

            if stack:
                ans[i] = stack[-1]

            stack.append(i)

        return ans

    def findPge(self, nums):

        n = len(nums)

        ans = [-1] * n

        stack = []

        for i in range(n):

            while (
                stack and
                nums[stack[-1]] < nums[i]
            ):
                stack.pop()

            if stack:
                ans[i] = stack[-1]

            stack.append(i)

        return ans
