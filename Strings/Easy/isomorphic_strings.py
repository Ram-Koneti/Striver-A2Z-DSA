"""
Problem:
Isomorphic Strings

Source:
LeetCode

Link:
https://leetcode.com/problems/isomorphic-strings/

Approach:
Use two hashmaps to store
character mappings between
both strings.

Check:
- s character maps consistently to t
- t character maps consistently to s

If any mismatch occurs,
return False.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Hashing / String Mapping
"""

def is_isomorphic(s, t):

    map_st = {}
    map_ts = {}

    for ch1, ch2 in zip(s, t):

        if ch1 in map_st:

            if map_st[ch1] != ch2:
                return False

        else:
            map_st[ch1] = ch2

        if ch2 in map_ts:

            if map_ts[ch2] != ch1:
                return False

        else:
            map_ts[ch2] = ch1

    return True
