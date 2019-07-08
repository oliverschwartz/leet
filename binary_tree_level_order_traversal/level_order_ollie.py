# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        q = queue.Queue()
        q.put(root)
        
        to_return = []
        
        while not q.empty():
            nodes = []
            vals = []
            
            # remove all items from the queue
            while not q.empty():
                node = q.get()
                nodes.append(node)
                vals.append(node.val)
                
            # for each node that was removed, enqueue its children
            for node in nodes:
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
            to_return.append(vals)
        return to_return
                