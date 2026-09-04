class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}

        # Build graph
        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        # DFS
        def dfs(current, target, product, visited):
            if current == target:
                return product

            visited.add(current)

            for neighbor, value in graph[current]:
                if neighbor not in visited:
                    result = dfs(
                        neighbor,
                        target,
                        product * value,
                        visited
                    )

                    if result != -1.0:
                        return result

            return -1.0

        answer = []

        for a, b in queries:
            if a not in graph or b not in graph:
                answer.append(-1.0)
            else:
                answer.append(dfs(a, b, 1.0, set()))

        return answer