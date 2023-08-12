class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        
        if obstacleGrid[ROWS - 1][COLS - 1] != 1:
            dp[ROWS - 1][COLS - 1] = 1
        
        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                
                if i == ROWS - 1 and j == COLS - 1:
                    continue
                
                if obstacleGrid[i][j] == 1:
                    continue
    
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        
        
        return dp[0][0]
        