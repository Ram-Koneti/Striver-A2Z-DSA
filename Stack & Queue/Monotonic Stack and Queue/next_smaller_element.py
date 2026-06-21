"""
Problem:
Next Smaller Element

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/help-classmates--141631/1

Approach:
Use a monotonic increasing stack
while traversing from right to left.

Remove all elements greater than
or equal to the current element.

The stack top then represents the
next smaller element.

If the stack becomes empty,
there is no smaller element on
the right, so store -1.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Monotonic Stack
"""

class Solution:

    def nextSmallerElement(self, arr):

        n = len(arr)

        ans = [-1] * n

        stack = []

        for i in range(n - 1, -1, -1):

            while stack and stack[-1] >= arr[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1]

            stack.append(arr[i])

        return ans
