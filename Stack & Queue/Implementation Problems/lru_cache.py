"""
Problem:
LRU Cache

Source:
LeetCode

Link:
https://leetcode.com/problems/lru-cache/

Approach:
Use a HashMap and a Doubly
Linked List.

The HashMap provides O(1)
access to cache nodes.

The Doubly Linked List keeps
track of usage order.

The most recently used node is
placed immediately after the
head.

The least recently used node is
placed just before the tail.

On every get() or existing put(),
move the accessed node to the
front.

If the cache reaches capacity,
remove the node before the tail.

Time Complexity:
get()  : O(1)
put()  : O(1)

Space Complexity:
O(capacity)

Pattern:
HashMap + Doubly Linked List
"""

class Node:

    def __init__(self, key, value):

        self.key = key
        self.val = value

        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity

        self.hashMap = {}

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:

        if key not in self.hashMap:
            return -1

        node = self.hashMap[key]

        self.deleteLL(node)
        self.insertAfterHead(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.hashMap:

            node = self.hashMap[key]

            node.val = value

            self.deleteLL(node)
            self.insertAfterHead(node)

        else:

            if len(self.hashMap) == self.capacity:

                lru = self.tail.prev

                self.deleteLL(lru)

                del self.hashMap[lru.key]

            node = Node(key, value)

            self.hashMap[key] = node

            self.insertAfterHead(node)

    def deleteLL(self, node):

        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insertAfterHead(self, node):

        nextNode = self.head.next

        node.next = nextNode
        node.prev = self.head

        self.head.next = node
        nextNode.prev = node
