class Solution:
    def getSmallestString(self, s: str) -> str:
        
        for i in range(len(s)):
            if i + 1 < len(s) and (int(s[i + 1]) % 2) == (int(s[i]) % 2):
                if s[i + 1] < s[i]:
                    return s[0:i] + s[i + 1] + s[i] + s[i + 2:]
        
        return s
