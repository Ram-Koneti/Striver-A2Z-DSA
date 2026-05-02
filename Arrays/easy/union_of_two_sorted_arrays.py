"""
Problem:
Union of Two Sorted Arrays

Source:
Striver A2Z DSA Sheet

Link:
https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1

Approach:
Use two pointers to traverse both arrays.
Compare elements and add the smaller one to the result if it is not already added.
Skip duplicates by checking the last inserted element.

Time Complexity:
O(n + m)

Space Complexity:
O(n + m)

Pattern:
Two Pointer / Merge Technique
"""

def union_sorted_arrays(a, b):
    i, j = 0, 0
    union = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            if not union or union[-1] != a[i]:
                union.append(a[i])
            i += 1
        else:
            if not union or union[-1] != b[j]:
                union.append(b[j])
            j += 1

    # remaining elements of a
    while i < len(a):
        if not union or union[-1] != a[i]:
            union.append(a[i])
        i += 1

    # remaining elements of b
    while j < len(b):
        if not union or union[-1] != b[j]:
            union.append(b[j])
        j += 1

    return union
