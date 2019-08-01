# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        self.paths = []
        def recursePathSum(node, target, path):
            if not node: return
            if node.val == target and not node.right and not node.left:
                self.paths.append(path + str(node.val) + ',')
                return
            else:
                recursePathSum(node.right, target - node.val, path + str(node.val) + ',')
                recursePathSum(node.left, target - node.val, path + str(node.val) + ',')
        
        recursePathSum(root, sum, '')
        return [p[:-1].split('|') for p in self.paths]


# iterative solution

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0          
        
        # populate stack with (node, sum) tuples as starting points
        visited = set()
        n_paths = 0  
        stack = [(root, sum)]
        while stack:
            v, target = stack.pop()
            if v.val == target:
                n_paths += 1
            if v not in visited and v != root:
                visited.add(v)
                stack.append((v, sum))
            if v.right:
                stack.append((v.right, target - v.val))
            if v.left:
                stack.append((v.left, target - v.val))
            
        return n_paths
            
            
        