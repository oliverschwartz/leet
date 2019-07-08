# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # corner cases: no root, and only root
        if root == None: return 0
        elif root.left == None and root.right == None: return 1
        
        # do level order traversal
        q = [(root, 0)]
        champ = 1
        level = 0
        while len(q) > 0:
            
            oldq = []
            while len(q) > 0:
                oldq.append(q.pop(0))
            
            min_pos = (2 ** level) - 1
            max_pos = 0
            
            for tup in oldq:
                pos = tup[1]
                node = tup[0]
                if pos > max_pos: max_pos = pos
                if pos < min_pos: min_pos = pos
                if node.left != None: q.append((node.left, pos*2))
                if node.right != None: q.append((node.right, pos*2 + 1))
                    
            level_width = max_pos - min_pos + 1
            if level_width > champ: champ = level_width        
            
            level += 1
                    
        return champ