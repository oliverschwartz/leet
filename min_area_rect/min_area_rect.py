from operator import itemgetter

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        # sort points by y val, then by x val
        points = sorted(points, key=itemgetter(1,0))
        
        # create a map "heights" of y coord => list of x coords
        heights = {}
        for p in points:
            if p[1] in heights: heights[p[1]].append(p[0])
            else: heights[p[1]] = [p[0]]
        
        # iterate heights, and populate sides, mapping (x coord pair @ a given height) => height
        # whenever we see that an x coord pair already has an entry, we have a rectangle (identical
        # top and bottom sides at different heights). Update area accordingly
        area = float('inf')
        sides = {}
        for y, x_list in heights.items():
            n = len(x_list)
            for i in range(n):
                for j in range(i + 1, n):
                    side = tuple([x_list[i], x_list[j]])
                    if side in sides:
                        area = min(area, (x_list[j] - x_list[i]) * (y - sides[side]))
                    sides[side] = y      
                    
        return 0 if area == float('inf') else area