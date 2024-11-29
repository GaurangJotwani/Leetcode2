class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        
        items.sort()
        prices = []
        max_seen = 0

        for price, beauty in items:
            max_seen = max(max_seen, beauty)
            if prices and prices[-1][0] == price:
                prices[-1][1] = max_seen
                continue
            prices.append([price, max_seen])
        
        output = []
        for q in queries:
            output.append(self.findBest(prices, q))
        return output
            
    
    def findBest(self, prices, q):
        l,r = 0, len(prices) - 1
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if prices[mid][0] <= q:
                res = prices[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res

            

        

