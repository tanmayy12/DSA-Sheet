from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # convert to string
        nums = list(map(str, nums))
        
        # custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1   # a should come first
            else:
                return 1    # b should come first
        
        nums.sort(key=cmp_to_key(compare))
        
        result = ''.join(nums)
        
        # handle case like [0,0]
        return '0' if result[0] == '0' else result