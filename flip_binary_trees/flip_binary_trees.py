# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def safeChildrenVals(node):
            return (node.left.val if node.left else None, node.right.val if node.right else None)
        
        # define it recursively - check roots of subtrees are equal or swapped,
        # and then recurse
        def recurseFlipEquiv(root1, root2):
            
            # base condition
            if root1 is None or root2 is None: return root1 == root2
            
            root1_left, root1_right = safeChildrenVals(root1)
            root2_left, root2_right = safeChildrenVals(root2)
           
            
            # recurse, not reversed
            if root1_left == root2_left and root1_right == root2_right:
                return recurseFlipEquiv(root1.right, root2.right) and recurseFlipEquiv(root1.left, root2.left)
            
            # recurse, reversed
            elif (root1_left == root2_right and root1_right == root2_left):
                return recurseFlipEquiv(root1.left, root2.right) and recurseFlipEquiv(root1.right, root2.left)
            
            # failure condition
            else: return False
            
        return recurseFlipEquiv(root1, root2)