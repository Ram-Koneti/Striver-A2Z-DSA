"""
Problem:
All Divisors of a Number

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1

Approach:
A divisor always appears
in pairs.

For every number i from
1 to sqrt(n):
- If i divides n, add i.
- Add the paired divisor
  n // i.

Avoid duplicate insertion
when i * i == n.

Finally sort the list to
return divisors in
ascending order.

Time Complexity:
O(sqrt(n) + d log d)

Space Complexity:
O(d)

where d is the number
of divisors.

Pattern:
Mathematical Optimization
"""

import math


class Solution:

    def getDivisors(self, n):

        lis = []

        for i in range(1, int(math.sqrt(n)) + 1):

            if n % i == 0:

                lis.append(i)

                if n // i != i:

                    lis.append(n // i)

        lis.sort()

        return lis
