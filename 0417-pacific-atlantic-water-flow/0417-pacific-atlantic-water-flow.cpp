class Solution {
public:
    int ROWS;
    int COLS;
    vector<vector<int>> dir = {{1, 0},{-1, 0},{0, 1},{0, -1}};
    vector<vector<int>> grid;

    void dfs(int r, int c, vector<vector<bool>> &visited) {
        visited[r][c] = true;
        for (auto d: dir) {
            int row = r + d[0];
            int col = c + d[1];
            if (row >= 0 and row < ROWS && col >= 0 && col < COLS && !visited[row][col] && grid[r][c] <= grid[row][col]) {
                dfs(row, col, visited);
            }
        }
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        ROWS = heights.size();
        COLS = heights[0].size();
        this->grid = heights;
        vector<vector<bool>> pac(ROWS, vector<bool>(COLS, false));
        vector<vector<bool>> atl(ROWS, vector<bool>(COLS, false));

        for (int c = 0; c < COLS; c++) {
            if(!pac[0][c]) dfs(0,c,pac);
            if(!atl[ROWS - 1][c]) dfs(ROWS - 1,c,atl);
        }
        for (int r = 0; r < ROWS; r++) {
            if(!pac[r][0]) dfs(r,0,pac);
            if(!atl[r][COLS-1]) dfs(r,COLS-1,atl);
        }
        vector<vector<int>> res;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (atl[r][c] && pac[r][c]) res.push_back({r,c});
            }
        }
        return res;
    }
};