"""
Problem:
Array Leaders

Source:
Striver A2Z DSA Sheet

Link:
https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

Approach:
Traverse from right to left.
Keep track of the maximum element seen so far.
If current element >= max_so_far, it is a leader.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Reverse Traversal
"""

def find_leaders(arr):
    leaders = []
    max_so_far = float('-inf')

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] >= max_so_far:
            leaders.append(arr[i])
            max_so_far = arr[i]

    return leaders[::-1]
