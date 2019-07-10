# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        visited = []
        def inorderTraverse(node):
            if node.left: inorderTraverse(node.left)
            visited.append(node.val)
            if len(visited) == k: return
            elif node.right: inorderTraverse(node.right)  
        inorderTraverse(root)
        return visited[k - 1]
                
                