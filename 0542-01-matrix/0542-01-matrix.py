class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        q = deque()
        visited = set()
        ROWS, COLS = len(mat), len(mat[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r,c,0))
                    visited.add((r,c))
        
        while q:
            r1,c1,d1 = q.popleft()
            mat[r1][c1] = d1

            for dr,dc in directions:
                row,col = r1 + dr, c1 + dc
                if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visited:
                    q.append((row, col, d1 + 1))
                    visited.add((row, col))
        
        return mat
