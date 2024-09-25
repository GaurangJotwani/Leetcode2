class Solution:
    def numSquares(self, n: int) -> int:

        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        
        for i in range(n + 1):
            tmp = dp[i]
            j = 1
            while j * j <= i:
                tmp = min(tmp, 1 + dp[i - j * j])
                j += 1
            dp[i] = tmp

        return dp[-1] 
        