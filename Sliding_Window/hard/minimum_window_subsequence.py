"""
Problem:
Minimum Window Subsequence

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/minimum-window-subsequence/1

Approach:
Use Two Pointers with
Forward and Backward
Scanning.

Start from every possible
left index.

Perform a forward scan to
find a window containing
the entire subsequence.

If a valid window is
found, perform a backward
scan to minimize the
window while preserving
the subsequence order.

Update the minimum window
if a smaller one is
found.

Move the left pointer to
the next possible start
and repeat.

Time Complexity:
O(n * m)

Space Complexity:
O(1)

Pattern:
Two Pointers
"""

class Solution:

    def minWindow(
        self,
        s1,
        s2
    ):

        n = len(s1)
        m = len(s2)

        left = 0

        minLen = float("inf")
        startIndex = -1

        while left < n:

            right = left
            index = 0

            # Forward scan
            while (
                right < n and
                index < m
            ):

                if s1[right] == s2[index]:
                    index += 1

                right += 1

            if index < m:
                break

            end = right - 1

            # Backward scan
            index = m - 1
            right = end

            while index >= 0:

                if s1[right] == s2[index]:
                    index -= 1

                right -= 1

            start = right + 1

            if end - start + 1 < minLen:

                minLen = end - start + 1
                startIndex = start

            left = start + 1

        if startIndex == -1:
            return ""

        return s1[
            startIndex:
            startIndex + minLen
        ]
