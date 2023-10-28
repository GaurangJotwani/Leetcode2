class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [""]
        
        for i in range(len(s)):
            self.getPalLength(i, i, s, res)
            self.getPalLength(i, i + 1, s, res)
        
        return res[0]
    
    
    def getPalLength(self, i, j, s, res):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        
        if j - i - 1 > len(res[0]):
            res[0] = s[i + 1: j]
        
        