class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        
        dp = [1] * len(pairs)
        
        pairs.sort()
        
        
        for idx, pair in enumerate(pairs):
            c, d = pair[0], pair[1]
            for i in range(idx):
                a, b = pairs[i][0], pairs[i][1]
                if c > b:
                    dp[idx] = max(dp[idx], 1 + dp[i])
        
        
        return max(dp)
            
        
        