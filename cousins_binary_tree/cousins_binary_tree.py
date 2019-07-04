# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        # tree with two nodes, can't have cousins
        if root.left is None or root.right is None: return False
        
        # keep going symmetrically down till we hit a value
        nodes =  [root]
        while True:
            
            # expand our nodes and check if any of the children are cousins
            new_nodes = []
            vals = set()
            for n in nodes:
                
                # extend our child valset
                if n.left is not None:
                    vals.add(n.left.val)
                    new_nodes.append(n.left)
                if n.right is not None:
                    vals.add(n.right.val)
                    new_nodes.append(n.right)
                    
                # check if x and y are cousins, but not siblings
                if x in vals and y in vals:
                    if (n.left is not None and n.right is not None and
                        (n.left.val == x or n.left.val == y) and
                        (n.right.val == x or n.right.val == y)):
                        return False
                    else:
                        return True
            
            # if we go through all child nodes and found one but not both of
            # x and y, they're not at the same depth
            if x in vals or y in vals: return False
            nodes = new_nodes