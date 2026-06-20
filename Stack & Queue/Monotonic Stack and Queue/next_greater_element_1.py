"""
Problem:
Next Greater Element I

Source:
LeetCode

Link:
https://leetcode.com/problems/next-greater-element-i/

Approach:
Use a monotonic decreasing stack
to preprocess the next greater
element for every number in nums2.

Whenever the current number is
greater than the stack top, it
becomes the next greater element
for that stack element.

Store the mapping in a hashmap.

Use the hashmap to build the
answer for nums1.

Time Complexity:
O(n + m)

Space Complexity:
O(n)

Pattern:
Monotonic Stack
"""

class Solution:
    def nextGreaterElement(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[int]:

        stack = []
        mp = {}

        for x in nums2:

            while stack and x > stack[-1]:
                mp[stack.pop()] = x

            stack.append(x)

        while stack:
            mp[stack.pop()] = -1

        ans = []

        for x in nums1:
            ans.append(mp[x])

        return ans
