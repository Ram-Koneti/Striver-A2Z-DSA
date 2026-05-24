"""
Problem:
Median of Two Sorted Arrays

Source:
LeetCode

Link:
https://leetcode.com/problems/median-of-two-sorted-arrays/

Approach:
Use binary search on the smaller array.
Partition both arrays such that:
left half elements <= right half elements.

Median depends on:
- total length even or odd

Time Complexity:
O(log(min(m, n)))

Space Complexity:
O(1)

Pattern:
Binary Search on Partition
"""

def find_median_sorted_arrays(nums1, nums2):

    # Ensure nums1 is smaller
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m = len(nums1)
    n = len(nums2)

    low = 0
    high = m

    while low <= high:

        cut1 = (low + high) // 2
        cut2 = (m + n + 1) // 2 - cut1

        left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
        left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]

        right1 = float('inf') if cut1 == m else nums1[cut1]
        right2 = float('inf') if cut2 == n else nums2[cut2]

        # Correct partition
        if left1 <= right2 and left2 <= right1:

            # Even length
            if (m + n) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2

            # Odd length
            return max(left1, left2)

        elif left1 > right2:
            high = cut1 - 1
        else:
            low = cut1 + 1
