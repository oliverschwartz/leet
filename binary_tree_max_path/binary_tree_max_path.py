# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.global_max = -float('inf')
        def max_path(node):

            # recursive base case
            if not node: return 0

            # calculate children
            left = max_path(node.left)
            right = max_path(node.right)
            
            # we update the global max reflect ALL possible path choices
            self.global_max = max(
                self.global_max,
                node.val,
                node.val + left, 
                node.val + right, 
                node.val + left + right
            )
            
            # for the return value . for this given node, the max_path must
            # actually use the node
            # so we return the max of paths that use the node
            return max(node.val + left, node.val, node.val + right)

        max_path(root)
        return self.global_max

