"""
Problem:
Rotate String

Source:
LeetCode

Link:
https://leetcode.com/problems/rotate-string/

Approach:
If lengths are different,
rotation is impossible.

Concatenate the string with itself.
If goal exists inside (s + s),
then goal can be formed by rotation.

Example:
s = "abcde"

s + s = "abcdeabcde"

goal = "cdeab" exists inside it.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
String Matching
"""

def rotate_string(s, goal):

    if len(s) != len(goal):
        return False

    return goal in (s + s)
