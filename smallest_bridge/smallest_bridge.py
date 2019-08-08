import queue

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        rs, cs = len(A), len(A[0])
        
        def get_neighbours(tile):
            (row, col) = tile
            neighbours = []
            if row > 0: neighbours.append((row - 1, col))
            if row < rs - 1: neighbours.append((row + 1, col))
            if col > 0: neighbours.append((row, col - 1))
            if col < cs - 1: neighbours.append((row, col + 1))
            return neighbours
        
        # find first island
        first = None
        for i in range(rs):
            for j in range(cs):
                if A[i][j]:
                    first = (i, j)
                    break
            if first: break
                
        # dfs all nodes in first island
        first_island = set()
        stack = [first]
        while stack:
            (row, col) = stack.pop()
            if A[row][col]:
                if A[row][col]: first_island.add((row, col))
                stack.extend([n for n in get_neighbours((row,  col)) if n not in first_island])
                
        # do BFS from first island
        q = queue.Queue()
        for n in first_island: q.put((n, 0))
        while not q.empty():
            ((row, col), dist) = q.get()
            if (row, col) not in first_island and A[row][col]:
                return dist - 1
            for n in [n for n in get_neighbours((row,  col)) if n not in first_island]:
                q.put((n, dist + 1))

