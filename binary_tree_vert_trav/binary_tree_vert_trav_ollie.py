# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # if root is None
        if not root: return []
        
        # traverse the tree in level-order
        nodes = self.levelOrder(root, 0, 0, {})
        
        a = []
        for x in sorted(nodes.keys()):
            nodes[x].sort(key = lambda tup: (-tup[0], tup[1]))
            a.append([t[1] for t in nodes[x]])
            
        return a
        
        
    def levelOrder(self, root, x, y, nodes):
        if not root: return
        
        if not nodes.__contains__(x):
            nodes[x] = [(y, root.val)]
        else: nodes[x].append((y, root.val))
            
        if root.left: self.levelOrder(root.left, x - 1, y - 1, nodes)
        if root.right: self.levelOrder(root.right, x + 1, y - 1, nodes)
        return nodes
        