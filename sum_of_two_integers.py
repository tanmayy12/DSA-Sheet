class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff   # 32-bit mask
        
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        
        # handle negative numbers
        return a if a <= 0x7fffffff else ~(a ^ mask)