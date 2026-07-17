"""
Problem:
Longest Substring with K Uniques

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

Approach:
Use Sliding Window with
HashMap.

Maintain two pointers:

left
right

The hash map stores the
frequency of characters
inside the current
window.

Expand the window by
moving the right pointer.

If the number of unique
characters exceeds k,
shrink the window from
the left until it
becomes valid.

Whenever the window
contains exactly k unique
characters, update the
maximum length.

Time Complexity:
O(n)

Space Complexity:
O(k)

Pattern:
Sliding Window + HashMap
"""

class Solution:

    def longestKSubstr(
        self,
        s,
        k
    ):

        left = 0
        maxLen = -1

        hashMap = {}

        for right in range(len(s)):

            hashMap[s[right]] = (
                hashMap.get(s[right], 0) + 1
            )

            while len(hashMap) > k:

                hashMap[s[left]] -= 1

                if hashMap[s[left]] == 0:
                    del hashMap[s[left]]

                left += 1

            if len(hashMap) == k:

                maxLen = max(
                    maxLen,
                    right - left + 1
                )

        return maxLen
