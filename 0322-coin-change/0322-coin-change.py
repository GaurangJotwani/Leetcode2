class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):

            minCoins = float("inf")

            for coin in coins:
               if i - coin >= 0 and dp[i - coin] != -1:
                   minCoins = min(minCoins, 1 + dp[i - coin])
            
            if minCoins != float("inf"):
                dp[i] = minCoins
        
        return dp[-1]




        