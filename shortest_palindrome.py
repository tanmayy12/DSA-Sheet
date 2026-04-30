class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        new = s + "#" + rev
        
        lps = [0] * len(new)
        
        j = 0
        for i in range(1, len(new)):
            while j > 0 and new[i] != new[j]:
                j = lps[j - 1]
            
            if new[i] == new[j]:
                j += 1
            
            lps[i] = j
        
        # length of longest palindromic prefix
        longest = lps[-1]
        
        return rev[:len(s) - longest] + s