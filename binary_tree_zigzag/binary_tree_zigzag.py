# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        # edge case
        if root is None: return []
        
        # traverse
        level_order = [[root.val]]
        nodes = [root]
        index = 0
        while True:
            n = len(nodes)
            if n == 0: break

            new_nodes = []
            level = []
            for i in range(n):
                
                # append values right to left
                if index % 2 == 0:
                    if nodes[n - i - 1].right is not None:
                        level.append(nodes[n - i - 1].right.val)
                    if nodes[n - i - 1].left is not None:
                        level.append(nodes[n - i - 1].left.val)
                        
                # append values left to right
                else:
                    if nodes[i].left is not None:
                        level.append(nodes[i].left.val)
                    if nodes[i].right is not None:
                        level.append(nodes[i].right.val)
                        
                # we always append nodes left to right
                if nodes[i].left is not None: new_nodes.append(nodes[i].left)
                if nodes[i].right is not None: new_nodes.append(nodes[i].right)
            
            index += 1
            if level != []: level_order.append(level)
            nodes = new_nodes
            
        return level_order