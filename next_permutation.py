class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2

        # Step 1: find first decreasing element
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: find just larger element and swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: reverse the right part
        nums[i + 1:] = reversed(nums[i + 1:])
