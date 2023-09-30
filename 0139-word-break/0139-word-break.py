class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        wordDict = set(wordDict) # Put all words in a set which makes it O(1) retrieval time
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            found = False
            for j in range(i, len(s)):
                pot_word = s[i:j + 1]
                if pot_word in wordDict and dp[i + len(pot_word)]:
                    found = True
                    break
            dp[i] = found
        
        return dp[0]


        