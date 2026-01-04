class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = ""

        for i in range(len(strs[0])):
            ch = strs[0][i]

            for word in strs[1:]:
                if i >= len(word) or word[i] != ch:
                    return prefix

            prefix += ch

        return prefix
