class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

class BST:
    def __init__(self, vals=[]):
        self.root = None
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

def interleave(left, right):
    if left == []:
        return [right]
    if right == []:
        return [left]
    ret = []
    ret.extend([[left[0]] + p for p in interleave(left[1:], right)])
    ret.extend([[right[0]] + p for p in interleave(left, right[1:])])
    return ret
                
def bstSeq(root):

    def recurseBstSeq(node):
        if not node.right and not node.left:
            return [[node.val]]
        subs = []
        if node.right and not node.left:
            subs = recurseBstSeq(node.right)
        elif node.left and not node.right:
            subs = recurseBstSeq(node.left)
        else:
            subs = []
            lefts, rights = recurseBstSeq(node.left), recurseBstSeq(node.right)
            for left in lefts:
                for right in rights:
                    subs.extend(interleave(left, right))
        return [[node.val] + p for p in subs]

    return recurseBstSeq(root)

print('interleave([1, 2, 3], [4, 5, 6])')
print(interleave([1, 2, 3], [4, 5, 6]))

b = BST(vals=[2, 1, 3])
print('BST: 2 1 3')
print(bstSeq(b.root))

b = BST(vals=[50, 30, 70, 20, 40, 60, 80])
print('BST: 50, 30, 70, 20, 40, 60, 80')
print(bstSeq(b.root))