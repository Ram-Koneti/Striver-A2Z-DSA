"""
Problem:
K-th Element of Two Arrays

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

Approach:
Use binary search on the smaller array.
Partition both arrays such that:
total elements on left side = k.

The kth element will be:
max(left1, left2)

Time Complexity:
O(log(min(n, m)))

Space Complexity:
O(1)

Pattern:
Binary Search on Partition
"""

def kth_element(a, b, k):

    # Ensure a is smaller
    if len(a) > len(b):
        a, b = b, a

    n = len(a)
    m = len(b)

    low = max(0, k - m)
    high = min(k, n)

    while low <= high:

        cut1 = (low + high) // 2
        cut2 = k - cut1

        left1 = float('-inf') if cut1 == 0 else a[cut1 - 1]
        left2 = float('-inf') if cut2 == 0 else b[cut2 - 1]

        right1 = float('inf') if cut1 == n else a[cut1]
        right2 = float('inf') if cut2 == m else b[cut2]

        # Correct partition
        if left1 <= right2 and left2 <= right1:
            return max(left1, left2)

        elif left1 > right2:
            high = cut1 - 1
        else:
            low = cut1 + 1
