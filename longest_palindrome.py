class Solution:
    def longestPalindrome(self, s):
        res = 0
        chars = set()
        
        for c in s:
            if c in chars:
                chars.remove(c)
                res += 2
            else:
                chars.add(c)
        
        return res + 1 if chars else res