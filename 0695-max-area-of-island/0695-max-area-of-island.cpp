class Solution {
public:
    int ROWS;
    int COLS;
    vector<vector<int>> grid;
    vector<vector<int>> dir = {{1, 0},{-1, 0},{0, 1},{0, -1}};
    
    int dfs(int r, int c, vector<vector<bool>> &visited) {
        visited[r][c] = true;
        int ans = 1;
        for (auto d: dir) {
            int row = r + d[0];
            int col = c + d[1];
            if (row >= 0 && row < ROWS && col >= 0 && col < COLS && !visited[row][col] && grid[row][col] == 1) {
                ans += dfs(row, col, visited);
            }
        }
        return ans;
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        this->grid = grid;
        ROWS = grid.size();
        COLS = grid[0].size();
        vector<vector<bool>> visited(ROWS, vector<bool>(COLS, false));
        int res = 0;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (!visited[r][c] && grid[r][c] == 1) {
                    res = max(res, dfs(r, c, visited));
                }
            }
        }
        return res;
    }
};