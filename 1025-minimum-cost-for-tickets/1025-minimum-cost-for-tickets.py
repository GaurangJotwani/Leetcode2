class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = {}

        def dfs(i):
            if i >= len(days):
                return 0
            
            if i in dp:
                return dp[i]
            
            #Case 1: take single day ticket
            ans1 = costs[0] + dfs(i + 1)

            #Case 2: 7 day pass
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1
            ans2 = costs[1] + dfs(j)

            #Case 2: 30 day pass
            j = i
            while j < len(days) and days[j] < days[i] + 30:
                j += 1
            ans3 = costs[2] + dfs(j)

            dp[i] = min(ans1, ans2, ans3)

            return dp[i]
        
        return dfs(0)




        