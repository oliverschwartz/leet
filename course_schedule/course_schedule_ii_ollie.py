class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Create a node for each course.
        nodes = {}
        for i in range(numCourses):
            nodes[i] = Node(i)
        
        # Build the graph.
        for entry in prerequisites:
            parent = nodes[entry[1]]
            child = nodes[entry[0]]
            child.num_parents += 1
            parent.children.append(child)
        
        path = []
        roots = self.findRoots(nodes)
        while len(roots) > 0:
            children = []
            for value, node in roots.items():
                del nodes[value]
                path.append(value)
                for child in node.children:
                    children.append(child)
                    child.num_parents -= 1
            
            roots = {}
            for child in children:
                if child.num_parents == 0:
                    roots[child.val] = child
            
        if len(nodes) > 0:
            return []
        return path
        
    def findRoots(self, nodes):
        roots = {}
        for value, node in nodes.items():
            if node.num_parents == 0:
                roots[value] = node
        return roots
        
# Node class
class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []
        self.num_parents = 0

        
