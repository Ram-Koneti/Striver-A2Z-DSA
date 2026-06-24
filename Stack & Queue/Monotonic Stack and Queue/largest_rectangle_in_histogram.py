"""
Problem:
Largest Rectangle in Histogram

Source:
LeetCode

Link:
https://leetcode.com/problems/largest-rectangle-in-histogram/

Approach:
Use a monotonic increasing stack.

Whenever the current height is
smaller than the stack top,
the stack top becomes the
minimum height of a rectangle.

Compute:

height * width

where width is determined using
the Previous Smaller Element
and Next Smaller Element
boundaries.

Process all remaining bars
after traversal.

Time Complexity:
O(n)

Space Complexity:
O(n)

Pattern:
Monotonic Stack
"""
 #  optimal approah : one pass solution
                        # while doing PSE poping , simultaneoulsy do NSE
                        # apply area formulae

stack = []
n= len(heights)
maxArea = 0

for i in range(n):

    while stack and heights[i] < heights[stack[-1]]:
        element = stack[-1] 
        stack.pop()
        nse = i
        pse = stack[-1] if stack  else -1

        maxArea = max(maxArea , heights[element]*(nse - pse -1))
    stack.append(i)

while stack:
    element = stack[-1] 
    stack.pop()
    nse = n
    pse = stack[-1]  if stack else -1
    maxArea = max(maxArea , heights[element]*(nse - pse -1))

return maxArea
