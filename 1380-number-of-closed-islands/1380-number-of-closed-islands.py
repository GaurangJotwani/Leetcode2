class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dr = [[0,1],[0,-1],[1,0],[-1,0]]

        seen = set()
        def dfs1(r, c):
            seen.add((r, c))
            grid[r][c] = 1

            for d in dr:
                row = r + d[0]
                col = c + d[1]
                if (row >= 0 and row < ROWS and 
                    col >= 0 and col < COLS and
                    (row, col) not in seen and
                    grid[row][col] == 0):
                    dfs1(row, col)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (c == 0 or c == COLS - 1 or
                    r == 0 or r == ROWS - 1):
                    if (grid[r][c] == 0):
                        dfs1(r, c)

        seen = set()
        def dfs2(r, c):
            seen.add((r, c))
            for d in dr:
                row = r + d[0]
                col = c + d[1]
                if (row >= 0 and row < ROWS and 
                    col >= 0 and col < COLS and
                    (row, col) not in seen and
                    grid[row][col] == 0):
                    dfs2(row, col)
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] == 0:
                    dfs2(r, c)
                    res += 1
        
        return res

        


        