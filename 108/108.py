# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def createTree(subarr):
            if len(subarr) == 0:
                return None
            mid = len(subarr) // 2
            newNode = TreeNode(subarr[mid])
            newNode.left = createTree(subarr[:mid])
            newNode.right = createTree(subarr[mid+1:])
            return newNode
        
        return createTree(nums)