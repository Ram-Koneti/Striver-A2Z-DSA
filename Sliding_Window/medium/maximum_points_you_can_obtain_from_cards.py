"""
Problem:
Maximum Points You Can Obtain from Cards

Source:
LeetCode

Link:
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

Approach:
Use Sliding Window.

Initially, take the first
k cards from the left and
compute their sum.

Then, one by one,
replace cards taken from
the left with cards from
the right.

Maintain:

leftSum
rightSum

At each step, update the
maximum score.

This considers every
possible combination of
taking cards from the
left and right ends.

Time Complexity:
O(k)

Space Complexity:
O(1)

Pattern:
Sliding Window
"""

class Solution:

    def maxScore(
        self,
        cardPoints: List[int],
        k: int
    ) -> int:

        n = len(cardPoints)

        leftSum = 0
        rightSum = 0
        maxSum = 0

        for i in range(k):

            leftSum += cardPoints[i]
            maxSum = leftSum

        rightIndex = n - 1

        for i in range(k - 1, -1, -1):

            leftSum -= cardPoints[i]
            rightSum += cardPoints[rightIndex]

            maxSum = max(
                maxSum,
                leftSum + rightSum
            )

            rightIndex -= 1

        return maxSum
