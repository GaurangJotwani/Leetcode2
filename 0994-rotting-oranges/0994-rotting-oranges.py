class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time = -1
        seen = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        fresh_orange_found = False
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    seen.add((r, c))
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_orange_found = True
        
        if not fresh_orange_found:
            return 0
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (0 <= row < ROWS and
                        0 <= col < COLS and
                        (row, col) not in seen and
                        grid[row][col] == 1
                       ):
                        grid[row][col] = 2
                        seen.add((row, col))
                        q.append((row, col))
            time += 1
                        
        
        # print(grid, time)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return time
                
            
        
        
        
        
        
        