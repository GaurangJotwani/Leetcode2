class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        cache = {}
        
        def helper(idx, cAmount):
            
            if (idx, cAmount) in cache:
                return cache[(idx, cAmount)]
            
            if cAmount == amount:
                return 1
            
            if cAmount > amount or idx >= len(coins):
                return 0
            
            ans1 = helper(idx, cAmount + coins[idx])
            
            ans2 = helper(idx + 1, cAmount)
            
            cache[(idx, cAmount)] = ans1 + ans2
            
            return cache[(idx, cAmount)]
        
        
        return(helper(0, 0))

        
                
        