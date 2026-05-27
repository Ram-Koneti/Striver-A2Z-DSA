"""
Problem:
Sort Characters By Frequency

Source:
LeetCode

Link:
https://leetcode.com/problems/sort-characters-by-frequency/

Approach:
Count frequency of each character
using hashmap.

Sort characters based on frequency
in descending order.

Build the answer by repeating
each character according to its count.

Time Complexity:
O(n log n)

Space Complexity:
O(n)

Pattern:
Hashing / Sorting
"""

from collections import Counter

def frequency_sort(s):

    freq = Counter(s)

    ans = []

    for ch, count in sorted(freq.items(),
                            key=lambda x: x[1],
                            reverse=True):

        ans.append(ch * count)

    return "".join(ans)
  
