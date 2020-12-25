"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def clone_nodes(node):
            while node:
                clone_node = Node(node.val, node.next, None)
                node.next = clone_node
                node = clone_node.next
        def connect_sibling_nodes(node):
            while node:
                clone_node = node.next
                if node.random:
                    clone_node.random = node.random.next
                node = clone_node.next
        def reconnect_nodes(node):
            clone_head = None
            if node:
                original_head = node
                clone_head = node.next
                clone_node = node.next
                node.next = clone_node.next
                node = node.next
            while node:
                clone_node.next = node.next
                clone_node = clone_node.next
                node.next = clone_node.next
                node = node.next
            return clone_head
        clone_nodes(head)
        connect_sibling_nodes(head)