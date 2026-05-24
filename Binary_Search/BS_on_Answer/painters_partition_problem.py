"""
Problem:
Painter's Partition Problem II

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1

Approach:
Use binary search on answer.
For each maximum time, check if all boards
can be painted using at most k painters.
Each painter paints contiguous boards only.

Time Complexity:
O(n log(sum(arr)))

Space Complexity:
O(1)

Pattern:
Binary Search on Answer
"""

def painters_partition(arr, k):

    def count_painters(max_time):

        painters = 1
        current_time = 0

        for board in arr:

            if current_time + board <= max_time:
                current_time += board
            else:
                painters += 1
                current_time = board

        return painters

    low = max(arr)
    high = sum(arr)
    answer = high

    while low <= high:

        mid = (low + high) // 2

        if count_painters(mid) <= k:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer
