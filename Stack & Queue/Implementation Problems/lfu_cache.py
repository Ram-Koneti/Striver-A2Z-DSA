"""
Problem:
LFU Cache

Source:
LeetCode

Link:
https://leetcode.com/problems/lfu-cache/

Approach:
Use two hash maps and multiple
Doubly Linked Lists.

key_map:
Maps a key to its node for
O(1) access.

freq_map:
Maps a frequency to a Doubly
Linked List containing all
nodes with that frequency.

Each node stores:

key
value
frequency

When a node is accessed, increase
its frequency and move it to the
corresponding frequency list.

Maintain the minimum frequency
(min_freq).

When the cache is full, remove the
Least Recently Used node from the
minimum frequency list.

Time Complexity:
get() : O(1)

put() : O(1)

Space Complexity:
O(capacity)

Pattern:
HashMap + Frequency Lists
"""

class Node:

    def __init__(self, key=-1, value=-1):

        self.key = key
        self.val = value

        self.prev = None
        self.next = None

        self.freq = 1


class DLL:

    def __init__(self):

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self._size = 0

    def __len__(self):
        return self._size

    def remove(self, node):

        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

        self._size -= 1

    def remove_tail(self):

        if self._size == 0:
            return None

        node = self.tail.prev

        self.remove(node)

        return node

    def insertAfterHead(self, node):

        nextNode = self.head.next

        node.next = nextNode
        node.prev = self.head

        self.head.next = node
        nextNode.prev = node

        self._size += 1


class LFUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity

        self.key_map = {}

        self.freq_map = {}

        self.min_freq = 0

    def get(self, key: int) -> int:

        if key not in self.key_map:
            return -1

        node = self.key_map[key]

        self.update_freq(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        if key in self.key_map:

            node = self.key_map[key]

            node.val = value

            self.update_freq(node)

            return

        if len(self.key_map) == self.capacity:

            dll = self.freq_map[self.min_freq]

            node = dll.remove_tail()

            del self.key_map[node.key]

        node = Node(key, value)

        self.key_map[key] = node

        self.min_freq = 1

        if 1 not in self.freq_map:
            self.freq_map[1] = DLL()

        self.freq_map[1].insertAfterHead(node)

    def update_freq(self, node):

        oldFreq = node.freq

        self.freq_map[oldFreq].remove(node)

        if (
            oldFreq == self.min_freq and
            len(self.freq_map[oldFreq]) == 0
        ):
            self.min_freq += 1

        node.freq += 1

        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DLL()

        self.freq_map[node.freq].insertAfterHead(node)
