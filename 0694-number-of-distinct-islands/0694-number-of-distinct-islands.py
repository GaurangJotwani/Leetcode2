class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        left_most = []
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r,c):
            visited.add((r,c))
            for dr,dc in directions:
                row,col = r + dr, c + dc
                if not self.isOutOfBoundsOrZero(row, col, grid) and (row, col) not in visited:
                    dfs(row, col)
        
        total = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    left_most.append((r,c))
                    total += 1
                    dfs(r,c)
        
        already_done = set()
        for i in range(len(left_most)):
            r1,c1 = left_most[i]
            if (r1,c1) in already_done:
                continue
            for j in range(i + 1, len(left_most)):
                r2,c2 = left_most[j]
                seen = set()
                if self.areSame(r1, c1, r2, c2, grid, seen):
                    total -= 1
                    already_done.add((r2,c2))

        return total
    


    def areSame(self, r1, c1, r2, c2, matrix, visited):
        if (r1,c1) in visited:
            return True
        if self.isOutOfBoundsOrZero(r1, c1, matrix) and self.isOutOfBoundsOrZero(r2, c2, matrix):
            return True
        if self.isOutOfBoundsOrZero(r1, c1, matrix) or self.isOutOfBoundsOrZero(r2, c2, matrix):
            return False
        visited.add((r1,c1))
        
        return (self.areSame(r1 + 1, c1, r2 + 1, c2, matrix, visited) and 
                self.areSame(r1 - 1, c1, r2 - 1, c2, matrix, visited) and 
                self.areSame(r1, c1 - 1, r2, c2 - 1, matrix, visited) and
                self.areSame(r1, c1 + 1, r2, c2 + 1, matrix, visited))
    
    def isOutOfBoundsOrZero(self,r,c,matrix):
        return r >= len(matrix) or r< 0 or c < 0 or c >= len(matrix[0]) or matrix[r][c] == 0
