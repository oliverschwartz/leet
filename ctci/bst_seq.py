class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class BST:
    def __init__(self, seq=[]):
        self.root = None
        for i in seq:
            self.add(i)
    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            cur = self.root
            while True:
                if val < cur.val:
                    if not cur.left:
                        cur.left = Node(val)
                        return
                    cur = cur.left
                if val > cur.val:
                    if not cur.right:
                        cur.right = Node(val)
                        return
                    cur = cur.right
    
def BST_seq(root):

    def BST_seq_recurse(node):
        if not node:
            return [None]
        l, r = BST_seq_recurse(node.left), BST_seq_recurse(node.right)

        ret = []
        for sl in l:
            for sr in r:
                seq = [node.val]
                if sr and sl:
                    s1, s2 = seq + sr + sl, seq + sl + sr
                    ret.extend([s1, s2])
                elif sr:
                    ret.append(seq + sr)
                elif sl: 
                    ret.append(seq + sl)
                else:
                    ret.append(seq)
        return ret

    return BST_seq_recurse(root)