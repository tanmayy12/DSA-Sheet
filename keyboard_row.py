
class Solution:
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            lower_word = word.lower()

            if all(ch in row1 for ch in lower_word):
                result.append(word)
            elif all(ch in row2 for ch in lower_word):
                result.append(word)
            elif all(ch in row3 for ch in lower_word):
                result.append(word)

        return result