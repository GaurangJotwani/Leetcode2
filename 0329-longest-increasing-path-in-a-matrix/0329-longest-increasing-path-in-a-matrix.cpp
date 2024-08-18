class Solution {
public:
    int ROWS;
    int COLS;
    vector<vector<int>> dir = {{0, 1},{0, -1},{1, 0},{-1, 0}};
    vector<vector<int>> matrix;

    int dfs(int r, int c, vector<vector<int>> &dp) {
        if (dp[r][c] != -1) return dp[r][c];
        dp[r][c] = 0; // visiting
        int ans = 1;
        for (auto d: dir) {
            int row = d[0] + r;
            int col = d[1] + c;
            if (row >= 0 && row < ROWS && col >= 0 && col < COLS && matrix[row][col] > matrix[r][c] && dp[row][col] != 0) {
                ans = max(ans, 1 + dfs(row, col, dp));
            }
        }
        return dp[r][c] = ans;
        
    }

    int longestIncreasingPath(vector<vector<int>>& matrix) {
        this->matrix = matrix;
        ROWS = matrix.size();
        COLS = matrix[0].size();
        vector<vector<int>> dp(ROWS, vector<int>(COLS, -1));
        int res = 0;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (dp[r][c] == -1) {
                    int t = dfs(r, c, dp);
                    res = max(res, t);
                }
            }
        }
        return res;
    }

};