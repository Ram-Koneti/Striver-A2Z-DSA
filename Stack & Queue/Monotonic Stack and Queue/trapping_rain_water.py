"""
Problem:
Trapping Rain Water

Source:
LeetCode

Link:
https://leetcode.com/problems/trapping-rain-water/

Approach:
Use two pointers from both ends
of the elevation map.

Maintain the maximum height seen
so far from the left and right.

If the left height is smaller,
the trapped water depends on
left_max.

Otherwise, it depends on
right_max.

Accumulate trapped water while
moving the pointers inward.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Two Pointers
"""

class Solution:

    def trap(self, height: List[int]) -> int:

        n = len(height)

        l = 0
        r = n - 1

        leftmax = 0
        rightmax = 0

        water = 0

        while l <= r:

            if height[l] <= height[r]:

                if leftmax <= height[l]:
                    leftmax = height[l]

                else:
                    water += leftmax - height[l]

                l += 1

            else:

                if rightmax <= height[r]:
                    rightmax = height[r]

                else:
                    water += rightmax - height[r]

                r -= 1

        return water
