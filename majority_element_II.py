class Solution:
    def majorityElement(self, nums):
        # Step 1: find candidates
        count1 = count2 = 0
        cand1 = cand2 = None
        
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: verify
        result = []
        for c in [cand1, cand2]:
            if nums.count(c) > len(nums) // 3:
                result.append(c)
        
        return result