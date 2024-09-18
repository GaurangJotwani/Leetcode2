class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        def dfs1(r, c):
            visited.add((r, c))
            grid[r][c] = -1

            for dr,dc in directions:
                row, col = r + dr, c + dc
                if (row >= 0 and row < ROWS and
                    col >= 0 and col < COLS and
                    (row, col) not in visited and
                    grid[row][col] == 1):
                    dfs1(row, col)
        
        for r in range(ROWS):
            found = False
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs1(r, c)
                    found = True
                    break
            if found:
                break
        
        q = deque()
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    visited.add((r, c))
                    q.append((r,c,0))
        
        while len(q) > 0:
            r,c,d = q.popleft()
            if grid[r][c] == -1:
                return d - 1
            
            for dr,dc in directions:
                row, col = r + dr, c + dc
                if (row >= 0 and row < ROWS and
                    col >= 0 and col < COLS and
                    (row, col) not in visited):
                    visited.add((row, col))
                    q.append((row, col, d + 1))

        




        