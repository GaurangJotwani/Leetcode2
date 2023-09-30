class Solution:
    def numDecodings(self, s: str) -> int:

        output = 0
        seen = {}


        def helper(idx):

            if idx in seen:
                return seen[idx]
            
            if idx >= len(s):
                return 1

            if s[idx] == "0":
                return 0
            
            
            
            ans = helper(idx + 1)
            if idx + 1 < len(s) and (s[idx] == "1" or (s[idx] == "2" and s[idx + 1] in "0123456")):
                ans += helper(idx + 2)
            
            seen[idx] = ans
            return seen[idx]
        
        return helper(0)

        