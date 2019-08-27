# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        stack.append(root)
        
        while stack:
            curr = stack.pop()
            if curr is p or curr is q:
                return curr

            if curr.val < p.val and curr.val > q.val:
                return curr
            elif curr.val > p.val and curr.val < q.val:
                return curr
            elif curr.val > p.val and curr.val > q.val:
                stack.append(curr.left)
            else:
                stack.append(curr.right)
        
        # Should not reach this line
        return None
