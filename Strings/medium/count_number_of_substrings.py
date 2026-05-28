"""
Problem:
Number of Substrings Containing All Three Characters

Source:
LeetCode

Link:
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

Approach:
Use Sliding Window.

Expand the window using right pointer.
Maintain count of characters.

Whenever window contains at least
one 'a', 'b', and 'c':

All substrings starting from left
and ending from right to end
are valid.

Add:
n - right

Then shrink window from left.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Sliding Window
"""

from collections import defaultdict

def number_of_substrings(s):

    count = defaultdict(int)

    left = 0
    ans = 0
    n = len(s)

    for right in range(n):

        count[s[right]] += 1

        while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:

            ans += n - right

            count[s[left]] -= 1
            left += 1

    return ans
