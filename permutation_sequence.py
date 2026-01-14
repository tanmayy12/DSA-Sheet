class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Step 1: factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        # Step 2: numbers list
        nums = []
        for i in range(1, n + 1):
            nums.append(str(i))

        # Step 3: make k zero-based
        k -= 1

        result = ""

        # Step 4: build permutation
        for i in range(n, 0, -1):
            block = fact[i - 1]
            index = k // block
            result += nums[index]

            nums.pop(index)
            k %= block

        return result
