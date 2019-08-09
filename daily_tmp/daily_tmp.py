class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)

        warmer = [0 for _x in range(n)]
        
        to_find_warmer = []
        for i in range(n):
            while to_find_warmer and to_find_warmer[-1][0] < T[i]:
                (_temp, idx) = to_find_warmer.pop()
                warmer[idx] = i - idx 
            to_find_warmer.append((T[i], i))
        return warmer
            