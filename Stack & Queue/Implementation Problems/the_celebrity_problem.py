"""
Problem:
The Celebrity Problem

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/the-celebrity-problem/1

Approach:
Use two pointers to eliminate
non-celebrities.

If person A knows person B,
A cannot be the celebrity.

Otherwise, B cannot be the
celebrity.

After elimination, only one
candidate remains.

Verify the candidate by checking:

1. Candidate knows nobody.
2. Everyone knows the candidate.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Two Pointers Elimination
"""

class Solution:

    def celebrity(self, mat):

        n = len(mat)

        top = 0
        down = n - 1

        while top < down:

            if mat[top][down] == 1:
                top += 1

            elif mat[down][top] == 1:
                down -= 1

            else:
                top += 1
                down -= 1

        candidate = top

        for i in range(n):

            if i == candidate:
                continue

            if (
                mat[candidate][i] == 1 or
                mat[i][candidate] == 0
            ):
                return -1

        return candidate
