# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root: return None
        
        self.heights = {}
        def treeHeight(node):
            if node in self.heights:
                return self.heights[node]
            if not node:
                return 0
            else:
                h = max(1 + treeHeight(node.left), 1 + treeHeight(node.right))
                self.heights[node] = h
                return h
            
        def recurseDeepest(node):
            l, r = treeHeight(node.left), treeHeight(node.right)
            if l == r:
                return node
            else:
                return recurseDeepest(node.left if l > r else node.right)
            
        return recurseDeepest(root)