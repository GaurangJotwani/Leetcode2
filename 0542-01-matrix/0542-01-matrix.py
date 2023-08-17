class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(mat), len(mat[0])
        res = [[0] * COLS for _ in range(ROWS)]
        
        
        q = deque()
        visited = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                
                if mat[r][c] == 0:
                    q.append((r,c,0))
                    visited.add((r,c))
        
        
        directions = [(0, 1),(0, -1),(1, 0),(-1, 0)]
        
        while q:
            for _ in range(len(q)):
                r,c,dist = q.popleft()
                res[r][c] = dist
                
                for dr,dc in directions:
                    row, col = r + dr, c + dc
                    
                    if (0 <= row < ROWS and
                        0 <= col < COLS and
                        (row,col) not in visited
                       ):
                        q.append((row,col, dist + 1))
                        visited.add((row,col))
            
        
        return res
        
        
        
        
                    