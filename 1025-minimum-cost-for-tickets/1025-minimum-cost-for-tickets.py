class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        memo = {}

        def dp(i):
            if i >= len(days):
                return 0

            if i in memo:
                return memo[i]
            
            #Case 1, daily ticket
            ans1 = costs[0] + dp(i + 1)

            #Case 2, weekly ticket
            j = i
            while j < len(days) and days[j] - days[i] < 7:
                j += 1
            ans2 = costs[1] + dp(j)

            #Case 3, monthly ticket
            j = i
            while j < len(days) and days[j] - days[i] < 30:
                j += 1
            ans3 = costs[2] + dp(j)

            memo[i] = min(ans1, ans2, ans3) 
            return memo[i]
        
        return dp(0)



        