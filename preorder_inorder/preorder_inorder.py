# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def helper(preorder, inorder):
            if preorder == [] or inorder == []: return None
            root = TreeNode(preorder.pop(0))
            idx = inorder.index(root.val)
            root.left = helper(preorder, inorder[:idx])
            root.right = helper(preorder, inorder[idx + 1:])
            return root
        
        return helper(preorder, inorder)
            