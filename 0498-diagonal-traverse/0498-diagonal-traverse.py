class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        ROWS,COLS = len(mat), len(mat[0])
        shouldReverse = False

        for r in range(0,ROWS):
            first = self.goDiagnolUp(mat, r, 0)
            res.append(first)
            if shouldReverse:
                res[-1].reverse()
            shouldReverse = not shouldReverse
        
        for c in range(1,COLS):
            first = self.goDiagnolUp(mat, ROWS - 1, c)
            res.append(first)
            if shouldReverse:
                res[-1].reverse()
            shouldReverse = not shouldReverse
            

        output = []
        for lst in res:
            output.extend(lst)
        return output
    
    def goDiagnolUp(self, mat, r, c):
        res = []

        while r < len(mat) and r >= 0 and c < len(mat[0]):
            res.append(mat[r][c])
            r -= 1
            c += 1
        
        return res