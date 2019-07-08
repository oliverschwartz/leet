# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # corner cases (avoid recursion on small arrays)
        if len(nums) == 0: return None   
        if len(nums) == 1: return TreeNode(nums[0])
        
        return self.buildTree(nums)

    # recursive method to create tree
    def buildTree(self, nums):
        # base case
        if len(nums) == 0: return None
        
        # create a node with the max value of the array
        i_max = nums.index(max(nums))
        node = TreeNode(nums[i_max])
        
        # populate the node's children
        node.left = self.buildTree(nums[:i_max])
        node.right = self.buildTree(nums[i_max+1:])
        
        return node