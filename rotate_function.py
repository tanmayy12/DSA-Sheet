class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        total = sum(nums)

        # F(0)
        f = sum(i * nums[i] for i in range(n))

        ans = f

        # Calculate F(1), F(2), ... using previous F
        for k in range(1, n):
            f = f + total - n * nums[n - k]
            ans = max(ans, f)

        return ans