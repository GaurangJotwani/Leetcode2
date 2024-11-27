class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        dir = [[0,1],[0,-1],[1,0],[-1, 0]]
        dp = {}
        seen = set()
        
        def dfs(r, c, idx):
            
            if board[r][c] != word[idx]:
                return False
            
            if idx == len(word) - 1:
                return True

            for dr,dc in dir:
                row, col = r + dr, c + dc
                if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in seen:
                    seen.add((r, c))
                    if dfs(row, col, idx + 1):
                        return True
                    seen.remove((r,c))
            
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        
        return False

