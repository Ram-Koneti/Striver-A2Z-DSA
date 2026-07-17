"""
Problem:
Minimum Window Substring

Source:
LeetCode

Link:
https://leetcode.com/problems/minimum-window-substring/

Approach:
Use Sliding Window with
HashMap.

Store the frequency of
each character in the
target string.

Maintain two pointers:

left
right

Expand the window by
moving the right pointer.

Decrease the required
frequency for each
character encountered.

When all characters of
the target are included,
shrink the window from
the left while it remains
valid.

Keep track of the
smallest valid window.

Time Complexity:
O(n + m)

Space Complexity:
O(m)

Pattern:
Sliding Window + HashMap
"""

class Solution:

    def minWindow(
        self,
        s: str,
        t: str
    ) -> str:

        if len(t) > len(s):
            return ""

        hashMap = {}

        for ch in t:
            hashMap[ch] = (
                hashMap.get(ch, 0) + 1
            )

        left = 0
        matched = 0

        minLen = float("inf")
        startIndex = -1

        for right in range(len(s)):

            if s[right] in hashMap:

                if hashMap[s[right]] > 0:
                    matched += 1

                hashMap[s[right]] -= 1

            while matched == len(t):

                if right - left + 1 < minLen:

                    minLen = right - left + 1
                    startIndex = left

                if s[left] in hashMap:

                    hashMap[s[left]] += 1

                    if hashMap[s[left]] > 0:
                        matched -= 1

                left += 1

        if startIndex == -1:
            return ""

        return s[
            startIndex:
            startIndex + minLen
        ]
