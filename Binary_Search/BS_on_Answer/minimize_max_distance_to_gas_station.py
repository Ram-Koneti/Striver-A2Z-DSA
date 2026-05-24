"""
Problem:
Minimize Max Distance to Gas Station

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1

Approach:
Use binary search on answer.
For every maximum distance d,
calculate how many gas stations are needed
to ensure every adjacent distance <= d.

If required stations <= k,
try smaller distance.

Find answer up to 6 decimal places.

Time Complexity:
O(n * log(range))

Space Complexity:
O(1)

Pattern:
Binary Search on Answer
"""

def minimize_max_distance(stations, k):

    def required_stations(distance):

        count = 0

        for i in range(1, len(stations)):

            gap = stations[i] - stations[i - 1]

            count += int(gap / distance)

            # Exact divisible case
            if gap % distance == 0:
                count -= 1

        return count

    low = 0
    high = stations[-1] - stations[0]

    # Precision for 6 decimal places
    while high - low > 1e-6:

        mid = (low + high) / 2

        if required_stations(mid) <= k:
            high = mid
        else:
            low = mid

    return round(high, 6)
