"""
Problem:
Number of Greater Elements to the Right

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/number-of-greater-elements-to-the-right/1

Approach:
Use a modified merge sort.

Store each element along with
its original index.

During merging, whenever an
element from the left half is
smaller than an element from
the right half, all remaining
elements in the right half are
greater than it.

Add that count to the answer
for the left element's index.

After preprocessing, answer
each query in O(1).

Time Complexity:
O(n log n)

Space Complexity:
O(n)

Pattern:
Merge Sort Counting
"""

class Solution:

    def count_NGE(self, arr, indices):

        n = len(arr)

        cnt = [0] * n

        nums = [(arr[i], i) for i in range(n)]

        self.mergeSort(nums, 0, n - 1, cnt)

        return [cnt[i] for i in indices]

    def mergeSort(self, arr, low, high, cnt):

        if low >= high:
            return

        mid = (low + high) // 2

        self.mergeSort(arr, low, mid, cnt)
        self.mergeSort(arr, mid + 1, high, cnt)

        self.merge(arr, low, mid, high, cnt)

    def merge(self, arr, low, mid, high, cnt):

        temp = []

        left = low
        right = mid + 1

        while left <= mid and right <= high:

            if arr[left][0] < arr[right][0]:

                cnt[arr[left][1]] += (
                    high - right + 1
                )

                temp.append(arr[left])
                left += 1

            else:

                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]
