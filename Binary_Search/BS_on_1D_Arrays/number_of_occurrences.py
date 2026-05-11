"""
Problem:
Number of Occurrence

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1

Approach:
Use binary search twice.
Find the first occurrence of target.
Find the last occurrence of target.

Number of occurrences =
(last occurrence - first occurrence + 1)

If target is not found return 0.

Time Complexity:
O(log n)

Space Complexity:
O(1)

Pattern:
Binary Search
"""

def count_occurrences(arr, target):

    def first_occurrence():
        low = 0
        high = len(arr) - 1
        first = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                first = mid
                high = mid - 1

            elif arr[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return first

    def last_occurrence():
        low = 0
        high = len(arr) - 1
        last = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                last = mid
                low = mid + 1

            elif arr[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return last

    first = first_occurrence()

    if first == -1:
        return 0

    last = last_occurrence()

    return last - first + 1
