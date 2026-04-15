class Solution:
    def hIndex(self, citations):
        n = len(citations)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if citations[mid] >= n - mid:
                right = mid - 1   # try smaller index
            else:
                left = mid + 1    # move right
        
        return n - left