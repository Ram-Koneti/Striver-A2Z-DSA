"""
Problem:
Count Subarrays with Given XOR

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1

Approach:
Use prefix XOR and hashmap.
If (current_xor ^ k) exists in hashmap,
then a subarray with XOR k is found.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Prefix XOR + HashMap
"""

def count_subarrays_with_xor(arr, k):
    xor = 0
    count = 0
    xor_map = {0: 1}

    for num in arr:
        xor ^= num

        required = xor ^ k

        if required in xor_map:
            count += xor_map[required]

        xor_map[xor] = xor_map.get(xor, 0) + 1

    return count
