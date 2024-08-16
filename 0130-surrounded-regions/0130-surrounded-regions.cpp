class Solution {
public:
    void dfs(int r, int c, vector<vector<char>>& board, vector<vector<bool>> &visited) {
        visited[r][c] = true;
        board[r][c] = 'S';
        for (auto d: dir) {
            int row = r + d[0];
            int col = c + d[1];
            if (row >= 0 && row < ROWS && col >= 0 && col < COLS && !visited[row][col] && board[row][col] == 'O') {
                dfs(row, col, board, visited);
            }
        }
    }

    void solve(vector<vector<char>>& board) {
        ROWS = board.size();
        COLS = board[0].size();
        vector<vector<bool>> visited(ROWS, vector<bool>(COLS, false));
        for (int r = 0; r< ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (r == 0 || r == ROWS - 1 || c == 0 || c == COLS - 1) {
                    if (!visited[r][c] && board[r][c] == 'O') {
                        dfs(r, c, board, visited);
                    }
                }
            }
        }
        for (int r = 0; r< ROWS; r++) {
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
    int ROWS;
    int COLS;
    vector<vector<int>> dir = {{0, 1},{0, -1},{1, 0},{-1, 0}};
};