import queue

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph, indegree = {}, {}
        for c in range(numCourses):
            graph[c] = []
            indegree[c] = 0
        
        for first, second in prerequisites:
            graph[second].append(first)
            indegree[first] += 1
        
        q = queue.Queue()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.put(c)
        
        order = []
        while not q.empty():
            v = q.get()
            order.append(v)
            for c in graph[v]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.put(c)
            del graph[v]
            
        return order if graph == {} else []