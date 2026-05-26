class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        order = []
        front = 0

        while front < len(queue):

            node = queue[front]
            front += 1

            order.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) == numCourses:
            return order

        return []
        