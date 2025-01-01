class Solution:
    def makeStringGood(self, s: str) -> int:
        


        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        @cache
        def dp(i, target, deleted):
            if i >= 26:
                return 0
            
            if counts[i] == target or counts[i] == 0:
                return dp(i + 1, target, 0)
            
            x = counts[i]

            if x > target:
                return dp(i + 1, target, x-target) + x - target
            else:
                need = target - x

                insert = need + dp(i + 1, target, 0)

                delete = x + dp(i + 1, target, x)

                change = dp(i + 1, target, 0) + need - min(need, deleted)

                return min(insert, delete, change)


        res = float("inf")

        max_freq = max(counts)

        for i in range(0, max_freq + 1):
            res = min(res, dp(0,i,0))
        
        return res