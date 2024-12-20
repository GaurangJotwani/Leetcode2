class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        dp = {}
        def dfs(k, i, canBuy):
            
            if (k,i,canBuy) in dp:
                return dp[(k,i,canBuy)]
            if k == 0:
                return 0
            if i == len(prices):
                return 0
            
            
            #Case 1: do nothing
            profit = dfs(k, i + 1, canBuy)

            #Case2 buy
            if canBuy:
                profit = max(profit, -prices[i] + dfs(k, i + 1, not canBuy))
            else:
                profit = max(profit, prices[i] + dfs(k - 1, i + 1, not canBuy))
            
            dp[(k,i,canBuy)] = profit
            return profit
        
        return dfs(k, 0, True)