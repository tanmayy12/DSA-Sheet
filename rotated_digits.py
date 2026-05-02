class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {'0','1','8','2','5','6','9'}
        change = {'2','5','6','9'}
        
        count = 0
        
        for num in range(1, n + 1):
            s = str(num)
            
            if any(d not in valid for d in s):
                continue
            
            if any(d in change for d in s):
                count += 1
        
        return count