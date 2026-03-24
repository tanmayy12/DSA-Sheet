class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        for c in t:
            count[ord(c) - ord('a')] -= 1
        
        return all(x == 0 for x in count)