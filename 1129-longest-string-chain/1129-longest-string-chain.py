class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words = sorted(words, key = lambda x: len(x))

        dp = [1] * len(words)
        res = 1
        for i in range(1, len(words)):
            word = words[i]
            for j in range(i - 1, -1, -1):
                if self.isPredecessor(words[j], word):
                    dp[i] = max(dp[i], 1 + dp[j])
            
            res = max(res, dp[i])

        return res


    def isPredecessor(self, word1, word2):
        if len(word2) - len(word1) != 1:
            return False

        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                j += 1
            
            if i == len(word1):
                break
        
        return i == len(word1)
        