class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        for i in range(len(s)):
            count += self.getCount(i, i, s)
            count += self.getCount(i, i + 1, s)
        
        return count
    
    def getCount(self, start, end, s):
        count = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            count += 1
            start -= 1
            end += 1
        
        return count




        