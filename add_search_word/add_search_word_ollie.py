class WordDictionary:

    def __init__(self):
        self.tst = TST()
        
    def addWord(self, word: str) -> None:
        self.tst.put(word)

    def search(self, word: str) -> bool:
        return self.tst.get(word)

class TST:
    def __init__(self):
        self.d = {}
    
    def put(self, word) -> None:
        if not word: return
        elif len(word) == 1:
            if self.d.__contains__(word): self.d[word].end = True
            else: self.d[word] = Node(char=word, end=True)
        else: 
            if not self.d.__contains__(word[0]): self.d[word[0]] = Node(char=word[0])
            self.putHelper(n=self.d[word[0]], word=word, index=0)
    
    def putHelper(self, n, word, index):
        char = word[index]
        if not n: n = Node(char=char)
        if char < n.char: n.left = self.putHelper(n=n.left, word=word, index=index)
        elif char > n.char: n.right = self.putHelper(n=n.right, word=word, index=index)
        elif index < len(word) - 1: n.mid = self.putHelper(n=n.mid, word=word, index=index+1)
        else: n.end = True
        return n
    
    def get(self, word) -> bool: # maybe contains is a more appropriate name
        if not word: return False
        elif len(word) == 1:
            if word == '.': 
                for char in self.d.keys():
                    if self.d[char].end: return True
                return False
            else: 
                if self.d.__contains__(word): return self.d[word].end
                return False
        else: 
            if word[0] == '.':
                for char in self.d.keys():
                    if self.getHelper(n=self.d[char], word=word, index=0): return True
            elif self.d.__contains__(word[0]):
                return self.getHelper(n=self.d[word[0]], word=word, index=0)
        return False
        
    def getHelper(self, n, word, index):
        if not n: return False
        char = word[index]
        if char == '.':
            if not index < len(word) - 1:
                lEnd = False
                rEnd = False
                if n.left: lEnd = n.left.end
                if n.right: rEnd = n.right.end
                return lEnd or rEnd or n.end
            elif index < len(word) - 1: return (
                    self.getHelper(n=n.left, word=word, index=index) or
                    self.getHelper(n=n.right, word=word, index=index) or
                    self.getHelper(n=n.mid, word=word, index=index+1))
            else: return (
                    self.getHelper(n=n.left, word=word, index=index) or
                    self.getHelper(n=n.right, word=word, index=index))
        elif char < n.char: return self.getHelper(n=n.left, word=word, index=index)
        elif char > n.char: return self.getHelper(n=n.right, word=word, index=index)
        elif index < len(word) - 1: return self.getHelper(n=n.mid, word=word, index=index+1)
        else: return n.end
        
        
class Node:
    def __init__(self, mid=None, left=None, right=None, char='', end=False):
        self.mid = mid
        self.left = left
        self.right = right
        self.end = end
        self.char = char

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)