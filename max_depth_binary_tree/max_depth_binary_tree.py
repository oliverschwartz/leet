# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        return self.traverse(root, 0)
        
    def traverse(self, root, best):
        if not root: 
            return best
        
        return max(self.traverse(root.left, best + 1),
                   self.traverse(root.right, best + 1))
        