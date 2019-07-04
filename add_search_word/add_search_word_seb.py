class WordDictionary:
    
    class WordTrie:
        def __init__(self, char):
            self.char = char
            self.children = {}
            self.terminal = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.WordTrie(None)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for idx, c in enumerate(word):
            if c not in cur.children: cur.children[c] = self.WordTrie(c)
            cur = cur.children[c]
        cur.terminal = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        """
        #print(word)
        nodes_to_explore = list(self.root.children.values())
        for idx, c in enumerate(word):
            #print(c, [x.char for x in nodes_to_explore])
            
            # got to end of trie
            if nodes_to_explore == []: return False
            
            # need to check terminal condition
            if idx == len(word) - 1:
                terminal = [n.char for n in nodes_to_explore if n.terminal]
                if c != '.': return c in terminal
                else: return len(terminal) > 0
            
            # wildcard
            if c == '.':
                new_nodes_to_explore = []
                for node in nodes_to_explore:
                    new_nodes_to_explore.extend(list(node.children.values()))
             
            # normal char
            if c != '.':
                new_nodes_to_explore = []
                for node in [n for n in nodes_to_explore if n.char == c]:
                    new_nodes_to_explore.extend(list(node.children.values()))
                    
            nodes_to_explore = new_nodes_to_explore
            
        return True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)