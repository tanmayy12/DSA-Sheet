class Solution:
    def groupAnagrams(self, strs):
        groups = {}   # normal dictionary

        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        result = []
        for value in groups.values():
            result.append(value)

        return result
