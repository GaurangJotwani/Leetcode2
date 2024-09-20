class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        total = sum(matchsticks)
        n = len(matchsticks)
        if total % 4:
            return False
        target = total // 4
        matchsticks.sort(reverse=True)

        used = [False for i in range(n)]
        def dfs(i, cSum, groups):
            if groups == 1:
                return True
            
            if cSum == target:
                return dfs(0,0,groups - 1)
            
            for j in range(i, n):
                if used[j] or cSum + matchsticks[j] > target:
                    continue
                
                used[j] = True
                if dfs(j + 1,  cSum + matchsticks[j], groups):
                    return True
                used[j] = False

                if cSum == 0:
                    break
            
            return False
        
        return dfs(0, 0, 4)

