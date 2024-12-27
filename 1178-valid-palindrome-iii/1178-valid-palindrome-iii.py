class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        

        dp = {}

        def dfs(l,r):
            if l == r:
                return 0
            if r - l == 1:
                if s[l] == s[r]:
                    return 0
                else:
                    return 1
            
            if (l,r) in dp:
                return dp[(l,r)]
            
            if s[l] == s[r]:
                dp[(l,r)] = dfs(l + 1, r - 1)
                return dp[(l,r)]
            

            dp[(l,r)] = 1 + min(dfs(l + 1, r),dfs(l, r - 1))
            
            return dp[(l,r)]
        
        return dfs(0, len(s) - 1) <= k