# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        # edge case
        if root is None: return []
        
        level_order = [[root.val]]
        nodes = [root]
        while True:
            
            # run out of nodes
            if nodes == []: break
            
            # traverse current nodes, add children and values
            level = []
            new_nodes = []
            for n in nodes:
                if n.left is not None:
                    new_nodes.append(n.left)
                    level.append(n.left.val)
                if n.right is not None:
                    new_nodes.append(n.right)
                    level.append(n.right.val)
            if level != []: level_order.append(level)
            nodes = new_nodes
            
        return level_order