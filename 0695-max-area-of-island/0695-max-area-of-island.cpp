class Solution {
public:
    int ROWS;
    int COLS;
    map<pair<int, int>, bool> seen;
    vector<vector<int>> directions = {{1,0},{-1,0},{0,1},{0,-1}};
    vector<vector<int>> grid;
    
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        
        ROWS = grid.size();
        COLS = grid[0].size();
        this->grid = grid;
        
        int maxArea = 0;
        
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] != 0 && seen.find({r, c}) == seen.end()) {
                    seen[{r, c}] = true;
                    maxArea = max(maxArea, dfs(r, c));
                }
            }
        }
        
        return maxArea;
    }
private:
    int dfs(int r, int c) {
        int res = 1;
        for (auto &dir : directions) {
            int row = r + dir[0];
            int col = c + dir[1];
            if (row >= 0 && row < ROWS 
                && col >= 0 && col < COLS
                && seen.find({row, col}) == seen.end() 
                && grid[row][col] != 0
               ) {
                seen[{row, col}] = true;
                res += dfs(row, col);
            }
        }
        
        return res;
    }
};