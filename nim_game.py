class Solution(object):
    def canWinNim(self, n):

        # If n is divisible by 4, you lose
        return n % 4 != 0