class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS, res = len(grid), len(grid[0]), 0
        q = deque()
        vis = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r, c, 0))
                    vis.add((r,c))
        
        while q:
            r, c, d = q.popleft()
            res = max(res, d)

            for dr,dc in directions:
                row, col = r + dr, c + dc
                if (row >= 0 and row < ROWS and 
                    col >= 0 and col < COLS and
                    (row, col) not in vis and
                    grid[row][col] == 0):
                    q.append((row, col, d + 1))
                    vis.add((row, col))
        

        return -1 if res == 0 else res

        


        