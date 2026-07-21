from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        @lru_cache(None)
        def dfs(a, b):
            if a == b:
                return True

            # Different character counts → impossible
            if sorted(a) != sorted(b):
                return False

            n = len(a)

            for k in range(1, n):

                # Case 1: No swap
                if dfs(a[:k], b[:k]) and dfs(a[k:], b[k:]):
                    return True

                # Case 2: Swap
                if dfs(a[:k], b[n-k:]) and dfs(a[k:], b[:n-k]):
                    return True

            return False

        return dfs(s1, s2)