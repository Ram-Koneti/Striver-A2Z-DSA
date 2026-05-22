"""
Problem:
Sqrt(x)

Source:
LeetCode

Link:
https://leetcode.com/problems/sqrtx/

Approach:
Use binary search to find the integer square root.
Store possible answer whenever mid * mid <= x.

Time Complexity:
O(log x)

Space Complexity:
O(1)

Pattern:
Binary Search on Answer
"""

def my_sqrt(x):
    low = 0
    high = x
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * mid <= x:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer
