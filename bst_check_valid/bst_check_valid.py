# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None: return True
        return self.isValid(root, 99999999999999999, -999999999999999999)
        
    def isValid(self, root, ma, mi):
        if root == None: return True
        if root.val <= mi or root.val >= ma: return False
        return (self.isValid(root.left, root.val, mi) 
            and self.isValid(root.right, ma, root.val))

        