"""
Problem:
Missing And Repeating

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1

Approach:
Use mathematical formulas:
1. Difference between expected sum and actual sum
2. Difference between expected square sum and actual square sum
Solve equations to find missing and repeating numbers.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Math
"""

def find_missing_and_repeating(arr):
    n = len(arr)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)

    expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6
    actual_sq_sum = sum(num * num for num in arr)

    diff = expected_sum - actual_sum
    sq_diff = expected_sq_sum - actual_sq_sum

    sum_values = sq_diff // diff

    missing = (diff + sum_values) // 2
    repeating = missing - diff

    return [repeating, missing]
