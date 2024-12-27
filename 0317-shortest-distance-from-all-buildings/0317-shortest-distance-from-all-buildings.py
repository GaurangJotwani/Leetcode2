class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        houses = set()
        obstacles = set()
        ROWS, COLS = len(grid), len(grid[0])
        cnts = [[0] * COLS for i in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    houses.add((r, c))
                elif grid[r][c] == 2:
                    obstacles.add((r,c))
        
        def bfs(s_r, s_c):
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            q = deque()
            visited = set()
            q.append((s_r,s_c,0))
            visited.add((s_r,s_c))

            while q:
                r,c,d = q.popleft()
                grid[r][c] += d
                cnts[r][c] += 1
                for dr,dc in directions:
                    row, col = r + dr, c + dc
                    if (0 <= row < ROWS and 0 <= col < COLS 
                        and (row, col) not in houses 
                        and (row,col) not in obstacles 
                        and (row,col) not in visited):
                        q.append((row,col,d + 1))
                        visited.add((row, col))

        for r,c in houses:
            bfs(r,c)
        
        res = float("inf")
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in houses and (r,c) not in obstacles and cnts[r][c] == len(houses):
                    res = min(grid[r][c], res)
        

        return res if res != float("inf") else -1


        












