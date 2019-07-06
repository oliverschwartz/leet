# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        d = self.getDepth(root, 0) # depth of tree
        l = (2 ** (d+1)) - 1       # length of each array
        mid = int((l/2) - 0.5)     # middle of array
        
        # create array of arrays of empty strings
        tree = []
        for i in range(d + 1):
            tree.append([""] * l)            
        
        # use queue: at each level, dequeue everything in queue.
        # then, requeue all children from left to right
        q = [(root, mid)]
        level = 0
        while len(q) != 0:
            to_add = []
            while len(q) != 0:
                n = q.pop(0)
                tree[level][n[1]] = str(n[0].val)
                to_add.append(n)

            # amount the child will be shifted by (left or right)
            shift = 2 ** (d - 1 - level)
                
            # enqueue a tuple of (node, position)
            for n in to_add:
                node = n[0]
                if node.left: q.append((node.left, n[1] - shift))
                if node.right: q.append((node.right, n[1] + shift))
                
            level += 1
        return tree
        
    def getDepth(self, root, d):
        if not root: return d - 1
        else: return max(self.getDepth(root.left, d + 1),
                   self.getDepth(root.right, d + 1))
        
        