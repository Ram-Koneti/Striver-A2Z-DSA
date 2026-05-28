"""
Problem:
Longest Palindromic Substring

Source:
LeetCode

Link:
https://leetcode.com/problems/longest-palindromic-substring/

Approach:
Use Expand Around Center technique.

For every index:
- Expand for odd length palindrome
- Expand for even length palindrome

Keep track of the longest palindrome found.

Time Complexity:
O(n^2)

Space Complexity:
O(1)

Pattern:
Two Pointers / Expand Around Center
"""

def longest_palindrome(s):

    start = 0
    end = 0

    def expand(left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]:

            left -= 1
            right += 1

        return right - left - 1

    for i in range(len(s)):

        # Odd length palindrome
        len1 = expand(i, i)

        # Even length palindrome
        len2 = expand(i, i + 1)

        max_len = max(len1, len2)

        if max_len > end - start:

            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]
