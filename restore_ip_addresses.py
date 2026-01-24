class Solution:
    def restoreIpAddresses(self, s):
        res = []

        def backtrack(start, path):
            # If we have 4 parts and used all characters
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            # Try segments of length 1 to 3
            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                # Invalid if leading zero or > 255
                if (part.startswith("0") and len(part) > 1) or int(part) > 255:
                    continue

                backtrack(start + length, path + [part])

        backtrack(0, [])
        return res
