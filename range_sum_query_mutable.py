class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)

        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def _prefixSum(self, i):
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & -i
        return total

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._prefixSum(right + 1) - self._prefixSum(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index, val)
# param_2 = obj.sumRange(left, right)