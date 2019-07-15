# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        
        stack = [root]
        leaves = set()
        parents = {root: None}
        while stack:
            v = stack.pop()
            if v.left:
                parents[v.left] = v
                stack.append(v.left)
            if v.right:
                parents[v.right] = v
                stack.append(v.right)
            if not v.left and not v.right:
                leaves.add(v)
        
        
        total = 0
        for v in leaves:
            path = ''
            while v is not None:
                path += str(v.val)
                v = parents[v]
            total += int(path[::-1])
        return total