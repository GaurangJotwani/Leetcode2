class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        mod = 10**9 + 7

        # for i in range(1, n  + 1):
        #     for j in range(k + 1):
        #         dp[i][j] = dp[i - 1][j]
        #         if j - 1 >= 0:
        #             dp[i][j] += dp[i][j - 1]
        #         if j - i >= 0:
        #             dp[i][j] -= dp[i-1][j - i]

        curr = [0] * (k + 1)
        prev = [0] * (k + 1)
        prev[0] = 1
        
        for i in range(1, n + 1):
            for j in range(k + 1):
                curr[j] = prev[j]
                if j - 1 >= 0:
                    curr[j] += curr[j - 1]
                    curr[j] = curr[j] % mod
                if j - i >= 0:
                    curr[j] -= prev[j - i]
            
            tmp = prev
            prev = curr
            curr = tmp
        
        return prev[k] % mod

