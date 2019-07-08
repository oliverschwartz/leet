# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None: return TreeNode(val)
        
        n = root
        
        while True:
            print(n.val)
            if n.val < val: 
                if n.right != None: n = n.right
                else: 
                    n.right = TreeNode(val)
                    break
            else: 
                if n.left != None: n = n.left
                else: 
                    n.left = TreeNode(val)
                    break
        return root