"""
Problem:
Sum of Subarray Minimums

Source:
LeetCode

Link:
https://leetcode.com/problems/sum-of-subarray-minimums/

Approach:
For each element, find:

1. Previous Smaller Element (PSE)
2. Next Smaller Element (NSE)

Calculate how many subarrays
use arr[i] as their minimum.

left = i - pse[i]
right = nse[i] - i

Contribution:

arr[i] * left * right

Sum the contributions of all
elements and return the result
modulo 10^9 + 7.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Monotonic Stack Contribution
"""

class Solution:

    def sumSubarrayMins(
        self,
        arr: List[int]
    ) -> int:

        n = len(arr)

        mod = 10**9 + 7

        nse = self.findNse(arr)
        pse = self.findPse(arr)

        ans = 0

        for i in range(n):

            left = i - pse[i]
            right = nse[i] - i

            ans = (
                ans +
                arr[i] * left * right
            ) % mod

        return ans

    def findNse(self, arr):

        n = len(arr)

        nse = [n] * n

        stack = []

        for i in range(n - 1, -1, -1):

            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]

            stack.append(i)

        return nse

    def findPse(self, arr):

        n = len(arr)

        pse = [-1] * n

        stack = []

        for i in range(n):

            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                pse[i] = stack[-1]

            stack.append(i)

        return pse
