"""
Problem:
Reverse Nodes in k-Group

Source:
LeetCode

Link:
https://leetcode.com/problems/reverse-nodes-in-k-group/

Approach:
Process the linked list in groups of k nodes.

First check if k nodes are available.
If not, leave the remaining nodes as they are.

Reverse the current group of k nodes
and connect it with the previously
processed groups.

Repeat until the entire list is processed.

Time Complexity:
O(n)

Space Complexity:
O(1)

Pattern:
Linked List Reversal
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # empty or singl node
        if head is None  or head.next is None:
            return head
        
        temp = head
        prev = None
        while temp:

            kthNode = self.getkthNode(temp,k)

            if kthNode is None:
                if prev:
                    prev.next = temp
                break
            
            nextNode = kthNode.next  #storenext
            kthNode.next = None      #break link

            newHead = self.reverse(temp)  #reverse the k group

            # if first group 
            if temp == head: head = newHead

            else: prev.next = newHead
            
            prev = temp  #store prevnode to connect

            temp = nextNode  #move to next k group

        return head

    # to find the kth node
    def getkthNode(self, head, k):

        temp = head
        k -=1

        while temp and k>0:
            temp = temp.next
            k-=1
        
        return temp

   # to reverse the ll
    def reverse(self,head):

        prev = None
        curr = head

        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front

        return prev
