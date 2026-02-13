class Solution:
    def distributeCandies(self, candyType):
        unique_types = len(set(candyType))
        return min(unique_types, len(candyType) // 2)