# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        p_depth, q_depth = None, None
        stack = [(root, 0)]
        parents = {root: None}
        while p_depth is None or q_depth is None:
            v, h = stack.pop()
            if v.val == p.val:
                p_depth = h
            if v.val == q.val:
                q_depth = h
            if v.left:
                parents[v.left] = v
                stack.append((v.left, h + 1))
            if v.right:
                parents[v.right] = v
                stack.append((v.right, h + 1))
                
        p_ancestor = p
        q_ancestor = q

        
        while p_ancestor != q_ancestor:
            if p_depth > q_depth:
                p_depth -= 1
                p_ancestor = parents[p_ancestor]
            elif q_depth > p_depth:
                q_depth -= 1
                q_ancestor = parents[q_ancestor]
            else:
                p_depth -= 1
                q_depth -= 1
                p_ancestor = parents[p_ancestor]
                q_ancestor = parents[q_ancestor]
    
        return p_ancestor
        
                
        