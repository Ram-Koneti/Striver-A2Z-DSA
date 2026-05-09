"""
Problem:
Merge Sorted Array

Source:
LeetCode

Link:
https://leetcode.com/problems/merge-sorted-array/

Approach:
Use three pointers starting from the end.
Place the larger element at the last position of nums1.

Time Complexity:
O(m + n)

Space Complexity:
O(1)

Pattern:
Two Pointer
"""

def merge_sorted_array(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1

        p -= 1

    # copy remaining elements from nums2
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

    return nums1
