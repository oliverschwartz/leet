# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        x_indices, y_indices = [], []
        node_coord_map = {}
        
        # do recursive traversal to build coordinate map
        def traverse(x_index, y_index, node):
            x_indices.append(x_index)
            y_indices.append(y_index)
            
            # update coordinate map
            if x_index in node_coord_map:
                if y_index in node_coord_map[x_index]: node_coord_map[x_index][y_index].append(node.val)
                else: node_coord_map[x_index][y_index] = [node.val]
            else: node_coord_map[x_index] = {y_index: [node.val]}
                
            # recurse
            if node.left is not None: traverse(x_index - 1, y_index + 1, node.left)
            if node.right is not None: traverse(x_index + 1, y_index + 1, node.right)
                
        traverse(0, 0, root)
        
        # go from min to max coord, appending sorted lists of vals from map
        ret = []
        for x_coord in range(min(x_indices), max(x_indices) + 1):
            lvl = []
            for y_coord in range(min(y_indices), max(y_indices) + 1):
                if x_coord in node_coord_map and y_coord in node_coord_map[x_coord]: 
                    lvl.extend(sorted(node_coord_map[x_coord][y_coord]))
            if lvl != []: ret.append(lvl)
        return ret