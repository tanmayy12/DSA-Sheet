class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(start, curr, remaining):
            if remaining == 0:
                res.append(curr[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                curr.append(candidates[i])
                backtrack(i + 1, curr, remaining - candidates[i])
                curr.pop()

        backtrack(0, [], target)
        return res
