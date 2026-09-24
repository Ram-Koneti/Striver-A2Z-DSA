"""
Problem:
Quick Sort

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/quick-sort/1

Approach:
Use the divide and conquer technique with the first element
as the pivot.

Partition the array so that:
- Elements smaller than or equal to the pivot are moved to the left.
- Elements greater than or equal to the pivot are moved to the right.

After partitioning, the pivot is placed at its correct position.

Then recursively apply Quick Sort to:
- Left part: low to pivot_index - 1
- Right part: pivot_index + 1 to high

Time Complexity:
Average: O(n log n)
Worst: O(n^2)

Space Complexity:
O(log n) average due to the recursive call stack.
O(n) in the worst case.

Pattern:
Divide and Conquer / Partitioning
"""

class Solution:
    def quickSort(self, arr, low, high):

        def partition(low, high):

            pivot = arr[low]

            l = low + 1
            r = high

            while True:

                # Find element greater than pivot
                while l <= r and arr[l] <= pivot:
                    l += 1

                # Find element smaller than pivot
                while l <= r and arr[r] >= pivot:
                    r -= 1

                # Pointers crossed
                if l > r:
                    break

                # Swap misplaced elements
                arr[l], arr[r] = arr[r], arr[l]

            # Place pivot at its correct position
            arr[low], arr[r] = arr[r], arr[low]

            return r

        # Base case
        if low >= high:
            return

        # Partition the array
        pIndex = partition(low, high)

        # Sort left part
        self.quickSort(arr, low, pIndex - 1)

        # Sort right part
        self.quickSort(arr, pIndex + 1, high)
