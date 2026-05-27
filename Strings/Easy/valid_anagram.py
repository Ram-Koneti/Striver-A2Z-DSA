"""
Problem:
Valid Anagram

Source:
LeetCode

Link:
https://leetcode.com/problems/valid-anagram/

Approach:
Count frequency of characters
in both strings.

If frequency maps are equal,
both strings are anagrams.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Hashing / Frequency Count
"""

from collections import Counter

def is_anagram(s, t):

    return Counter(s) == Counter(t)
