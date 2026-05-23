"""
Problem:
Aggressive Cows

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/aggressive-cows/1

Approach:
Use binary search on minimum distance.
For each distance, check if it is possible
to place all cows in stalls maintaining that distance.

Time Complexity:
O(n log(max(stalls)))

Space Complexity:
O(1)

Pattern:
Binary Search on Answer
"""

def aggressive_cows(stalls, k):

    stalls.sort()

    def can_place(distance):
        cows = 1
        last_position = stalls[0]

        for i in range(1, len(stalls)):

            if stalls[i] - last_position >= distance:
                cows += 1
                last_position = stalls[i]

            if cows >= k:
                return True

        return False

    low = 1
    high = stalls[-1] - stalls[0]
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        if can_place(mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer
