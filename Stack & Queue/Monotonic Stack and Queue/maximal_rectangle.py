"""
Problem:
Maximal Rectangle

Source:
LeetCode

Link:
https://leetcode.com/problems/maximal-rectangle/

Approach:
Precompute column-wise heights
for consecutive 1s.

For each cell:

If matrix[i][j] is 1,
increase the height.

If matrix[i][j] is 0,
reset the height to 0.

Each row of the height matrix
represents a histogram.

Apply Largest Rectangle in
Histogram on every row and
track the maximum area.

Time Complexity:
O(rows * cols)

Space Complexity:
O(rows * cols)

Pattern:
Histogram + Monotonic Stack
"""

class Solution:

    def maximalRectangle(
        self,
        matrix: List[List[str]]
    ) -> int:

        n = len(matrix)
        m = len(matrix[0])

        psum = [[0] * m for _ in range(n)]

        for j in range(m):

            sumi = 0

            for i in range(n):

                if matrix[i][j] == "0":
                    sumi = 0

                else:
                    sumi += 1

                psum[i][j] = sumi

        maxArea = 0

        for i in range(n):
            maxArea = max(
                maxArea,
                self.lHist(psum[i])
            )

        return maxArea

    def lHist(self, heights):

        n = len(heights)

        stack = []

        maxArea = 0

        for i in range(n):

            while (
                stack and
                heights[i] < heights[stack[-1]]
            ):

                element = stack.pop()

                nse = i

                pse = (
                    stack[-1]
                    if stack
                    else -1
                )

                maxArea = max(
                    maxArea,
                    heights[element] *
                    (nse - pse - 1)
                )

            stack.append(i)

        while stack:

            element = stack.pop()

            nse = n

            pse = (
                stack[-1]
                if stack
                else -1
            )

            maxArea = max(
                maxArea,
                heights[element] *
                (nse - pse - 1)
            )

        return maxArea
