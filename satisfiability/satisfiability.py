class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        # build graph with equalities, and list of equalities
        # to check after we perform DFS
        graph, inequalities = {}, []
        for e in equations:
            x, op, y = e[0], e[1:3], e[3]
            if op == '==':
                if x not in graph: graph[x] = [y]
                else: graph[x].append(y)
                if y not in graph: graph[y] = [x]
                else: graph[y].append(x)
            else:
                inequalities.append([x, y])

        # do DFS and get strongly connected components (equality groups)
        # we traverse all possible entry points, and for each do a DFS
        # to build a component map of of vertex => component
        visited, component_map = set(), {}
        component_count = 0
        for v in graph:
            if v in visited: continue
            stack = [v]
            while len(stack) > 0:
                w = stack.pop()
                if w in visited: continue
                visited.add(w)
                component_map[w] = component_count
                if w in graph:
                    stack.extend(graph[w])
            component_count += 1
            
        # now check if we our equalities work with our components. For any
        # given inequality, the variables must live in two different components
        # for satisfiability
        for ineq in inequalities:
            
            # in case if we have a self contradictory inequality that's not in graph
            if ineq[0] == ineq[1]: return False
            
            # if either variable wasn't in equality graph then we can pass
            if ineq[0] not in visited or ineq[1] not in visited: continue
                
            # if they're in the same equality connected component, then
            # satisfiability is violated
            if component_map[ineq[0]] == component_map[ineq[1]]: return False
        
        return True