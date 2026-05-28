"""
Problem:
Sum of Beauty of All Substrings

Source:
LeetCode

Link:
https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

Approach:
Generate all substrings using
starting index.

Maintain frequency array while
expanding the substring.

For every substring:
- Find maximum frequency
- Find minimum non-zero frequency
- Add their difference to answer

Time Complexity:
O(n^2 * 26)

Space Complexity:
O(26)

Pattern:
String / Frequency Count
"""

def beauty_sum(s):

    ans = 0
    n = len(s)

    for i in range(n):

        freq = [0] * 26

        for j in range(i, n):

            idx = ord(s[j]) - ord('a')
            freq[idx] += 1

            maxi = max(freq)

            mini = float('inf')

            for count in freq:

                if count > 0:
                    mini = min(mini, count)

            ans += maxi - mini

    return ans
