class Solution:
    def permute(self, nums):
        res = []
        used = [False] * len(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()
                used[i] = False

        backtrack([])
        return res
