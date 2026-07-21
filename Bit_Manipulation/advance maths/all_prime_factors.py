"""
Problem:
All Prime Factors in Any Order

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/all-prime-factors-of-a-number/1

Approach:
Use trial division to find
all prime factors.

Start checking from 2.

For every number i:
- While i divides n, add i
  to the answer.
- Reduce n by dividing it
  with i.

After the loop, if n is
greater than 1, it means
n itself is a remaining
prime factor.

Time Complexity:
O(sqrt(n))

Space Complexity:
O(number of prime factors)

Pattern:
Prime Factorization
"""

class Solution:

    def primeFactors(self, n):

        i = 2

        ans = []

        while i * i <= n:

            while n % i == 0:

                ans.append(i)

                n //= i

            i += 1

        if n > 1:

            ans.append(n)

        return ans
