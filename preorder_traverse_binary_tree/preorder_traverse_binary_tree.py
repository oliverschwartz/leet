# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        # we know that given an element as root, the smaller elements will be
        # in the left subtree, while the larger elements will be in the right subtree
        #
        # this lets us write this thing recursively
        #
        def recursePreorder(preorder):
            root = TreeNode(preorder.pop(0))
            if preorder == []: return root
            
            else:
                left_preorder, right_preorder = [], []
                for n in preorder:  
                    if n < root.val: left_preorder.append(n)
                    else: right_preorder.append(n)
                if left_preorder != []: root.left = recursePreorder(left_preorder)
                if right_preorder != []: root.right = recursePreorder(right_preorder)
            return root
        return recursePreorder(preorder)