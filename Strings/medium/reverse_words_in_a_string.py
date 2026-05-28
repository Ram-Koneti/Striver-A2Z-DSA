"""
Problem:
Reverse Words in a String

Source:
LeetCode

Link:
https://leetcode.com/problems/reverse-words-in-a-string/

Approach:
Use split() to extract words.

split() automatically removes:
- leading spaces
- trailing spaces
- multiple spaces

Reverse the list of words
and join them using single spaces.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
String Manipulation
"""

def reverse_words(s):

    words = s.split()

    return " ".join(words[::-1])
