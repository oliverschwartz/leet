class MagicDictionary:
    
    """Our strategy is to use a trie, and for any given word,
    store a complete list of its permutations and then search for each of those permutations
    
    For example, for 'hello' we store '#ello, h#llo, he#llo, etc' and when we search for 
    'hello', we search for each of those terms"""
    
    class TrieNode():
        def __init__(self, val):
            self.val = val
            self.children = {}
            self.terminal = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode(None)
        self.blacklist = set()
        
    def generatePermutations(self, term):
        n, perms = len(term), []
        for i in range(n): perms.append(term[0 : i] + '#' + term[i + 1 : n + 1])
        return perms
        
    def insertPermutation(self, perm):
        cur = self.root
        for c in perm:
            if c not in cur.children: cur.children[c] = self.TrieNode(c)
            cur = cur.children[c]
        cur.terminal = True
        
    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        permMap = {}
        for word in dict:
            self.blacklist.add(word)
            perms = self.generatePermutations(word)
            for perm in perms:
                if perm in permMap: permMap[perm].add(word)
                else: permMap[perm] = { word }
                self.insertPermutation(perm)
        
        # any perms that correspond to multiple words, mean those
        # words are actually valid and shouldn't be blacklisted
        falsePositives = set()
        for perm, words in permMap.items():
            if len(words) > 1:
                falsePositives.update(words)
        self.blacklist -= falsePositives
                
               
    def searchPermutation(self, perm):
        cur = self.root
        for c in perm:
            if c not in cur.children: return False
            else: cur = cur.children[c]
        return cur.terminal
        
    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        if word in self.blacklist: return False
        for perm in self.generatePermutations(word):
            if self.searchPermutation(perm): return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)