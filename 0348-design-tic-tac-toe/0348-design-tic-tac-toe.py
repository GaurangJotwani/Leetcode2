class TicTacToe:

    def __init__(self, n: int):
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.pos_diag = 0
        self.neg_diag = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        r = row
        c = col
        if player == 1:
            self.rows[r] += 1
            self.cols[c] += 1
            if row == col:
                self.pos_diag += 1
            if row + col == self.n - 1:
                self.neg_diag += 1
            if self.rows[r] == self.n or self.cols[c] == self.n or self.pos_diag == self.n or self.neg_diag == self.n:
                return 1
        else:
            self.rows[r] -= 1
            self.cols[c] -= 1
            if row == col:
                self.pos_diag -= 1
            if row + col == self.n - 1:
                self.neg_diag -= 1
            if self.rows[r] == -self.n or self.cols[c] == -self.n or self.pos_diag == -self.n or self.neg_diag == -self.n:
                return 2
        
        return 0




# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)