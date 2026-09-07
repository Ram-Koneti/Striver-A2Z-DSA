"""
Problem:
Reverse a Stack

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/reverse-a-stack/1

Approach:
Use recursion to reverse the stack without using an extra stack.

The reverseStack function removes the top element and recursively
reverses the remaining stack.

After the remaining stack is reversed, insert the removed element
at the bottom using the insert function.

The insert function:
- If the stack is empty, insert the element.
- Otherwise, remove the top element.
- Recursively insert the element at the bottom.
- Restore the removed element.

Time Complexity:
O(n^2)

Space Complexity:
O(n) due to the recursive call stack.

Pattern:
Recursion / Insert at Bottom
"""

class Solution:

    def reverseStack(self, st):

        # Base case
        if not st:
            return

        top = st.pop()

        # Recursively reverse the remaining stack
        self.reverseStack(st)

        # Insert the removed element at the bottom
        self.insert(st, top)

    def insert(self, st, ele):

        # Base case
        if not st:
            st.append(ele)
            return

        top = st.pop()

        # Recursively reach the bottom
        self.insert(st, ele)

        # Restore the removed element
        st.append(top)
