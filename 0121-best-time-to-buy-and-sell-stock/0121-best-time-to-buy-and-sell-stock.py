class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        ans = 0
        for price in prices:
            minPrice = min(price, minPrice)
            ans = max(ans, price - minPrice)
        
        return ans