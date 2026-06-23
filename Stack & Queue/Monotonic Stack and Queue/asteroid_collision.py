"""
Problem:
Asteroid Collision

Source:
LeetCode

Link:
https://leetcode.com/problems/asteroid-collision/

Approach:
Use a stack to maintain the
surviving asteroids.

A collision occurs only when:

stack top > 0
current asteroid < 0

Compare their absolute sizes.

Smaller asteroid explodes.

If both have equal size,
both explode.

Continue until the current
asteroid is destroyed or can
be safely added to the stack.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Stack Simulation
"""

class Solution:

    def asteroidCollision(
        self,
        asteroids: List[int]
    ) -> List[int]:

        stack = []

        for ast in asteroids:

            while (
                stack and
                stack[-1] > 0 and
                ast < 0
            ):

                if stack[-1] < -ast:
                    stack.pop()
                    continue

                elif stack[-1] == -ast:
                    stack.pop()

                break

            else:
                stack.append(ast)

        return stack
