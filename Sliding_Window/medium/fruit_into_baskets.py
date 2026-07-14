"""
Problem:
Fruit Into Baskets

Source:
LeetCode

Link:
https://leetcode.com/problems/fruit-into-baskets/

Approach:
Use Sliding Window with
HashMap.

Maintain two pointers:

left
right

The hash map stores the
frequency of each fruit
type inside the current
window.

Expand the window by
moving the right pointer.

If the window contains
more than two distinct
fruit types, shrink it
from the left until only
two types remain.

Update the maximum window
length whenever the
window contains at most
two fruit types.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Sliding Window + HashMap
"""

class Solution:

    def totalFruit(self, fruits: List[int]) -> int:

        n = len(fruits)

        left = 0
        maxLen = 0

        hashMap = {}

        for right in range(n):

            hashMap[fruits[right]] = (
                hashMap.get(fruits[right], 0) + 1
            )

            while len(hashMap) > 2:

                hashMap[fruits[left]] -= 1

                if hashMap[fruits[left]] == 0:
                    del hashMap[fruits[left]]

                left += 1

            maxLen = max(
                maxLen,
                right - left + 1
            )

        return maxLen
