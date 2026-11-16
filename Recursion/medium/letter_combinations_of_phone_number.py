"""
Problem:
17. Letter Combinations of a Phone Number

Source:
LeetCode

Link:
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Approach:
Use backtracking to generate all possible letter combinations.

Each digit maps to a set of letters using a hashmap.

For every digit:
1. Get all letters mapped to the current digit.
2. Try each letter by adding it to the current string.
3. Recursively process the next digit.

Base Case:
When the length of curr equals the length of digits,
add the combination to the result.

If digits is empty, return an empty list.

Time Complexity:
O(4^n * n), where n is the length of digits.
Each digit can have at most 4 letters, and creating
each combination takes O(n) time.

Space Complexity:
O(n) for the recursion stack, excluding the output.

Pattern:
Backtracking / String Building
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(ind, curr):
            # Base case
            if len(curr) == len(digits):
                res.append(curr)
                return

            # Try every letter mapped to the current digit
            for ch in hashmap[digits[ind]]:
                backtrack(ind + 1, curr + ch)

        if digits:
            backtrack(0, "")

        return res
