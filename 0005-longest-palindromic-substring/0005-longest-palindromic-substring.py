class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        for i in range(len(s)):
            substr1 = self.getLongest(s,i,i)
            substr2 = self.getLongest(s, i, i + 1)
            if len(substr1) > len(ans):
                ans = substr1
            if len(substr2) > len(ans):
                ans = substr2
        
        return ans
    
    def getLongest(self, s, i, j):
        ans = 0
        while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1: j]
