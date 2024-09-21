class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        ROWS, COLS = len(heights),len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        pq = []
        heapq.heappush(pq,(0,0,0))
        vis = set()

        while pq:
            diff,r,c = heapq.heappop(pq)
            if (r,c) in vis:
                continue
            vis.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return diff
            
            for dr,dc in directions:
                row, col = r + dr, c + dc
                if (0 <= row < ROWS and 
                    0 <= col < COLS and 
                    (row, col) not in vis):
                    diff2 = abs(heights[r][c] - heights[row][col])
                    heapq.heappush(pq, (max(diff, diff2),row, col))
            
        
        