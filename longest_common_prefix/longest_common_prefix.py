class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = Trie()
        for s in strs: t.put(s)
        return t.get_longest_prefix(len(strs))

class Trie:            
    def __init__(self):
        self.root = Node()
    
    def get_longest_prefix(self, num):
        node = self.root
        if node.children == None: return ''
        elif len(node.children.keys()) > 1: return ''
        
        pref = ''
        
        while (True):
            if node.children == None: break
            for char, child in node.children.items():
                found = False
                if child.count == num:
                    pref += child.char
                    node = child
                    found = True
            if not found: break
        return pref
                    
    def put(self, w):
        n = self.root
        i = 0
        while (i < len(w)):
            if n.children == None:
                n.children = {}
                n.children[w[i]] = Node(char=w[i])
            elif not n.children.__contains__(w[i]):
                n.children[w[i]] = Node(char=w[i])
            else: 
                n.children[w[i]].count += 1
            n = n.children[w[i]]
            i += 1
            
""" Each node can as many children as necessary.
    Each node stores a count of the number of words
    that pass along it """
class Node:
    def __init__(self, children=None, char='', count=1):
        self.children = children
        self.count = count
        self.char = char
        

            