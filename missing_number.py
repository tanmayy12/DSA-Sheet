class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        res = n
        
        for i in range(n):
            res ^= i ^ nums[i]
        
        return res