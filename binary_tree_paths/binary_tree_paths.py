# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        self.paths = []
        def recurseTreePath(node, path):
            if not node:
                return
            if not node.left and not node.right:
                self.paths.append(path + str(node.val))
            if node.left:
                recurseTreePath(node.left, path + str(node.val) + '->')
            if node.right:
                recurseTreePath(node.right, path + str(node.val) + '->')
                
        recurseTreePath(root, '')
        return self.paths

# iterative version
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        
        paths = []
        stack = [(root, '')]
        while stack:
            v, p = stack.pop()
            if not v.left and not v.right:
                paths.append(p + str(v.val))
            if v.right:
                stack.append((v.right, p + str(v.val) + '->'))
            if v.left:
                stack.append((v.left, p + str(v.val) + '->'))
        return paths