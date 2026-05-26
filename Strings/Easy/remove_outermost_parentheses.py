"""
Problem:
Remove Outermost Parentheses

Source:
LeetCode

Link:
https://leetcode.com/problems/remove-outermost-parentheses/

Approach:
Use a counter to track balance of parentheses.

For every '(':
add it only if balance > 0

For every ')':
remove balance first,
then add it only if balance > 0

This skips the outermost parentheses
of every primitive valid string.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Stack / Parentheses Traversal
"""

def remove_outer_parentheses(s):

    ans = []
    count = 0

    for ch in s:

        # Opening bracket
        if ch == '(':

            if count > 0:
                ans.append(ch)

            count += 1

        # Closing bracket
        else:

            count -= 1

            if count > 0:
                ans.append(ch)

    return "".join(ans)
