class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        

        dp = {}

        def dfs(l,r,k):
            if l == r:
                return True
            if r - l == 1 and s[l] == s[r]:
                return True
            
            if (l,r,k) in dp:
                return dp[(l,r,k)]
            
            if s[l] == s[r]:
                dp[(l,r,k)] = dfs(l + 1, r - 1, k)
                return dp[(l,r,k)]
            
            if k > 0:
                dp[(l,r,k)] = dfs(l + 1, r, k - 1) or dfs(l, r - 1, k - 1)
            else:
                dp[(l,r,k)] = False
            
            return dp[(l,r,k)]
        
        return dfs(0, len(s) - 1, k)