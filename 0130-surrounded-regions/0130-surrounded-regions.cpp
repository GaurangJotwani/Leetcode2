class Solution {
public:
    map<pair<int,int>, bool> visited;
    int ROWS;
    int COLS;
    vector<vector<int>> dir = {{1, 0},{-1, 0},{0, 1},{0, -1}};
    
    void solve(vector<vector<char>>& board) {
        ROWS = board.size();
        COLS = board[0].size();
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (r == 0 || c == 0 || r == ROWS - 1 || c == COLS - 1) {
                    if (board[r][c] == 'O' && visited.find({r, c}) == visited.end()) {
                        visited[{r, c}] = true;
                        board[r][c] = 'S';
                        dfs(r, c, board);
                    }
                }
            }
        }
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (board[r][c] == 'S') {
                    board[r][c] = 'O';
                } else if (board[r][c] == 'O') {
                    board[r][c] = 'X';
                }
            }
        }
        
    }
private:
    void dfs(int r, int c, vector<vector<char>>& board) {
        for (auto d: dir) {
            int row = r + d[0];
            int col = c + d[1];
            if (row >= 0 && row < ROWS &&
                col >= 0 && col < COLS &&
                visited.find({row, col}) == visited.end() &&
                board[row][col] == 'O'
               ) {
                board[row][col] = 'S';
                visited[{row, col}] = true;
                dfs(row, col, board);
            }
        }
    }
};