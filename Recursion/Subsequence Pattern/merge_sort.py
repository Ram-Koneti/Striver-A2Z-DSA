"""
Problem:
Merge Sort

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/merge-sort/1

Approach:
Use the divide and conquer technique.

1. Divide the array into two halves.
2. Recursively sort the left half.
3. Recursively sort the right half.
4. Merge the two sorted halves into one sorted section.

The merge function uses two pointers:
- low points to the left half.
- high points to the right half.

Compare both elements and place the smaller one into
the temporary array. After one half is exhausted, add
the remaining elements from the other half.

Finally, copy the sorted temporary array back into arr.

Time Complexity:
O(n log n)

Space Complexity:
O(n) for the temporary array, plus O(log n) recursion stack.

Pattern:
Divide and Conquer / Merge Sort
"""

class Solution:
    def mergeSort(self, arr, l, r):

        def merge(l, mid, r):

            temp = []

            low = l
            high = mid + 1

            # Compare elements from both sorted halves
            while low <= mid and high <= r:

                if arr[low] <= arr[high]:
                    temp.append(arr[low])
                    low += 1
                else:
                    temp.append(arr[high])
                    high += 1

            # Add remaining elements from left half
            while low <= mid:
                temp.append(arr[low])
                low += 1

            # Add remaining elements from right half
            while high <= r:
                temp.append(arr[high])
                high += 1

            # Copy sorted elements back into arr
            for i in range(l, r + 1):
                arr[i] = temp[i - l]

        # Base case
        if l >= r:
            return

        mid = (l + r) // 2

        # Sort left half
        self.mergeSort(arr, l, mid)

        # Sort right half
        self.mergeSort(arr, mid + 1, r)

        # Merge both sorted halves
        merge(l, mid, r)
