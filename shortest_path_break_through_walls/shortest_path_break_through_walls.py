# from https://leetcode.com/discuss/interview-question/353827/Google-or-Onsite-or-Shortest-Path-Breaking-Through-Walls

import queue

# m is 2x2 matrix, k is number of walls we can break
def shortest_path(m, k):
    nr, nc = len(m), len(m[0])

    def get_neighbours(tile):
        (x, y) = tile
        nbs = []
        for (a, b) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + a <= nr - 1 and 0 <= y + b <= nc - 1:
                nbs.append((x + a, y + b))
        return nbs

    # do BFS tracking dist
    q = queue.Queue()
    q.put(((0, 0), 0, k))
    visited = [[None for c in range(nc)] for r in range(nr)] 

    while not q.empty():
        (r, c), dist, walls = q.get()
        visited[r][c] = walls

        # we found the goal!
        if  (r, c) == (nr - 1, nc - 1) and walls >= m[r][c]:
            return dist

        # we're blocked
        elif m[r][c] == 1 and walls == 0:
            continue

        # populate new nodes
        else:
            new_walls = (walls - 1 if m[r][c] else walls)
            for (x, y) in get_neighbours((r, c)):
                if not visited[x][y] or visited[x][y] < new_walls:
                    q.put(((x, y), dist + 1, new_walls))
    return -1


assert shortest_path(
    [[0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0]],
    2
) == 10