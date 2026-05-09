"""
Problem:
Count Inversions

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

Approach:
Use Merge Sort.
During merging, if left element > right element,
then all remaining elements in left half form inversions.

Time Complexity:
O(n log n)

Space Complexity:
O(n)

Pattern:
Merge Sort
"""

def inversion_count(arr):

    def merge_sort(low, high):
        if low >= high:
            return 0

        mid = (low + high) // 2

        count = merge_sort(low, mid)
        count += merge_sort(mid + 1, high)
        count += merge(low, mid, high)

        return count

    def merge(low, mid, high):
        temp = []
        left = low
        right = mid + 1
        count = 0

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                count += (mid - left + 1)
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        return count

    return merge_sort(0, len(arr) - 1)
