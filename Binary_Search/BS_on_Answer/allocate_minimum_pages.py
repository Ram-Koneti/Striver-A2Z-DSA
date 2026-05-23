"""
Problem:
Allocate Minimum Pages

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

Approach:
Use binary search on maximum pages.
For each value, check if books can be allocated
to students such that no student gets more pages.

Time Complexity:
O(n log(sum(arr)))

Space Complexity:
O(1)

Pattern:
Binary Search on Answer
"""

def allocate_minimum_pages(arr, k):

    if k > len(arr):
        return -1

    def count_students(max_pages):
        students = 1
        pages = 0

        for book in arr:

            if pages + book <= max_pages:
                pages += book
            else:
                students += 1
                pages = book

        return students

    low = max(arr)
    high = sum(arr)
    answer = high

    while low <= high:
        mid = (low + high) // 2

        if count_students(mid) <= k:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer
