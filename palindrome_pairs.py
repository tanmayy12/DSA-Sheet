class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_map = {word: i for i, word in enumerate(words)}
        res = []

        def isPalindrome(s):
            return s == s[::-1]

        for i, word in enumerate(words):
            for j in range(len(word) + 1):

                left = word[:j]
                right = word[j:]

                # Case 1
                if isPalindrome(left):
                    rev = right[::-1]
                    if rev in word_map and word_map[rev] != i:
                        res.append([word_map[rev], i])

                # Case 2
                # j != len(word) avoids duplicates
                if j != len(word) and isPalindrome(right):
                    rev = left[::-1]
                    if rev in word_map and word_map[rev] != i:
                        res.append([i, word_map[rev]])

        return res