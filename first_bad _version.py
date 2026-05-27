# Dummy API for local testing
def isBadVersion(version):
    bad = 4
    return version >= bad


class Solution(object):
    def firstBadVersion(self, n):

        left = 1
        right = n

        while left < right:

            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


# Testing
sol = Solution()
print(sol.firstBadVersion(5))