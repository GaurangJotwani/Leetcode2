class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        dr = [[1,0],[-1,0],[0,-1],[0,1]]
        visited = set()
        def dfs(r, c):
            ans = grid[r][c]
            
            for d in dr:
                row, col = r + d[0], c + d[1]
                if (row >= 0 and row < ROWS and
                    col >= 0 and col < COLS and
                    (row, col) not in visited and
                    grid[row][col] != 0):
                    visited.add((row, col))
                    ans = max(ans, grid[r][c] + dfs(row, col))
                    visited.remove((row, col))
            
            
            return ans
        
        res = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    visited = set()
                    visited.add((r,c))
                    res = max(res, dfs(r, c))
                    visited.remove((r, c))
                    print(res, r, c)
        
        return res
            

            

            
        