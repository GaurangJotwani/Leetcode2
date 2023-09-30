class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            p1 = self.getCount(i, i, s)
            if len(p1) > len(longest):
                longest = p1
            p2 = self.getCount(i, i + 1, s)
            if len(p2) > len(longest):
                longest = p2
            
        return longest
    
    def getCount(self, start, end, s):
        print(start, end)
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        
        return s[start + 1: end]
        