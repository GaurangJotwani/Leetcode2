class Solution {
public:
    vector<vector<char>> grid;
    map<pair<int, int>, bool> seen;
    int ROWS;
    int COLS;
    vector<vector<int>>dir{{1, 0},{-1, 0},{0, 1},{0, -1}};
    
    int numIslands(vector<vector<char>>& grid) {
        this->grid = grid;
        ROWS = grid.size();
        COLS = grid[0].size();
        int res = 0;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (seen.find({r, c}) != seen.end() || grid[r][c] == '0') continue;
                helper(r, c);
                res++;
            }
        }
        return res;
    }
private:
    void helper(int r, int c) {
        seen[{r, c}] = true;
        for (auto &d: dir) {
            int row = r + d[0];
            int col = c + d[1];
            if (row >= 0 && row < ROWS && 
                col >= 0 && col < COLS &&
                grid[row][col] != '0' &&
                seen.find({row, col}) == seen.end()) {
                helper(row, col);
            }
        }
    }
};