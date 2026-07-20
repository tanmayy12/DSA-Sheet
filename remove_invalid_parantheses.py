from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        def isValid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    if count == 0:
                        return False
                    count -= 1
            return count == 0

        res = []
        visited = set([s])
        queue = deque([s])
        found = False

        while queue:
            curr = queue.popleft()

            if isValid(curr):
                res.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue

                nxt = curr[:i] + curr[i + 1:]

                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return res