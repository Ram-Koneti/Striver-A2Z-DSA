"""
Problem:
Longest Common Prefix

Source:
LeetCode

Link:
https://leetcode.com/problems/longest-common-prefix/

Approach:
Take the first string as prefix.

Compare it with every other string.
Keep reducing the prefix until
it matches the beginning of
the current string.

If prefix becomes empty,
return "".

Time Complexity:
O(n * m)

n = number of strings
m = length of shortest prefix

Space Complexity:
O(1)

Pattern:
String Matching
"""

def longest_common_prefix(strs):

    prefix = strs[0]

    for word in strs[1:]:

        while not word.startswith(prefix):

            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix
