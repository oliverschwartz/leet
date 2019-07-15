# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return True
        
        val = root.val
        stack = [root]
        while stack:
            v = stack.pop()
            if v.val != val: return False
            if v.right: stack.append(v.right)
            if v.left: stack.append(v.left)
        return True