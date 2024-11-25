class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        ans = 0
        seen = set()
        def dfs(r, c):
            seen.add((r, c))
            for dr,dc in dir:
                row, col = r + dr, c + dc
                if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in seen and grid[row][col] == '1':
                    dfs(row, col)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] == '1':
                    ans += 1
                    dfs(r, c)
        
        return ans
