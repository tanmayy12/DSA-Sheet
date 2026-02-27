class Solution:
    def minCut(self, s):
        n = len(s)
        
        # Step 1: Palindrome table
        is_pal = [[False] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
        
        # Step 2: DP for minimum cuts
        cuts = [0] * n
        
        for i in range(n):
            min_cut = i  # maximum possible cuts
            
            for j in range(i + 1):
                if is_pal[j][i]:
                    if j == 0:
                        min_cut = 0
                    else:
                        min_cut = min(min_cut, cuts[j - 1] + 1)
            
            cuts[i] = min_cut
        
        return cuts[-1]