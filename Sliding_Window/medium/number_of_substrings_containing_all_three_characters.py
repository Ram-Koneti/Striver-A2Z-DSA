"""
Problem:
Number of Substrings Containing All Three Characters

Source:
LeetCode

Link:
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

Approach:
Track the latest index of
each character:

a
b
c

For every position,
update the latest index
of the current character.

If all three characters
have been seen, the
earliest of their latest
indices determines how
many valid substrings
end at the current
position.

Add:

minimum latest index + 1

to the answer.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Last Occurrence Tracking
"""

class Solution:

    def numberOfSubstrings(
        self,
        s: str
    ) -> int:

        lastIndex = [-1] * 3

        count = 0

        for i in range(len(s)):

            lastIndex[
                ord(s[i]) - ord("a")
            ] = i

            if (
                lastIndex[0] != -1 and
                lastIndex[1] != -1 and
                lastIndex[2] != -1
            ):

                count += min(lastIndex) + 1

        return count
