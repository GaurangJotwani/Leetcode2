class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        if n == 1:
            return 1
        
        for i in range(2, n + 1):
            l = 0 
            r = i - 1
            res = 0
            while r >= 0:
                res += dp[l] * dp[r]
                l += 1
                r -= 1
            dp[i] = res
        
        return dp[-1]
