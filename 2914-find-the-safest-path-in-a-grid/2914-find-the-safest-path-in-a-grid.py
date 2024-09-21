class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        safety_factors = [[0]*COLS for i in range(ROWS)]
        q = deque()
        vis = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r,c, 0))
                    vis.add((r, c))
        while q:
            r,c,d = q.popleft()
            safety_factors[r][c] = d

            for dr,dc in directions:
                row, col = r + dr, c + dc
                if (0 <= row < ROWS and 
                    0 <= col < COLS and
                    (row, col) not in vis):
                    q.append((row, col, d + 1))
                    vis.add((row, col))
        

        pq = []
        res = safety_factors[0][0]
        vis = set()
        heapq.heappush(pq, (-1 * safety_factors[0][0], 0, 0))

        while pq:
            safety, r, c = heapq.heappop(pq)
            safety = -1 * safety
            if (r, c) in vis:
                continue
            if r == ROWS - 1 and c == COLS - 1:
                return safety
            vis.add((r, c))
            for dr,dc in directions:
                row, col = r + dr, c + dc
                if (0 <= row < ROWS and 
                    0 <= col < COLS and
                    (row, col) not in vis):
                    heapq.heappush(pq,(-1 * min(safety, safety_factors[row][col]), row, col))


            



