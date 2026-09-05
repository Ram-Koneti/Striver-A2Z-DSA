"""
Problem:
Sort a Stack

Source:
GeeksforGeeks

Link:
https://www.geeksforgeeks.org/problems/sort-a-stack/1

Approach:
Use recursion to sort the stack without using an extra stack.

The sort function removes the top element and recursively sorts
the remaining stack.

After the smaller stack is sorted, insert the removed element
back into its correct position using the insert function.

The insert function:
- If the stack is empty or its top element is <= ele,
  push ele.
- Otherwise, remove the top element, recursively insert ele,
  and then restore the removed element.

This produces a stack sorted in ascending order from bottom to top.

Time Complexity:
O(n^2)

Space Complexity:
O(n) due to the recursive call stack.

Pattern:
Recursion / Sorting by Insertion
"""

class Solution:
    def sortStack(self, st):

        def insert(st, ele):

            # Base case:
            # Empty stack or correct position found
            if not st or st[-1] <= ele:
                st.append(ele)
                return

            top = st.pop()

            # Recursively find the correct position
            insert(st, ele)

            # Restore the removed element
            st.append(top)

        def sort(st):

            # Base case
            if not st:
                return

            top = st.pop()

            # Recursively sort the remaining stack
            sort(st)

            # Insert the removed element in sorted position
            insert(st, top)

        sort(st)

        return st
