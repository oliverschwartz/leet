# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        vals = []
        max_depth = -1
        stack = [(root, 0)]
        while stack:
            (v, depth) = stack.pop()
            if depth > max_depth:
                vals.append(v.val)
                max_depth = depth
            if v.left: stack.append((v.left, depth + 1))
            if v.right: stack.append((v.right, depth + 1))
        return vals