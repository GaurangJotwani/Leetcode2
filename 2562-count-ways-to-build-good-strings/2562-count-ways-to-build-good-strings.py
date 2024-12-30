class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:


        mod = 10**9 + 7
        cache = {}
        def dfs(cLen):

            if cLen > high:
                return 0
            
            if cLen in cache:
                return cache[cLen]

            total = 1 if cLen >= low else 0

            total += dfs(cLen + zero) % mod

            total += dfs(cLen + one) % mod

            cache[cLen] = total % mod

            return cache[cLen]
        

        return dfs(0)
        


            
            
        