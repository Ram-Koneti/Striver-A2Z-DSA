"""
Problem:
Reverse Pairs

Source:
LeetCode

Link:
https://leetcode.com/problems/reverse-pairs/

Approach:
Use Merge Sort.
Before merging two sorted halves,
count pairs where arr[i] > 2 * arr[j].

Time Complexity:
O(n log n)

Space Complexity:
O(n)

Pattern:
Merge Sort
"""

def reverse_pairs(nums):

    def merge_sort(low, high):
        if low >= high:
            return 0

        mid = (low + high) // 2

        count = merge_sort(low, mid)
        count += merge_sort(mid + 1, high)
        count += count_pairs(low, mid, high)
        merge(low, mid, high)

        return count

    def count_pairs(low, mid, high):
        count = 0
        right = mid + 1

        for i in range(low, mid + 1):
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1

            count += right - (mid + 1)

        return count

    def merge(low, mid, high):
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1

        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(low, high + 1):
            nums[i] = temp[i - low]

    return merge_sort(0, len(nums) - 1)
