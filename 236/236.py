# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is p or root is q:
            return root
        
        p_left, q_left = dfs(root.left, p, q)
        
        if p_left and q_left:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_left != q_left:
            return root
        else: 
            return self.lowestCommonAncestor(root.right, p, q)

memo = {}
def dfs(node, p, q):
    return dfsHelper(node, p), dfsHelper(node, q)

def dfsHelper(node, target):
    if not node:
        return False
    elif node is target:
        return True
    else:
        if (node, target) not in memo:
            memo[(node, target)] = dfsHelper(node.left, target) or dfsHelper(node.right, target)
        return memo[(node, target)]
