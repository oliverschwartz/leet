"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        
        nodes = [root]
        while nodes:
            l = len(nodes)
            new_nodes = []
            for idx, v in enumerate(nodes):
                if idx == l - 1: v.next = None
                else: v.next = nodes[idx + 1]
                if v.left: new_nodes.append(v.left)
                if v.right: new_nodes.append(v.right)
            nodes = new_nodes
        return root