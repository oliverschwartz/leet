# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        def recursePath(node, target):
            if not node:
                return False
            if node.val == target and not node.right and not node.left:
                return True
            else:
                return (
                    recursePath(node.left, target - node.val) or
                    recursePath(node.right, target - node.val)
                )
        return recursePath(root, sum)