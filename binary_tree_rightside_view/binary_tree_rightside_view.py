# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        # build a right order traversal list, of format
        # (val, depth)
        visited = []
        def rightSideDFS(node, depth):
            if not node: return
            visited.append((node.val, depth))
            rightSideDFS(node.right, depth + 1)
            rightSideDFS(node.left, depth + 1)
        rightSideDFS(root, 0)
        
        # iterate our traversal, each time we get to a lower depth,
        # append that value
        vals, seen_depth = [], -1
        for (val, depth) in visited:
            if depth > seen_depth:
                vals.append(val)
                seen_depth = depth
        return vals