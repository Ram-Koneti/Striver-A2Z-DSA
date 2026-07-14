"""
Problem:
Longest Substring Without Repeating Characters

Source:
LeetCode

Link:
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Approach:
Use Sliding Window with
HashMap.

Maintain two pointers:

left
right

The hash map stores the
last index of every
character.

If the current character
already exists inside the
current window, move the
left pointer to one
position after its last
occurrence.

Update the maximum window
length at every step.

Time Complexity:
O(n)

Space Complexity:
O(min(n, charset))

Pattern:
Sliding Window + HashMap
"""

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        hashMap = {}

        left = 0
        maxLen = 0

        for right in range(n):

            if (
                s[right] in hashMap and
                hashMap[s[right]] >= left
            ):
                left = hashMap[s[right]] + 1

            maxLen = max(
                maxLen,
                right - left + 1
            )

            hashMap[s[right]] = right

        return maxLen
