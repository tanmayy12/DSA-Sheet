class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            # If already computed
            if start in memo:
                return memo[start]

            # Reached end of string
            if start == len(s):
                return [""]

            sentences = []

            # Try every possible word
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordSet:
                    # Get remaining sentences
                    rest_sentences = dfs(end)

                    for sentence in rest_sentences:
                        if sentence:
                            sentences.append(word + " " + sentence)
                        else:
                            sentences.append(word)

            memo[start] = sentences
            return sentences

        return dfs(0)