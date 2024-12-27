class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid[0]), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        visited = set()
        sizes = defaultdict(int)
        sizes[0] = 0

        def dfs(r,c,island):
            visited.add((r, c))
            grid[r][c] = island
            ans = 1
            for dr,dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visited and grid[row][col] == 1:
                    ans += dfs(row, col, island)
            return ans
        
        max_island = 0
        island = 1
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == 1:
                    size = dfs(r,c,island)
                    sizes[island] = size
                    max_island = max(max_island, size)
                    island += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    boundry_islands = set()
                    for dr,dc in directions:
                        row, col = r + dr, c + dc
                        if 0 <= row < ROWS and 0 <= col < COLS:
                            boundry_islands.add(grid[row][col])
                    tmp = 1
                    for island in boundry_islands:
                        tmp +=  sizes[island]
                    max_island = max(tmp, max_island)
        
        return max_island



