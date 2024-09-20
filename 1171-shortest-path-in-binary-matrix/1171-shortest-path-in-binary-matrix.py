class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        minHeap = []
        visited = set()

        if grid[0][0] == 1: 
            return -1

        heapq.heappush(minHeap, (1,0,0))
        
        while minHeap:
            d,r,c = heapq.heappop(minHeap)
            if (r,c) in visited:
                continue
            
            visited.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return d
            
            for dr,dc in directions:
                row, col = r + dr, c + dc
                if (row >= 0 and row < ROWS and
                    col >= 0 and col < COLS and
                    (row, col) not in visited and
                    grid[row][col] == 0):
                    heapq.heappush(minHeap, (d + 1, row, col))
        
        return -1


