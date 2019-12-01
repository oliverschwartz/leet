# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.champion = (0, root.val)
        
        def levelOrder(level, root):
            if not root:
                return
            elif level > self.champion[0]:
                self.champion = (level, root.val)
            levelOrder(level + 1, root.left)
            levelOrder(level + 1, root.right)
            
        levelOrder(0, root)
        return self.champion[1]
