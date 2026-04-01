class Solution:
    def thirdMax(self, nums):
        nums = list(set(nums))  # remove duplicates
        
        nums.sort(reverse=True)
        
        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]