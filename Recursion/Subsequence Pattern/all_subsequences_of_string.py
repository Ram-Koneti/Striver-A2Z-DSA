"""
Problem:
All Subsequences of String

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/power-set4302/1

Approach:
Use recursion with the include-exclude pattern.

For every character, we have two choices:
1. Include the current character.
2. Exclude the current character.

When the index reaches the end of the string,
add the current subsequence to the result.

Finally, sort the result to return all subsequences
in lexicographical order.

The empty string is also included because the recursion
starts with an empty subsequence.

Time Complexity:
O(n * 2^n)

Space Complexity:
O(n) for the recursion stack,
excluding the output.

Pattern:
Recursion / Backtracking / Include-Exclude
"""

class Solution:
    def powerSet(self, s):

        n = len(s)
        res = []

        def dfs(ind, curr):

            # Base case
            if ind >= n:
                res.append(curr)
                return

            # Include current character
            dfs(ind + 1, curr + s[ind])

            # Exclude current character
            dfs(ind + 1, curr)

        dfs(0, "")

        return sorted(res)
