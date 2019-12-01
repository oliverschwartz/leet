# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        traversal = []
        
        def preorder(node):
            if not node:
                return
            traversal.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        for i, node in enumerate(traversal):
            node.left = None
            if node == traversal[-1]:
                node.right = None
            else:
                node.right = traversal[i + 1]
    
