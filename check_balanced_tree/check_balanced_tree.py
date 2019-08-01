# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        
        class UnbalancedException(Exception):
            pass
        
        def recurseIsBalanced(node):
            
            if not node:
                return 0
            
            else:
                h1 = recurseIsBalanced(node.left)
                h2 = recurseIsBalanced(node.right)
                
                if abs(h1 - h2) > 1:
                    raise UnbalancedException
                
                else:
                    return 1 + max(h1, h2)
                
        try:
            recurseIsBalanced(root)
        except UnbalancedException:
            return False
        
        return True
        