# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        self.root = root
        
        def delete(val):
            node, parent = find(val)
            if not node:
                return
            
            # node is a child
            if not node.left and not node.right:
                if not parent:
                    self.root = None
                elif parent.right == node:
                    parent.right = None
                elif parent.left == node:
                    parent.left = None
                return
            
            # node missing left or right, so no need to insert
            elif not node.left:
                if not parent:
                    self.root = node.right
                elif parent.right == node:
                    parent.right = node.right
                elif parent.left == node:
                    parent.left = node.right
                return
            elif not node.right:
                if not parent:
                    self.root = node.left
                elif parent.right == node:
                    parent.right = node.left
                elif parent.left == node:
                    parent.left = node.left
                return
            
            # node has both left and right, change parent to right and insert left
            else:
                if not parent:
                    self.root = node.left
                elif parent.right == node:
                    parent.right = node.left
                elif parent.left == node:
                    parent.left = node.left
                insert(node.right)
                return
            
        def insert(node):
            cur = self.root
            while True:
                if node.val > cur.val:
                    if not cur.right:
                        cur.right = node
                        return
                    cur = cur.right
                if node.val < cur.val:
                    if not cur.left:
                        cur.left = node
                        return
                    cur = cur.left
        
        def find(val):
            parent = None
            cur = self.root
            while cur:
                if val < cur.val:
                    parent = cur
                    cur = cur.left
                elif val > cur.val:
                    parent = cur
                    cur = cur.right
                else:
                    return (cur, parent)
            return (cur, parent)
        
        delete(key)
        return self.root
            