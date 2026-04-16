class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        # build graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # use list as queue
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        i = 0  # pointer instead of pop(0)
        
        while i < len(queue):
            node = queue[i]
            i += 1
            count += 1
            
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return count == numCourses