class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

class BST:
    def __init__(self, vals=[]):
        self.root = None
        self.init_vals = vals
        for i in vals:
            self.insert(i)
    def insert(self, x):
        if not self.root:
            self.root = Node(x)
        else:
            cur = self.root
            while True:
                if x > cur.val:
                    if not cur.right:
                        cur.right = Node(x)
                        return
                    cur = cur.right
                if x < cur.val:
                    if not cur.left:
                        cur.left = Node(x)
                        return
                    cur = cur.left

def isSubtree(root, subroot):

    def recurseSearch(node):
        if not node: return False
        if node.val == subroot.val:
            if recurseCheck(node, subroot):
                return True
        return recurseSearch(node.left) or recurseSearch(node.right)

    def recurseCheck(node, subnode):
        if not node and not subnode:
            return True
        if node and subnode and (node.val == subnode.val):
            return recurseCheck(node.left, subnode.left) and recurseCheck(node.right, subnode.right)
        return False

    return recurseSearch(root)


tests = [
    (BST(vals=[2, 1, 3]), BST(vals=[1])),
    (BST(vals=[2, 1, 3]), BST(vals=[2])),
    (BST(vals=[2, 1, 3]), BST(vals=[2, 1, 3])),
    (BST(vals=[2, 1, 3]), BST(vals=[2, 1, 3])),
    (BST(vals=[50, 30, 70, 20, 40, 60, 80, 15, 25, 35, 45, 55, 65, 75, 85]), BST(vals=[80, 75, 85]))
]
for (root, subroot) in tests:
    print('isSubtree for {}, {}: {}'.format(root.init_vals, subroot.init_vals, isSubtree(root.root, subroot.root)))

