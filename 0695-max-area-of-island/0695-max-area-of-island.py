class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        seen = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        def dfs(r, c):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == 0 or 
                (r, c) in seen):
                return 0
            seen.add((r, c))
            area = 1
            for dr, dc in directions:
                row, col = r + dr, c + dc
                area += dfs(row, col)


            return area





        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea
    
    
        