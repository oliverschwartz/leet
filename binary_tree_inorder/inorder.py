# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None: return [] # corner case
        order = []
        return self.traverse(root, order)
    
    def traverse(self, root, order):
        if root.left != None: self.traverse(root.left, order)
        order.append(root.val)
        if root.right != None: self.traverse(root.right, order)
        return order