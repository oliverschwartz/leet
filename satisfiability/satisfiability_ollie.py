class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        g = Graph()
        ineqs = []
        
        for e in equations:
            # corner case: a != a
            if e[0] == e[3] and e[1] == '!': return False
            elif e[1] == '=': g.connect(e[0], e[3])
            else: ineqs.append(e)

        for i in ineqs:
            if i[3] in g.adj.keys() and i[0] in g.adj.keys():
                if i[3] in g.dfs(i[0]): return False
        
        return True
        
class Graph:
    def __init__(self, adj=None):
        if adj == None:
            self.adj = {}
        else: self.adj = None
        
    # connect two nodes (or create the nodes
    # if they aren't already in the graph)
    def connect(self, a, b):
        if not self.adj.__contains__(a):
            self.adj[a] = [b]
        else: self.adj[a].append(b)
        if not self.adj.__contains__(b):
            self.adj[b] = [a]
        else: self.adj[b].append(a)
            
    # recursive dfs method:
    # returns all nodes reachable from 'start'
    def dfs(self, start, seen=None):
        if seen == None: seen = []
        seen.append(start)
        for a in self.adj[start]:
            if not a in seen:
                seen = self.dfs(a, seen)
        return seen
        
            
        
        
        