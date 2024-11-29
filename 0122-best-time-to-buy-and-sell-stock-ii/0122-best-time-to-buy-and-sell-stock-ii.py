class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}
        
        def dp(i, canBuy):

            if i == len(prices):
                return 0

            if (i, canBuy) in cache:
                return cache[(i, canBuy)]
            
            #dont do anything
            p1 = dp(i + 1, canBuy)

            if canBuy:
                p2 = -prices[i] + dp(i + 1, not canBuy)
            else:
                p2 = prices[i] + dp(i + 1, not canBuy)
            
            cache[(i, canBuy)] = max(p1, p2)
            return cache[(i, canBuy)]
        
        return dp(0, True)
