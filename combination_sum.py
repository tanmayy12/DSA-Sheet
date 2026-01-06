class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, curr, remaining):
            if remaining == 0:
                res.append(curr[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr, remaining - candidates[i])
                curr.pop()

        backtrack(0, [], target)
        return res
