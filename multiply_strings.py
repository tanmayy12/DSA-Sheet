class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum_ = mul + res[i + j + 1]

                res[i + j + 1] = sum_ % 10
                res[i + j] += sum_ // 10

        # Skip leading zeros
        result = []
        for digit in res:
            if not (len(result) == 0 and digit == 0):
                result.append(str(digit))

        return "".join(result)
