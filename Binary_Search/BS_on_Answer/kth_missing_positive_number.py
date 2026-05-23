"""
Problem:
Kth Missing Positive Number

Source:
LeetCode

Link:
https://leetcode.com/problems/kth-missing-positive-number/

Approach:
Use binary search.
Missing numbers before index mid:
arr[mid] - (mid + 1)

Find the first position where missing count >= k.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Pattern:
Binary Search on Answer
"""

def find_kth_positive(arr, k):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        missing = arr[mid] - (mid + 1)

        if missing < k:
            low = mid + 1
        else:
            high = mid - 1

    return low + k
