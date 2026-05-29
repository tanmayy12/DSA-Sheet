class Solution(object):
    def isAdditiveNumber(self, num):

        n = len(num)

        # Try all possible first and second numbers
        for i in range(1, n):
            for j in range(i + 1, n):

                first = num[:i]
                second = num[i:j]

                # Leading zero check
                if (len(first) > 1 and first[0] == '0') or \
                   (len(second) > 1 and second[0] == '0'):
                    continue

                a = int(first)
                b = int(second)

                k = j

                while k < n:
                    s = str(a + b)

                    if not num.startswith(s, k):
                        break

                    k += len(s)
                    a, b = b, int(s)

                if k == n:
                    return True

        return False