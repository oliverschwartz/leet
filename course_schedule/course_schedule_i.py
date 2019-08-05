import queue

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph, indegree = {}, {}
        for c in range(numCourses):
            graph[c] = []
            indegree[c] = 0
        
        for first, second in prerequisites:
            graph[first].append(second)
            indegree[second] += 1
            
        q = queue.Queue()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.put(c)
                
        while not q.empty():
            v = q.get()
            for c in graph[v]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.put(c)
            del graph[v]
            
        return graph == {}