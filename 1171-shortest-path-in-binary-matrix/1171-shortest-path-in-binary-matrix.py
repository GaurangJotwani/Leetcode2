class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        if grid[0][0] == 1: 
            return -1

        q.append((1,0,0))
        visited.add((0, 0))
        
        while q:
            d,r,c = q.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return d
            
            for dr,dc in directions:
                row, col = r + dr, c + dc
                if (row >= 0 and row < ROWS and
                    col >= 0 and col < COLS and
                    (row, col) not in visited and
                    grid[row][col] == 0):
                    visited.add((row, col))
                    q.append((d + 1, row, col))
        
        return -1


