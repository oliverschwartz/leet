# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:

        # do DFS and also track a parents array
        parents = {root: None}
        stack = [root]
        leaves = set()
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
        
        paths = []
        min_s = None
        for v in leaves:
            update = True
            s = ''
            while v is not None:
                s += chr(ord('a') + v.val)
                v = parents[v]
                # break early if we can
                if min_s and s >= min_s:
                    update = False
                    break
            if update: min_s = s
        return min_s
        