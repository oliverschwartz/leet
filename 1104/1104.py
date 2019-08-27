import math

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = []
        
        def reverse(lab, lev):
            return int(-lab + math.pow(2, lev) - 1 + math.pow(2, lev - 1))
        
        while not path or path[-1] != 1:
            level = math.floor(math.log(label, 2)) + 1
            path.append(label)
            label = label // 2
            label = reverse(label, level - 1)
        
        path.reverse()
        return path
