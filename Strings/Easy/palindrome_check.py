"""
Problem:
Reverse Words in a String

Source:
LeetCode

Link:
https://leetcode.com/problems/reverse-words-in-a-string/

Approach:
Split the string into words,
reverse the list of words,
then join them using single spaces.

split() automatically removes:
- leading spaces
- trailing spaces
- multiple spaces between words

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
String Manipulation
"""

def reverse_words(s):

    words = s.split()

    words.reverse()

    return " ".join(words)
